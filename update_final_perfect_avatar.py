# 1. No index.html: No sticky footer usar a imagem recortada exata da carinha do gato com o fone!
with open("kuroneko-toys/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Substituir o sticky avatar
html = html.replace('src="official_store_cat.jpg"', 'src="cat_head_phone.jpg"')

with open("kuroneko-toys/index.html", "w", encoding="utf-8") as f:
    f.write(html)

# 2. No style.css: Ajustar para a imagem ficar perfeitamente enquadrada e redondinha
with open("kuroneko-toys/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Substituir regras do sticky avatar
old_sticky = """.sticky-avatar-wrap {
    width: 56px !important;
    height: 56px !important;
    border-radius: 50% !important;
    overflow: hidden !important;
    position: relative !important;
    border: 2px solid var(--kuro-orange) !important;
    box-shadow: 0 0 15px var(--kuro-orange-glow) !important;
    background: #11131F !important;
    flex-shrink: 0;
}

/* Enquadramento perfeito na cabeça do gato e fone de telefone */
.sticky-cat-img {
    width: 320% !important;
    height: auto !important;
    max-width: none !important;
    position: absolute !important;
    top: -160px !important;
    left: -65px !important;
    border-radius: 0 !important;
    display: block !important;
}"""

new_sticky = """.sticky-avatar-wrap {
    width: 56px !important;
    height: 56px !important;
    border-radius: 50% !important;
    overflow: hidden !important;
    border: 2px solid var(--kuro-orange) !important;
    box-shadow: 0 0 15px var(--kuro-orange-glow) !important;
    background: #11131F !important;
    flex-shrink: 0;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

.sticky-cat-img {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    object-position: center !important;
    border-radius: 50% !important;
    display: block !important;
}"""

css = css.replace(old_sticky, new_sticky)

with open("kuroneko-toys/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Avatar da barra fixa e cabeçalho perfeitamente afinados!")
