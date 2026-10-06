with open("alo-agua/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Substituir logomark.png no header pelo novo logo conceito 1
old_header_brand = """            <a href="#" class="brand-link">
                <img src="logomark.png" alt="Mascote Alô Água e Gás" class="brand-logo">
                <div class="brand-text">
                    <span class="brand-name">Alô Água</span>
                    <span class="brand-sub">Água Mineral & Gás</span>
                </div>
            </a>"""

new_header_brand = """            <a href="#" class="brand-link">
                <img src="logo_conceito1.jpg" alt="Novo Logotipo Alô Água" class="brand-logo concept-logo">
            </a>"""

html = html.replace(old_header_brand, new_header_brand)

# No sticky footer bar também
html = html.replace('<img src="logomark.png" alt="Mascote Alô Água" class="sticky-avatar">', '<img src="logo_conceito1.jpg" alt="Novo Logotipo Alô Água" class="sticky-avatar">')

# No footer tradicional
html = html.replace('<img src="logomark.png" alt="Alô Água" class="footer-logo">', '<img src="logo_conceito1.jpg" alt="Alô Água" class="footer-logo">')

with open("alo-agua/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("alo-agua/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Ajustar tamanho do novo logo no header
css += """
.concept-logo {
    width: auto !important;
    height: 60px !important;
    object-fit: contain !important;
    border-radius: 8px;
}
"""

with open("alo-agua/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Logo conceito 1 aplicado no site.")
