import re

with open("el-bethel/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Change sticky footer text
html = html.replace('WhatsApp\n                </a>', 'Enviar Receita\n                </a>')

with open("el-bethel/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("el-bethel/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Make sure product images are perfectly sized
old_css_img = """.product-card img {
    width: 100%;
    height: auto;
    object-fit: contain;
    transition: transform 0.3s ease;
}"""

new_css_img = """.product-card img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    transition: transform 0.3s ease;
}"""

css = css.replace(old_css_img, new_css_img)

with open("el-bethel/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Text and sizing fixed.")
