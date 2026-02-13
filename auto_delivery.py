#!/usr/bin/env python3
import imaplib
import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import re
import sys
import time

GMAIL_USER = os.getenv('GMAIL_USER', 'boyisak@gmail.com')
GMAIL_PASS = os.getenv('GMAIL_APP_PASS')

PACK_MAP = {
    'E-Commerce SEO Pack': 'products/seo-pack.md',
    'E-Commerce Copy Pack': 'products/copy-pack.md',
    'E-Commerce Upsell Pack': 'products/upsell-pack.md',
    'E-Commerce CS Pack': 'products/cs-pack.md',
    'E-Commerce Mega Pack': 'products/e-commerce-prompt-mastery.md',
}

def parse_email(msg):
    full_body = ''
    for part in msg.walk():
        ctype = part.get_content_type()
        if ctype in ['text/plain', 'text/html']:
            try:
                payload = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                full_body += payload
            except:
                pass
    buyer_match = re.search(r'Buyer[:\\s]*([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,})', full_body, re.I)
    buyer = buyer_match.group(1) if buyer_match else None

    amount_match = re.search(r'\\$(\\d+\\.\\d{2})', full_body)
    amount = float(amount_match.group(1)) if amount_match else 0.0

    item_match = re.search(r'(?:Item|Description|Name|Product)[:\\s]*([^\\n&lt;]{1,100})', full_body, re.I)
    item_desc = item_match.group(1).strip() if item_match else ''

    return buyer, amount, item_desc

def deliver_pack(buyer_email, pack_key, dry_run=False):
    filename = PACK_MAP.get(pack_key)
    if not filename or not os.path.exists(filename):
        print('Pack not found: %s (%s)' % (pack_key, filename))
        return False

    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = buyer_email
    msg['Subject'] = 'Your E-Commerce Prompt Pack: %s' % pack_key

    body = '''Thank you for your purchase!

Your AI prompt pack is attached as Markdown file. Copy-paste into ChatGPT/Claude/Gemini for instant use.

Scale your Shopify/Etsy store 10x! 

Best,
Glyph Johnson'''
    msg.attach(MIMEText(body, 'plain'))

    try:
        with open(filename, 'rb') as f:
            part = MIMEBase('text', 'markdown')
            part.set_payload(f.read())
        encoders.encode_base64(part)
        safe_name = pack_key.replace(' ', '_').replace('E-Commerce ', '').lower() + '.md'
        part.add_header('Content-Disposition', 'attachment; filename=%s' % safe_name)
        msg.attach(part)

        if dry_run:
            print('DRY-RUN: Would send to %s: %s' % (buyer_email, safe_name))
            return True

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASS)
        server.sendmail(GMAIL_USER, buyer_email, msg.as_string())
        server.quit()
        print('Delivered %s to %s' % (pack_key, buyer_email))
        return True
    except Exception as e:
        print('Delivery error: %s' % str(e))
        return False

def main(dry_run=False):
    if not GMAIL_PASS:
        print('Set GMAIL_APP_PASS env var')
        return

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(GMAIL_USER, GMAIL_PASS)
    mail.select('inbox')

    typ, data = mail.search(None, '(UNSEEN FROM \"paypal.com\")')
    msg_ids = data[0].split()

    for num in msg_ids:
        typ, data = mail.fetch(num, '(RFC822)')
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        subject = msg['Subject'] or ''
        if 'received' not in subject.lower() and 'completed' not in subject.lower():
            continue

        buyer, amount, item_desc = parse_email(msg)
        if not buyer:
            print('No buyer found')
            continue

        pack_key = None
        ldesc = item_desc.lower()
        if amount == 12.99 or 'mega' in ldesc:
            pack_key = 'E-Commerce Mega Pack'
        else:
            for key in PACK_MAP:
                if key.lower() in ldesc:
                    pack_key = key
                    break

        if pack_key:
            deliver_pack(buyer, pack_key, dry_run)
            mail.store(num, '+FLAGS', '\\Seen')
        else:
            print('Unknown pack: amount=%.2f, desc=%r' % (amount, item_desc[:100]))

    mail.close()
    mail.logout()

if __name__ == '__main__':
    dry_run = '--dry' in sys.argv
    main(dry_run)