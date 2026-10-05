import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove the Hero button
html = re.sub(r'<a href="https://wa\.me/558597496713" target="_blank" class="cta-btn">.*?</a>', '', html, flags=re.DOTALL)

# 2. Remove the social links row in the bottom footer
html = re.sub(r'<div style="display: flex; justify-content: center; align-items: center; gap: 2rem; flex-wrap: wrap; margin: 2rem 0;">.*?</div>\s*</div>', '', html, flags=re.DOTALL)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("CTAs removed from body.")
