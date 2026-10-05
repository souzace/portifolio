import re

with open("beluton/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace Hero Background
old_hero_bg = """    background: linear-gradient(135deg, #0a0a0a 0%, #2a2312 100%);"""
new_hero_bg = """    background: linear-gradient(rgba(10,10,10,0.7), rgba(10,10,10,0.85)), url('sax_repair.jpg');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;"""
css = css.replace(old_hero_bg, new_hero_bg)

# Replace CTA Background
old_cta_bg = """    background: linear-gradient(rgba(10,10,10,0.9), rgba(10,10,10,0.9)), url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" opacity="0.05"><circle cx="50" cy="50" r="40" fill="%23D4AF37"/></svg>');
    background-size: 200px;"""
new_cta_bg = """    background: linear-gradient(rgba(10,10,10,0.85), rgba(10,10,10,0.9)), url('brass_cta.jpg');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;"""
css = css.replace(old_cta_bg, new_cta_bg)

with open("beluton/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Background images updated.")
