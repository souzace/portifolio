import shutil

# Copiar a ilustração da loja oficial limpa
shutil.copy("/home/fsouza/.gemini/antigravity-cli/brain/f889fbae-fa01-4f54-81c2-1a2c07cf5799/kuro_neko_toys_store_official_1791999778376.jpg", "kuroneko-toys/official_store_cat.jpg")

with open("kuroneko-toys/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Integrar na Hero Section: Layout 2 colunas com a arte da loja e o gato atendente em destaque
old_hero = """    <!-- Hero Section: Akihabara Night Market -->
    <section class="hero-section">
        <div class="hero-glow-bg"></div>
        <div class="container hero-container">
            <div class="hero-pill">
                <span class="pulse-dot"></span>
                <span>Direto de Akihabara para Fortaleza • Envios para todo o Brasil</span>
            </div>
            
            <h1 class="hero-headline">
                O Santuário dos <span class="neon-text-purple">Colecionadores</span> e Fãs de <span class="neon-text-yellow">Animes</span>.
            </h1>
            
            <p class="hero-desc">
                Action figures originais, estátuas detalhadas, colecionáveis raros e aquele garimpo geek que você só encontra na Kuro Neko Toys. De fã para fã, com pronta entrega em Fortaleza.
            </p>

            <div class="hero-cta-group">
                <a href="#destaques" class="btn-primary-glow">
                    <span>Explorar Drops do Mês</span>
                    <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </a>
                <a href="https://wa.me/558592828087?text=Ol%C3%A1!%20Gostaria%20de%20saber%20se%20voc%C3%AAs%20t%C3%AAm%20uma%20action%20figure%20espec%C3%ADfica." target="_blank" class="btn-secondary-neon">
                    <span>Pedir Peça sob Encomenda</span>
                </a>
            </div>

            <!-- Badges de Confiança Geek -->
            <div class="hero-badges-row">
                <div class="trust-badge">
                    <span class="tb-icon">🛡️</span>
                    <div class="tb-text">
                        <strong>100% Autênticos</strong>
                        <small>Peças lacradas e revisadas</small>
                    </div>
                </div>
                <div class="trust-badge">
                    <span class="tb-icon">📦</span>
                    <div class="tb-text">
                        <strong>Embalagem Blindada</strong>
                        <small>Caixas protegidas com plástico bolha</small>
                    </div>
                </div>
                <div class="trust-badge">
                    <span class="tb-icon">⚡</span>
                    <div class="tb-text">
                        <strong>Pronta Entrega</strong>
                        <small>Retirada no Mondubim ou motoboy</small>
                    </div>
                </div>
            </div>
        </div>
    </section>"""

new_hero = """    <!-- Hero Section: O Balcão Oficial do Kuro Neko -->
    <section class="hero-section">
        <div class="hero-glow-bg"></div>
        <div class="container hero-split-grid">
            <div class="hero-left-content">
                <div class="hero-pill">
                    <span class="pulse-dot"></span>
                    <span>Sua loja Geek em Fortaleza • Envios para todo o Brasil</span>
                </div>
                
                <h1 class="hero-headline">
                    O Santuário dos <span class="neon-text-purple">Colecionadores</span> e Fãs de <span class="neon-text-yellow">Animes</span>.
                </h1>
                
                <p class="hero-desc">
                    Action figures originais, estátuas detalhadas, colecionáveis raros e aquele garimpo geek que você só encontra aqui. O Kuro Neko está pronto no balcão para atender o seu pedido!
                </p>

                <div class="hero-cta-group">
                    <a href="#destaques" class="btn-primary-glow">
                        <span>Explorar Drops do Mês</span>
                        <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                    </a>
                    <a href="https://wa.me/558592828087?text=Ol%C3%A1%20Kuro%20Neko!%20Gostaria%20de%20saber%20se%20voc%C3%AAs%20t%C3%AAm%20uma%20action%20figure%20espec%C3%ADfica." target="_blank" class="btn-secondary-neon">
                        <span>Falar no Balcão (WhatsApp)</span>
                    </a>
                </div>

                <!-- Badges de Confiança Geek -->
                <div class="hero-badges-row">
                    <div class="trust-badge">
                        <span class="tb-icon">🛡️</span>
                        <div class="tb-text">
                            <strong>100% Autênticos</strong>
                            <small>Peças lacradas e revisadas</small>
                        </div>
                    </div>
                    <div class="trust-badge">
                        <span class="tb-icon">📦</span>
                        <div class="tb-text">
                            <strong>Embalagem Blindada</strong>
                            <small>Caixas super protegidas</small>
                        </div>
                    </div>
                    <div class="trust-badge">
                        <span class="tb-icon">⚡</span>
                        <div class="tb-text">
                            <strong>Pronta Entrega</strong>
                            <small>Mondubim, feiras ou motoboy</small>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Coluna da Direita: A Arte Oficial da Loja com o Gato no Balcão -->
            <div class="hero-right-visual">
                <div class="cat-poster-frame">
                    <img src="official_store_cat.jpg" alt="Kuro Neko Toys Store Oficial" class="cat-official-art">
                    <div class="cat-poster-badge">
                        <span class="badge-status-dot"></span>
                        <span>Balcão Aberto • Atendimento Online</span>
                    </div>
                </div>
            </div>
        </div>
    </section>"""

html = html.replace(old_hero, new_hero)

# 2. Atualizar o avatar do sticky footer para usar o gatinho oficial
html = html.replace('src="logo_kuroneko.jpg"', 'src="official_store_cat.jpg"')

with open("kuroneko-toys/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("kuroneko-toys/style.css", "r", encoding="utf-8") as f:
    css = f.read()

css += """
/* Layout 2 Colunas da Hero com o Gato no Balcão */
.hero-split-grid {
    display: grid;
    grid-template-columns: 1.2fr 0.9fr;
    gap: 3.5rem;
    align-items: center;
    position: relative;
    z-index: 2;
    text-align: left;
}

.hero-left-content {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.hero-desc {
    margin: 0 0 2rem 0;
}

.hero-cta-group {
    justify-content: flex-start;
    margin-bottom: 2.5rem;
}

.hero-badges-row {
    width: 100%;
}

.hero-right-visual {
    display: flex;
    justify-content: center;
    align-items: center;
}

.cat-poster-frame {
    position: relative;
    border-radius: 24px;
    overflow: hidden;
    border: 2px solid var(--cyber-blue);
    box-shadow: 0 0 40px rgba(14, 165, 233, 0.3), 0 20px 40px rgba(0, 0, 0, 0.6);
    background: #000;
    max-width: 420px;
    transition: transform 0.3s, box-shadow 0.3s;
}

.cat-poster-frame:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 0 50px rgba(139, 92, 246, 0.5), 0 25px 50px rgba(0, 0, 0, 0.8);
    border-color: var(--purple-neon);
}

.cat-official-art {
    width: 100%;
    height: auto;
    display: block;
    object-fit: cover;
}

.cat-poster-badge {
    position: absolute;
    bottom: 1.2rem;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(6, 9, 19, 0.85);
    backdrop-filter: blur(8px);
    border: 1px solid var(--border-blue);
    padding: 0.5rem 1.2rem;
    border-radius: 50px;
    font-size: 0.8rem;
    font-weight: 700;
    color: #fff;
    white-space: nowrap;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
}

.badge-status-dot {
    width: 8px;
    height: 8px;
    background: var(--wa-green);
    border-radius: 50%;
    box-shadow: 0 0 8px var(--wa-green);
}

@media (max-width: 992px) {
    .hero-split-grid {
        grid-template-columns: 1fr;
        text-align: center;
        gap: 2.5rem;
    }
    .hero-left-content {
        align-items: center;
    }
    .hero-cta-group {
        justify-content: center;
    }
    .cat-poster-frame {
        max-width: 340px;
    }
}
"""

with open("kuroneko-toys/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Gato oficial integrado com maestria na Hero e na barra fixa!")
