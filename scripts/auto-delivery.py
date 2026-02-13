#!/usr/bin/env python3
import imaplib
import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import sys
import argparse
import time
import glob
import re
import subprocess

GMAIL_USER = os.getenv('GMAIL_USER', 'glyphjohnson@gmail.com')
GMAIL_PASS = os.getenv('GMAIL_PASS')  # Use Gmail App Password
IMAP_SERVER = 'imap.gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
PRODUCTS_DIR = 'products'

def ensure_pdfs(dry_run=False):
    \"\"\"Generate PDF from MD files if PDF doesn't exist.\"\"\"
    md_files = glob.glob(f'{PRODUCTS_DIR}/*.md')
    for md_file in md_files:
        pdf_file = md_file.replace('.md', '.pdf')
        if not os.path.exists(pdf_file):
            if dry_run:
                print(f"[DRY-RUN] Would generate {pdf_file}")
            else:
                try:
                    subprocess.run(['pandoc', md_file, '-o', pdf_file, '--quiet'], check=True, capture_output=True)
                    print(f"Generated {pdf_file}")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to generate {pdf_file}: {e}")

def get_text(msg):
    \"\"\"Extract plain text from email.\"\"\"
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == 'text/plain':
                try:
                    return part.get_payload(decode=True).decode('utf-8', errors='ignore')
                except:
                    pass
    else:
        try:
            return msg.get_payload(decode=True).decode('utf-8', errors='ignore')
        except:
            pass
    # Fallback to HTML stripped roughly
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/html':
                try:
                    html = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                    text = re.sub('<[^<]+?>', ' ', html)
                    text = re.sub(r'\\s+', ' ', text).strip()
                    return text
                except:
                    pass
    return ''

def extract_buyer_email(text):
    \"\"\"Extract buyer email from PayPal notification text.\"\"\"
    patterns = [
        r'Email address[:\\s]*([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,})',
        r'Email[:\\s]*([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,})',
        r'Sender\'s email address[:\\s]*([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,})',
        r'payer_email[:=\\s]*([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,})',
        r'Primary email[:\\s]*([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,})',
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            candidate = match.group(1).strip()
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', candidate):
                if 'paypal' not in candidate.lower():
                    return candidate
    return None

def get_product_files():
    \"\"\"Get list of product files (MD and PDF).\"\"\"
    files = []
    files.extend(glob.glob(f'{PRODUCTS_DIR}/*.md'))
    files.extend(glob.glob(f'{PRODUCTS_DIR}/*.pdf'))
    return [f for f in files if os.path.isfile(f)]

def send_delivery_email(buyer_email, dry_run=False):
    \"\"\"Send products to buyer.\"\"\"
    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = buyer_email
    msg['Subject'] = 'Thank you for your purchase! Your digital products are attached.'

    body = '''Dear Customer,

Thank you for your purchase from Glyph Prompt Mastery.
Please find your digital product(s) attached as Markdown and PDF files.

If you have any questions, reply to this email.

Best regards,
Glyph Johnson
glyphjohnson@gmail.com'''
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    product_files = get_product_files()
    for filename in product_files:
        try:
            basename = os.path.basename(filename)
            with open(filename, 'rb') as attachment:
                if filename.endswith('.md'):
                    part = MIMEText(attachment.read().decode('utf-8'), 'plain', 'utf-8')
                    part.add_header('Content-Disposition', f'attachment; filename="{basename}"')
                else:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename="{basename}"')
                msg.attach(part)
        except Exception as e:
            print(f'Failed to attach {filename}: {e}')

    if dry_run:
        print(f'[DRY-RUN] Would send email to {buyer_email} with {len(product_files)} attachments')
        return True

    try:
        server = smtplib.SMTP(SMTP_SERVER, 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASS)
        server.sendmail(GMAIL_USER, buyer_email, msg.as_string())
        server.quit()
        print(f'Successfully sent delivery email to {buyer_email}')
        return True
    except Exception as e:
        print(f'Failed to send email to {buyer_email}: {e}')
        return False

def poll_gmail(dry_run=False):
    \"\"\"Poll Gmail for new PayPal payment notifications.\"\"\"
    if not dry_run:
        ensure_pdfs(dry_run)
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(GMAIL_USER, GMAIL_PASS)
        mail.select('inbox')
        # Search for unseen PayPal emails
        search_criteria = '(UNSEEN FROM "paypal.com")'
        status, message_numbers = mail.search(None, search_criteria)
        message_numbers = message_numbers[0].split(b' ')
        processed = 0
        for num in message_numbers:
            if not num:
                continue
            status, msg_data = mail.fetch(num, '(RFC822)')
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)
            text = get_text(msg)
            buyer_email = extract_buyer_email(text)
            if buyer_email:
                print(f'Found payment notification for buyer: {buyer_email}')
                sent = send_delivery_email(buyer_email, dry_run)
                if sent or dry_run:
                    mail.store(num, '+FLAGS', '\\Seen')
                    processed += 1
            else:
                print(f'No buyer email extracted from message {num}')
                mail.store(num, '+FLAGS', '\\Seen')
        mail.close()
        print(f'Poll complete. Processed {processed} payments.')
    except Exception as e:
        print(f'Poll error: {e}')

def main():
    parser = argparse.ArgumentParser(description='Auto-delivery script for PayPal payments via Gmail polling.')
    parser.add_argument('--dry-run', '-d', action='store_true', help='Dry run: no login or send')
    parser.add_argument('--once', '-o', action='store_true', help='Run once and exit')
    parser.add_argument('--interval', '-i', type=int, default=60, help='Polling interval in seconds (default: 60)')
    args = parser.parse_args()

    print('Starting PayPal auto-delivery poller...')
    print(f'Gmail: {GMAIL_USER}')
    print(f'Products: {len(get_product_files())} files')

    if args.once:
        poll_gmail(args.dry_run)
    else:
        while True:
            poll_gmail(args.dry_run)
            if args.once:  # shouldn't happen
                break
            time.sleep(args.interval)

if __name__ == '__main__':
    if not GMAIL_PASS:
        print('ERROR: GMAIL_PASS environment variable required.')
        sys.exit(1)
    main()
