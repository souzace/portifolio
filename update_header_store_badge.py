with open("kuroneko-toys/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Substituir o bloco do header antigo pelo novo layout:
# - Mantém a marca à esquerda
# - Mantém os links de navegação se desejar, mas o usuário pediu para remover a barra superior de localização e whatsapp button
# - À direita, no lugar do badge de localização e botão de WhatsApp, colocar o selo retrô em caixa "STORE" exatamente como no card vertical!

old_header = """    <!-- Header Flutuante / Cyberpunk Nav -->
    <header class="cyber-header">
        <div class="container header-content">
                        <a href="#" class="brand-box">
                <img src="official_avatar_fb.jpg?v=1792001850" alt="Kuro Neko Toys" class="brand-avatar-circle">
                <div class="brand-titles">
                    <div class="brand-kanji">黒猫玩具</div>
                    <div class="brand-main">KURO <span class="brand-neko">NEKO</span> <span class="brand-toys">TOYS</span></div>
                </div>
            </a>
            
            <nav class="nav-links">
                <a href="#destaques" class="nav-item">Action Figures</a>
                <a href="#universos" class="nav-item">Universos</a>
                <a href="#feiras" class="nav-item">Onde Estamos</a>
            </nav>

            <div class="header-actions">
                <span class="loc-badge">📍 Fortaleza / CE</span>
                <a href="https://wa.me/558592828087?text=Ol%C3%A1%20Kuro%20Neko!%20Vim%20pelo%20site%20e%20quero%20conferir%20o%20cat%C3%A1logo%20de%20colecion%C3%A1veis." target="_blank" class="btn-neon-wa">
                    <span>Chamar no Zap</span>
                </a>
            </div>
        </div>
    </header>"""

new_header = """    <!-- Header Flutuante / Cyberpunk Nav -->
    <header class="cyber-header">
        <div class="container header-content">
            <a href="#" class="brand-box">
                <img src="official_avatar_fb.jpg?v=1792001850" alt="Kuro Neko Toys" class="brand-avatar-circle">
                <div class="brand-titles">
                    <div class="brand-kanji">黒猫玩具</div>
                    <div class="brand-main">KURO <span class="brand-neko">NEKO</span> <span class="brand-toys">TOYS</span></div>
                </div>
            </a>
            
            <nav class="nav-links">
                <a href="#destaques" class="nav-item">Action Figures</a>
                <a href="#universos" class="nav-item">Universos</a>
                <a href="#feiras" class="nav-item">Onde Estamos</a>
            </nav>

            <div class="header-right-store">
                <div class="store-comic-badge">STORE</div>
            </div>
        </div>
    </header>"""

html = html.replace(old_header, new_header)

with open("kuroneko-toys/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("kuroneko-toys/style.css", "r", encoding="utf-8") as f:
    css = f.read()

css += """
/* Selo Retrô STORE no canto superior direito do Header */
.header-right-store {
    display: flex;
    align-items: center;
}

.store-comic-badge {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.15rem;
    font-weight: 900;
    letter-spacing: 3px;
    color: #12141F;
    background-color: #F8FAFC;
    border: 3px solid #1E293B;
    border-radius: 8px;
    padding: 0.35rem 1.4rem;
    box-shadow: 3px 3px 0px var(--kuro-orange);
    text-transform: uppercase;
    transition: transform 0.2s, box-shadow 0.2s;
    user-select: none;
}

.store-comic-badge:hover {
    transform: translate(-2px, -2px);
    box-shadow: 5px 5px 0px var(--kuro-orange);
}

@media (max-width: 768px) {
    .store-comic-badge {
        font-size: 0.95rem;
        padding: 0.25rem 0.9rem;
        letter-spacing: 2px;
    }
}
"""

with open("kuroneko-toys/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Header atualizado com a remoção de localização/zap e adição da placa STORE!")
