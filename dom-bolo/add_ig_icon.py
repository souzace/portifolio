import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# The Instagram SVG icon
ig_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px; vertical-align: middle; position: relative; top: -1px;"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>"""

# Replace the sticky-btn text to include the icon
# Currently it is: <a href="https://www.instagram.com/dombolofortal/" target="_blank" class="sticky-btn">Pedir no WhatsApp</a>
html = re.sub(
    r'<a href="https://www\.instagram\.com/dombolofortal/" target="_blank" class="sticky-btn">Pedir no WhatsApp</a>',
    f'<a href="https://www.instagram.com/dombolofortal/" target="_blank" class="sticky-btn" style="display: flex; align-items: center;">{ig_svg}Fazer Pedido</a>',
    html
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Instagram icon added.")
