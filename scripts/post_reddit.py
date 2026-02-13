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
