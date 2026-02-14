import os
import re

dirr = 'projects/glyph-prompt-mastery'
pages = ['index.html', 'about.html', 'seo.html', 'copy.html', 'cs.html', 'upsell.html']
keywords = 'AI prompts, ecommerce SEO prompts, shopify prompts, etsy prompts, copywriting prompts, upsell prompts, customer service prompts, chatgpt prompts, claude prompts, prompt engineering'

for page in pages:
    path = os.path.join(dirr, page)
    with open(path, 'r') as f:
        content = f.read()
    title_match = re.search(r'<title>([^<]+)</title>', content)
    desc_match = re.search(r'<meta\\s+name="description"\\s+content="([^"]*)"\\s*>', content)
    title = title_match.group(1) if title_match else 'Glyph Prompt Mastery'
    desc = desc_match.group(1) if desc_match else ''
    url = 'https://glyph-prompt-mastery.com/' + page
    if page == 'index.html':
        schema_type = 'WebSite'
    else:
        schema_type = 'WebPage'
    schema = '''{
  "@context": "https://schema.org",
  "@type": "%s",
  "name": "%s",
  "description": "%s",
  "url": "%s"
}''' % (schema_type, title, desc, url)
    new_metas = '''    <meta name="keywords" content="%s">
    <meta property="og:title" content="%s">
    <meta property="og:description" content="%s">
    <meta property="og:type" content="website">
    <meta property="og:url" content="%s">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="%s">
    <meta name="twitter:description" content="%s">
    <link rel="canonical" href="%s">
    <script type="application/ld+json">
%s
    </script>''' % (keywords, title, desc, url, title, desc, url, schema)
    # Replace the description meta followed by style with desc + new_metas + style
    pattern = r'(<meta\\s+name="description"\\s+content="[^"]*"[^>]*)>\\s*\\n\\s*<style>'
    replacement = r'\\1>\n' + new_metas + '\n    <style'
    content = re.sub(pattern, replacement, content)
    with open(path, 'w') as f:
        f.write(content)
    print('Updated ' + page + ': ' + title + ', ' + desc[:50] + '...')
