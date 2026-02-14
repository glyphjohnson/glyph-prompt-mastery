#!/bin/bash
set -e
cd /home/glyph/.openclaw/workspace/glyph-dashboard
mkdir -p data
SESSIONS=$(openclaw sessions list --json)
STATUS=$(openclaw status --json)
openclaw sessions list --json > tmp_sessions.json
openclaw status --json > tmp_status.json
node -e "
const fs = require('fs');
const sessions = JSON.parse(fs.readFileSync('tmp_sessions.json', 'utf8'));
const status = JSON.parse(fs.readFileSync('tmp_status.json', 'utf8'));
const data = {
  timestamp: new Date().toISOString(),
  sessions,
  status
};
fs.writeFileSync('data/status.json', JSON.stringify(data, null, 2));
fs.unlinkSync('tmp_sessions.json');
fs.unlinkSync('tmp_status.json');
" || rm -f tmp_*.json
git add data/status.json || true
git commit -m "Update status at $(date)" || true
git push origin main || true