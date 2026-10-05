import re

with open("beluton/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Subtitle/Phrase
# Currently: <span class="logo-sub">Luthieria</span>
html = html.replace('<span class="logo-sub">Luthieria</span>', '<span class="logo-sub">Luthieria Contemporânea</span>')

# 2. Update WhatsApp Links
# Currently: href="https://wa.me/"
html = html.replace('href="https://wa.me/"', 'href="https://api.whatsapp.com/send?phone=558597591685"')

with open("beluton/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Text and WA link updated.")
