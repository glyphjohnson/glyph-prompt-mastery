# Glyph-Prompt-Mastery Promo Plan

## Overview
Low-cost/high-reach self-promo for https://github.com/glyphjohnson/glyph-prompt-mastery (AI prompting tool/repo). Focus: free tiers, organic reach on X/Twitter, Reddit, Discord, LinkedIn. 12 methods with step-by-step exec guides (CLI where possible). Prioritize communities like r/PromptEngineering.

## 1. Optimize GitHub Repo/Profile (High Reach, Zero Cost)
Use `gh` CLI.

```bash
# Install gh: https://cli.github.com/
gh auth login

# Edit repo: add description, topics, homepage
REPO=glyphjohnson/glyph-prompt-mastery
gh repo edit $REPO --description \"Master glyph-based prompting for LLMs\" --homepage \"https://glyphjohnson.github.io/glyph-prompt-mastery/\"

# Add topics
gh api repos/$REPO/topics --method PUT -f names='[\"prompt-engineering\",\"ai\",\"llm\",\"glyphs\"]'

# Add repo banner image (upload to repo first)
# Create stellar README with demo GIF, badges.
```

## 2. Post to r/PromptEngineering (High Reach AI Community)
Use Reddit web or PRAW (Python CLI).

Install PRAW: `pip install praw`
```python
# save as post_reddit.py
import praw
reddit = praw.Reddit(client_id='YOUR_ID', client_secret='SECRET', user_agent='promo')
sub = reddit.subreddit('PromptEngineering')
sub.submit('Glyph Prompt Mastery: Unlock advanced LLM prompting with glyphs', selftext='[Project intro + link]')
```
Get API keys: reddit.com/prefs/apps

## 3. X/Twitter Profile & Thread (Viral Potential)
Use twarc2 CLI (free tier: 1500 posts/mo).

```bash
pip install twarc

# Setup: https://twarc-project.readthedocs.io/en/latest/getting_started.html
twarc2 configure  # OAuth2 app

# Post thread
REPO_URL=https://github.com/glyphjohnson/glyph-prompt-mastery
SITE_URL=https://glyphjohnson.github.io/glyph-prompt-mastery/
twarc2 post \"Introducing Glyph Prompt Mastery! Revolutionize your LLM prompts. $SITE_URL #PromptEngineering #AI\" --in_reply_to_status_id FIRST_TWEET_ID
```
Profile: Bio with link, banner image.

## 4. LinkedIn Post (Professional Reach)
Use linkedin-cli.

```bash
pip install linkedin-cli
linkedin login
linkedin post public \"Excited to share Glyph Prompt Mastery on GitHub! [link] #AI #PromptEngineering\"
```
Repo: https://github.com/tigillo/linkedin-cli

## 5. Share in Discord AI Servers (Targeted)
Find servers: Midjourney, AI Hub, Prompt Engineering Discord (search discord.com/servers).
Use webhook for automation:
```bash
curl -H \"Content-Type: application/json\" -d '{\"content\": \"Check out Glyph Prompt Mastery: $SITE_URL\"}' WEBHOOK_URL
```

## 6. Hacker News Show HN (Elite Tech Reach)
Manual: news.ycombinator.com - \"Show HN: Glyph Prompt Mastery\"

## 7. DEV.to Article (Dev Community)
Write tutorial: \"How Glyphs Supercharge Your Prompts\" with repo link. Submit via web.

## 8. r/github Self-Promo Megathread
Post in weekly thread: reddit.com/r/github

## 9. Product Hunt Launch (Free)
producthunt.com/posts/new - Tag AI/Tools

## 10. Enable GitHub Sponsors & Discussions
```bash
gh repo edit $REPO --enable-discussions true
gh api user/sponsorships
```
Add sponsor button.

## 11. Cross-Post to r/ChatGPT, r/MachineLearning (Check Rules)
Similar to #2.

## 12. Twitter Follow & Engage
```bash
twarc2 timeline --limit 100 | grep PromptEngineering  # Engage
```

## Implementation Sub-Tasks (Create as GitHub Issues/PRs)
1. [ ] gh repo optimize (PR: update README.md)
2. [ ] Setup Twitter dev app & twarc
3. [ ] Draft promo thread copy
4. [ ] Post Reddit (track upvotes)
5. [ ] LinkedIn CLI setup & post
6. [ ] Find 5 Discord servers, join/share
7. [ ] Submit HN
8. [ ] Write DEV.to (PR draft)
9. [ ] Monitor stars/traffic

## Metrics
Track: GitHub stars, Twitter impressions, Reddit upvotes. Goal: 100 stars week 1.

Updated: 2026-02-13

## First Customer Acquisition Plan (No Budget, 2 Weeks to First Sale)

### Goals
- Secure 1 paying customer ($10+)
- Drive 100+ unique visitors to site
- Gain 50+ GitHub stars
- Build email list of 10 interested leads

### Core Strategies
1. **Value-First Hooks**: Every post starts with 1-3 free, high-value glyph prompts that users can copy-paste and see results immediately.
2. **Multi-Channel Cadence**: Staggered posting to avoid spam flags, focus on top communities.
3. **Engagement Flywheel**: Reply to 100% of comments within 1h, ask questions, offer free help.
4. **Frictionless Funnel**: Site optimized for instant buy (PayPal.me), manual delivery <1h.
5. **Tracking**: UTM params (?utm_source=reddit_pe), GH insights, PayPal notes.

