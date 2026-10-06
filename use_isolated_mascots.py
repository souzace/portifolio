import shutil

# 1. Copiar os mascotes isolados
shutil.copy("/home/fsouza/.gemini/antigravity-cli/brain/f889fbae-fa01-4f54-81c2-1a2c07cf5799/alo_agua_mascotes_logo_1791303087819.jpg", "alo-agua/mascotes_puros.jpg")

# 2. Atualizar o index.html para voltar o padrão antigo: Imagem dos mascotes + Texto ao lado em HTML
with open("alo-agua/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Substituir o header
old_header = """            <a href="#" class="brand-link">
                <img src="logo_mascote_moderno.jpg" alt="Novo Logotipo Alô Água" class="brand-logo concept-logo">
            </a>"""

new_header = """            <a href="#" class="brand-link">
                <img src="mascotes_puros.jpg" alt="Mascotes Alô Água" class="brand-logo modern-mascot-logo">
                <div class="brand-text">
                    <span class="brand-name">Alô Água</span>
                    <span class="brand-sub">Água Mineral & Gás</span>
                </div>
            </a>"""

html = html.replace(old_header, new_header)

# No sticky footer bar
html = html.replace('src="logo_mascote_moderno.jpg"', 'src="mascotes_puros.jpg"')

with open("alo-agua/index.html", "w", encoding="utf-8") as f:
    f.write(html)

# 3. Ajustar style.css para o novo layout de imagem + texto ao lado
with open("alo-agua/style.css", "r", encoding="utf-8") as f:
    css = f.read()

css += """
.modern-mascot-logo {
    width: auto !important;
    height: 70px !important;
    object-fit: contain !important;
    border-radius: 6px;
}
.brand-name {
    font-size: 1.6rem !important;
    font-weight: 800 !important;
    color: var(--dark-navy) !important;
    line-height: 1 !important;
}
.brand-sub {
    font-size: 0.8rem !important;
    font-weight: 700 !important;
    color: var(--primary-blue) !important;
    letter-spacing: 1px !important;
    margin-top: 3px;
    display: block;
}
"""

with open("alo-agua/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Padrão antigo restaurado com os mascotes novos!")
