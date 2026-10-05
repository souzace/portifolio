import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove ONLY the hero button
html = re.sub(r'<a href="https://wa\.me/558597496713" target="_blank" class="cta-btn">.*?Entre em Contato</a>', '', html, flags=re.DOTALL)

# 2. Remove ONLY the social-links container from the #contato footer
# We need to be non-greedy and stop at the closing div of social-links container
match = re.search(r'<div style="display: flex; justify-content: center; align-items: center; gap: 2rem; flex-wrap: wrap; margin: 2rem 0;">.*?</a>\s*</div>', html, re.DOTALL)
if match:
    html = html.replace(match.group(0), '')

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("CTAs removed carefully.")
