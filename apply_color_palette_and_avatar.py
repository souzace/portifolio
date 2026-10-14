# 1. Atualizar o index.html:
# - No Header: Usar official_avatar_fb.jpg como logomarca oficial redonda com nome ao lado
with open("kuroneko-toys/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Substituir o header brand pelo avatar oficial do Instagram com o lettering limpo
old_brand = """            <a href="#" class="brand-box">
                <img src="logo_kuroneko.jpg" alt="Kuro Neko Toys" class="brand-img-logo">
            </a>"""

new_brand = """            <a href="#" class="brand-box">
                <img src="official_avatar_fb.jpg" alt="Kuro Neko Toys" class="brand-official-avatar">
                <div class="brand-titles">
                    <div class="brand-kanji">黒猫玩具</div>
                    <div class="brand-main">KURO <span class="brand-neko">NEKO</span> <span class="brand-toys">TOYS</span></div>
                </div>
            </a>"""

html = html.replace(old_brand, new_brand)

with open("kuroneko-toys/index.html", "w", encoding="utf-8") as f:
    f.write(html)

# 2. Atualizar o style.css:
# - Trocar o roxo pelo LARANJA do KURO (#F97316 / #EA580C)
# - Adicionar o VERMELHO do NEKO (#EF4444 / #DC2626)
# - Linhas horizontais e detalhes no AZUL OCEANO do TOYS (#0284C7 / #0EA5E9)
# - Dar ZOOM no avatar da barra fixa focando na carinha do gato e no telefone
with open("kuroneko-toys/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Substituir a paleta
css = css.replace("""    --cyber-blue: #0EA5E9; /* Azul ciano elétrico brilhante */
    --cyber-blue-glow: rgba(14, 165, 233, 0.45);
    --blue-neon: #2563EB;
    --purple-neon: #8B5CF6;
    --purple-glow: rgba(139, 92, 246, 0.35);
    --yellow-neon: #FACC15;
    --yellow-glow: rgba(250, 204, 21, 0.35);""", """    --kuro-orange: #F97316; /* Laranja oficial KURO */
    --kuro-orange-glow: rgba(249, 115, 22, 0.45);
    --neko-red: #EF4444; /* Vermelho oficial NEKO */
    --neko-red-glow: rgba(239, 68, 68, 0.45);
    --toys-ocean-blue: #0284C7; /* Azul Oceano oficial TOYS */
    --toys-ocean-glow: rgba(2, 132, 199, 0.45);
    --yellow-neon: #FBBF24;
    --yellow-glow: rgba(251, 191, 36, 0.35);""")

# Ajustar os gradientes e botões que eram roxos para Laranja KURO
css = css.replace('var(--purple-neon)', 'var(--kuro-orange)')
css = css.replace('var(--purple-glow)', 'var(--kuro-orange-glow)')
css = css.replace('#C084FC', 'var(--kuro-orange)')
css = css.replace('rgba(147, 51, 234', 'rgba(249, 115, 22')
css = css.replace('rgba(139, 92, 246', 'rgba(249, 115, 22')

# Linhas horizontais (borders) em Azul Oceano TOYS
css = css.replace('--border-color: rgba(14, 165, 233, 0.15);', '--border-color: rgba(2, 132, 199, 0.25); /* Linhas horizontais Azul Oceano */')
css = css.replace('border-top: 1px solid var(--border-color);', 'border-top: 1px solid var(--toys-ocean-blue);')

# Destaques em Vermelho NEKO
css = css.replace('.neon-text-purple {', '.neon-text-purple {\n    color: var(--kuro-orange) !important;\n    text-shadow: 0 0 20px var(--kuro-orange-glow) !important;\n}')
css = css.replace('.hero-pill {', '.hero-pill {\n    background-color: rgba(239, 68, 68, 0.12) !important;\n    border: 1px solid var(--neko-red) !important;\n    color: #FCA5A5 !important;')
css = css.replace('.pulse-dot {', '.pulse-dot {\n    background-color: var(--neko-red) !important;\n    box-shadow: 0 0 10px var(--neko-red) !important;')

# Adicionar regras específicas para o logo oficial e zoom no avatar sticky
css += """
/* Logomarca Oficial do Instagram no Header */
.brand-official-avatar {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid var(--kuro-orange);
    box-shadow: 0 0 15px var(--kuro-orange-glow);
}
.brand-main {
    font-size: 1.35rem;
    font-weight: 900;
    color: var(--kuro-orange);
    letter-spacing: 1px;
}
.brand-neko {
    color: var(--neko-red);
    text-shadow: 0 0 10px var(--neko-red-glow);
}
.brand-toys {
    color: var(--toys-ocean-blue);
    text-shadow: 0 0 10px var(--toys-ocean-glow);
}

/* ZOOM no Avatar da Barra Fixa Flutuante (Foco na Carinha do Gato e Telefone) */
.sticky-avatar-wrap {
    width: 56px !important;
    height: 56px !important;
    overflow: hidden !important;
    position: relative !important;
    border: 2px solid var(--kuro-orange) !important;
    box-shadow: 0 0 15px var(--kuro-orange-glow) !important;
    background: #0D0F1A !important;
}

.sticky-cat-img {
    width: 250% !important;
    height: 250% !important;
    object-fit: cover !important;
    position: absolute !important;
    top: -125% !important;
    left: -75% !important;
    border-radius: 0 !important;
}

/* Linha da barra fixa em Azul Oceano TOYS */
.sticky-footer-bar {
    border-top: 2px solid var(--toys-ocean-blue) !important;
    box-shadow: 0 -10px 30px rgba(2, 132, 199, 0.3) !important;
}
"""

with open("kuroneko-toys/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Todas as cores da tríade oficial (Laranja KURO, Vermelho NEKO, Azul Oceano TOYS) e Zoom no Avatar aplicados!")
