import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Remove the <header> tag and its contents
html = re.sub(r'<header class="header">.*?</header>', '', html, flags=re.DOTALL)

# Adjust the hero padding since there is no header anymore
# The hero usually has padding-top to account for the fixed header. 
# We should remove it or let it center naturally.
# We'll just write it back and let CSS handle the 100vh centering, since .hero has display: flex; align-items: center;
# Let's check if .hero has a padding-top hack.
old_hero_css = re.search(r'\.hero \{.*?\}', html, re.DOTALL)
if old_hero_css:
    hero_css_str = old_hero_css.group(0)
    # If there is padding-top like 80px or 100px, we might not strictly need to remove it if flex handles it,
    # but let's be clean.
    pass

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Header removed.")