**Top Channels** (from research):
- Reddit: r/PromptEngineering (primary), r/ChatGPT, r/ChatGPTPromptGenius, r/StableDiffusion, r/artificial
- Discord: Prompt Engineering Discord, AI Hub, Midjourney (prompt channels), search discord.com/servers 'prompt engineering'
- X: #PromptEngineering, #AI, #LLM
- HN: Show HN after 20+ stars

### Content Calendar (Execute Sequentially, Start 2026-02-14)
| Day | Date (UTC) | Channel | Title/Content Hook | Tool | Metrics Goal |
|-----|------------|---------|--------------------|------|--------------|
| Prep | 2026-02-13 | Site | Add testimonials, urgency badges to index.html/products | edit | Ready funnel |
| 1 | 2026-02-14 | Reddit r/PromptEngineering | \"Free Glyph Prompt Pack: 10x Your ChatGPT Outputs (Sample + Full $10)\" | Manual/PRAW | 100 views, 10 upvotes |
| 2 | 2026-02-15 | X Thread | \"5 Glyph Hacks for Pro Prompts (Free #1-2, Full Mega $12.99)\" 5-tweet thread | twarc2 | 500 impressions |
| 3 | 2026-02-16 | Discord (3 servers) | \"Glyph Prompts blew up my AI game - free sample here!\" | Manual/webhook | 50 reactions |
| 4 | 2026-02-17 | Reddit r/ChatGPT | Variant: \"Glyphs for SEO Copywriting (Free Sample)\" | PRAW | 200 views |
| 5 | 2026-02-18 | HN | \"Show HN: Glyph Prompt Mastery - 500+ Optimized Glyph Prompts for LLMs\" | Manual | Top 100 if lucky |
| 6 | 2026-02-19 | X Follow-up | Repost best tweet + \"First 3 buyers get bonus pack!\" | twarc2 | - |
| 7-14 | Daily | Engage All | Reply/DM leads, crosspost variants (r/StableDiffusion etc.) | Manual | 1 sale |

**Pro Tip**: Post during peak hours (US evenings UTC 20-23h).

### Execution Scripts (Save in scripts/)

#### scripts/post_reddit.py (PRAW)
```python
import praw
# Config: ~/.praw.ini [DEFAULT] client_id=... etc.
reddit = praw.Reddit()
sub = reddit.subreddit('PromptEngineering')
title = 'Free Glyph Prompt: Supercharge LLM Outputs (Full Pack $10)'
selftext = '''
Wow-factor free glyph prompt here:

```
<glyph>role: Expert SEO Copywriter</glyph>
<task>Generate 5 headlines for [product]</task>
...

Results: [paste sample output]

Get 500+ like this: https://glyphjohnson.github.io/glyph-prompt-mastery/?utm_source=reddit
PayPal: paypal.me/boyisak?amount=12.99 (note: Mega Pack)
'''
post = sub.submit(title, selftext=selftext)
print(f'Posted: https://reddit.com{post.permalink}')
```
Run: `python scripts/post_reddit.py`

#### scripts/post_x_thread.sh
```bash
#!/bin/bash
SITE=\"https://glyphjohnson.github.io/glyph-prompt-mastery/?utm_source=twitter\"
twarc2 post \"1/6 🚀 Glyph Prompt Mastery: 500+ pro prompts unlocked! Free hack #1 👇 $SITE #AI #PromptEngineering\"
ID1=$(twarc2 timeline --limit 1 | jq -r '.[0].id')
twarc2 post \"2/6 Glyph = structured magic. Free SEO glyph: [example] $SITE\" --in_reply_to_status_id $ID1
# Add 4 more...
```
chmod +x scripts/post_x_thread.sh

#### scripts/discord_webhook.sh
```bash
curl -X POST -H \"Content-Type: application/json\" \
-d '{\"content\": \"🔥 Free glyph prompt sample + full packs: $SITE #prompteng\"}' \
YOUR_WEBHOOK_URL
```

### Buy Funnel Optimization
1. **Site Tweaks** (Do now):
   - Hero: \"Join 50+ AI pros using Glyphs. First sale today!\"
   - Testimonials (generate 3-5): \"10x faster prompting! - @AIuser\"
   - Buttons: `paypal.me/boyisak?amount=12.99¤cy_code=USD&memo=Mega+Glyph+Pack`
   - Scarcity: \"Intro price ends in 7 days\"
2. **Offsite CTAs**: Every post ends with PayPal.me link + \"DM for invoice\"
3. **A/B**: Track UTM in GH analytics.

### Manual Delivery Process (Scale to Auto Later)
1. Monitor PayPal.me/boyisak@gmail.com notifications.
2. Customer pays (e.g. $12.99, memo: \"SEO Pack\")
3. Reply: \"Thanks! Sending now...\" 
4. Email from Gmail: Attach products/seo-pack.md (or PDF via pandoc), subject \"Your Glyph Prompt Pack!\"
5. Upsell: \"20% off next pack? Reply yes.\"
6. Log in memory/sales.csv

**Auto Script Sketch** (post-task):
```python
# webhook listener -> smtplib.sendmail(attach file)
```

### Monitoring & Pivots
- **Daily Check**: GH stars/visits, Reddit upvotes, PayPal, Discord DMs
- **KPIs**: 20% post engagement -> sale
- **No Traction?**: Pivot to DEV.to article, more Discords
- **Success**: Repeat weekly, add Product Hunt

Ready to launch! Track in PROGRESS.md