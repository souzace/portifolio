# 1. Ajustar index.html: No header colocar a foto de perfil oficial com o texto Kuro Neko Toys
with open("kuroneko-toys/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# No header, usar a official_avatar_fb.jpg com proporção redonda elegante e o texto ao lado
header_brand_old = """            <a href="#" class="brand-box">
                <img src="official_avatar_fb.jpg" alt="Kuro Neko Toys" class="brand-official-avatar">
                <div class="brand-titles">
                    <div class="brand-kanji">黒猫玩具</div>
                    <div class="brand-main">KURO <span class="brand-neko">NEKO</span> <span class="brand-toys">TOYS</span></div>
                </div>
            </a>"""

# Na imagem do usuário vemos que o header ficou com um card vertical minúsculo porque pegou official_store_cat.jpg em vez do avatar
# Vamos garantir que está o avatar oficial redondo com tamanho ideal
header_brand_new = """            <a href="#" class="brand-box">
                <img src="official_avatar_fb.jpg" alt="Kuro Neko Toys" class="brand-avatar-circle">
                <div class="brand-titles">
                    <div class="brand-kanji">黒猫玩具</div>
                    <div class="brand-main">KURO <span class="brand-neko">NEKO</span> <span class="brand-toys">TOYS</span></div>
                </div>
            </a>"""

# Se o header tiver img src="official_store_cat.jpg" ou similar, substitui
import re
html = re.sub(r'<a href="#" class="brand-box">.*?</a>', header_brand_new, html, flags=re.DOTALL)

with open("kuroneko-toys/index.html", "w", encoding="utf-8") as f:
    f.write(html)

# 2. Ajustar style.css:
# - .brand-avatar-circle: redondo, 52px por 52px, borda laranja
# - .sticky-avatar-wrap e .sticky-cat-img:
#   Na imagem do usuário, o círculo da barra fixa está mostrando o pé do balcão e as patinhas, mas não a carinha do gato e o telefone!
#   Precisamos mirar o crop EXATAMENTE no terço superior do card (onde estão a cabeça do gato, os olhões amarelos e o fone preto)!
with open("kuroneko-toys/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Substituir o bloco do sticky zoom
old_zoom = """.sticky-cat-img {
    width: 250% !important;
    height: 250% !important;
    object-fit: cover !important;
    position: absolute !important;
    top: -125% !important;
    left: -75% !important;
    border-radius: 0 !important;
}"""

new_zoom = """.brand-avatar-circle {
    width: 50px !important;
    height: 50px !important;
    border-radius: 50% !important;
    object-fit: cover !important;
    border: 2px solid var(--kuro-orange) !important;
    box-shadow: 0 0 15px var(--kuro-orange-glow) !important;
    flex-shrink: 0;
}

.sticky-avatar-wrap {
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

css = css.replace(old_zoom, new_zoom)

with open("kuroneko-toys/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Ajuste de enquadramento do avatar e do logo concluído!")
