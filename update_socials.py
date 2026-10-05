import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Define the Facebook SVG
fb_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>'

# Update Main Footer Links
# 1. Instagram
html = re.sub(
    r'<a href="#" aria-label="Instagram">',
    r'<a href="https://www.instagram.com/mvnilson/" target="_blank" aria-label="Instagram">',
    html,
    count=1
)
# 2. YouTube
html = re.sub(
    r'<a href="#" aria-label="YouTube">',
    r'<a href="https://www.youtube.com/@NilsonVieira" target="_blank" aria-label="YouTube">',
    html,
    count=1
)
# 3. WhatsApp
html = re.sub(
    r'<a href="#" aria-label="WhatsApp">',
    r'<a href="https://wa.me/5585997496713" target="_blank" aria-label="WhatsApp">',
    html,
    count=1
)
# Add Facebook to Main Footer
# Find the WhatsApp link block and append Facebook after it
wa_block = r'<a href="https://wa.me/5585997496713" target="_blank" aria-label="WhatsApp">\s*<svg.*?</svg>\s*</a>'
match = re.search(wa_block, html, re.DOTALL)
if match:
    fb_link = f'\n        <a href="https://www.facebook.com/mvnilson" target="_blank" aria-label="Facebook">\n            {fb_svg}\n        </a>'
    html = html[:match.end()] + fb_link + html[match.end():]


# Update Sticky Footer Links
# 1. WhatsApp
html = re.sub(
    r'<a href="#" class="sticky-social-btn" aria-label="WhatsApp"',
    r'<a href="https://wa.me/5585997496713" target="_blank" class="sticky-social-btn" aria-label="WhatsApp"',
    html
)
# 2. Instagram
html = re.sub(
    r'<a href="#" class="sticky-social-btn" aria-label="Instagram"',
    r'<a href="https://www.instagram.com/mvnilson/" target="_blank" class="sticky-social-btn" aria-label="Instagram"',
    html
)
# 3. YouTube
html = re.sub(
    r'<a href="#" class="sticky-social-btn" aria-label="YouTube"',
    r'<a href="https://www.youtube.com/@NilsonVieira" target="_blank" class="sticky-social-btn" aria-label="YouTube"',
    html
)
# Add Facebook to Sticky Footer
wa_sticky_block = r'<a href="https://www.youtube.com/@NilsonVieira" target="_blank" class="sticky-social-btn" aria-label="YouTube" title="Ver no YouTube">\s*<svg.*?</svg>\s*</a>'
match_sticky = re.search(wa_sticky_block, html, re.DOTALL)
if match_sticky:
    fb_sticky_link = f'\n        <a href="https://www.facebook.com/mvnilson" target="_blank" class="sticky-social-btn" aria-label="Facebook" title="Curtir no Facebook">\n            {fb_svg}\n        </a>'
    html = html[:match_sticky.end()] + fb_sticky_link + html[match_sticky.end():]

# Fix WhatsApp number (user said 85 9749-6713, which means 99749-6713 in Brazil usually, but let's use what they wrote: 558597496713)
html = html.replace("5585997496713", "558597496713")

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Social links updated.")
