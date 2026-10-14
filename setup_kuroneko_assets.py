import shutil

# Copiar o logotipo oficial do Kuro Neko Toys para a pasta do projeto
shutil.copy("/home/fsouza/.gemini/antigravity-cli/brain/f889fbae-fa01-4f54-81c2-1a2c07cf5799/kuro_neko_toys_logo_1791995255331.jpg", "kuroneko-toys/logo_kuroneko.jpg")

# Atualizar o index.html com o logotipo no header e na barra fixa
with open("kuroneko-toys/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Substituir o emoji do avatar no header pela imagem oficial
old_header_brand = """            <a href="#" class="brand-box">
                <div class="brand-avatar-wrap">
                    <span class="cat-emoji">🐱⚡</span>
                </div>
                <div class="brand-titles">
                    <div class="brand-kanji">黒猫玩具</div>
                    <div class="brand-main">KURO NEKO <span class="brand-accent">TOYS</span></div>
                </div>
            </a>"""

new_header_brand = """            <a href="#" class="brand-box">
                <img src="logo_kuroneko.jpg" alt="Kuro Neko Toys" class="brand-img-logo">
            </a>"""

html = html.replace(old_header_brand, new_header_brand)

# Substituir no sticky avatar
html = html.replace('<span class="avatar-cat">🐱✨</span>', '<img src="logo_kuroneko.jpg" alt="Kuro Neko" class="sticky-cat-img">')

with open("kuroneko-toys/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("kuroneko-toys/style.css", "r", encoding="utf-8") as f:
    css = f.read()

css += """
.brand-img-logo {
    height: 64px;
    width: auto;
    border-radius: 12px;
    box-shadow: 0 0 20px rgba(6, 182, 212, 0.3);
}

.sticky-cat-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
}
"""

with open("kuroneko-toys/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Ativos e código da Kuro Neko Toys configurados com sucesso!")
