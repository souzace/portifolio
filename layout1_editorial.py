import re

with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. New Header & Hero (Editorial Style)
new_hero = """    <!-- Header Minimalista -->
    <nav class="nav-minimal">
        <div class="container nav-content">
            <a href="#vitrine" class="nav-link-dark">Especialidades</a>
            <a href="#historia" class="nav-link-dark">Nossa Arte</a>
            <a href="#contato" class="btn-outline-dark">Visite-nos</a>
        </div>
    </nav>

    <!-- Título Editorial (Logo) -->
    <section class="editorial-title">
        <img src="logomark.jpg" alt="Empório Linneo" class="logo-editorial">
    </section>

    <!-- Hero Editorial (Split) -->
    <section class="hero-editorial">
        <div class="container hero-split">
            <div class="hero-text-side">
                <h1>O aroma fresco da tradição,<br>todos os dias.</h1>
                <p>Pães de fermentação natural, doces artesanais e aquele café perfeito para acompanhar o seu momento.</p>
                <a href="#vitrine" class="btn-editorial">Explorar o Cardápio</a>
            </div>
            <div class="hero-img-side">
                <img src="hero_bakery.jpg" alt="Pães e Café" class="hero-photo">
            </div>
        </div>
    </section>"""

html = re.sub(r'<!-- Header -->.*?</section>', new_hero, html, flags=re.DOTALL)

# 2. New Vitrine (Zigzag/Asymmetrical)
new_vitrine = """    <!-- Vitrine Editorial (ZigZag) -->
    <section id="vitrine" class="vitrine-editorial">
        <div class="container">
            <h2 class="section-title-dark">Nossas Especialidades</h2>
            
            <div class="zigzag-row">
                <div class="zz-img" style="background-image: url('product1.jpg');"></div>
                <div class="zz-text">
                    <h3>Pães Artesanais</h3>
                    <p>Fermentação natural de 48h, crosta rústica e miolo macio. O verdadeiro sabor do trigo resgatado do tempo.</p>
                </div>
            </div>
            
            <div class="zigzag-row reverse">
                <div class="zz-img" style="background-image: url('product2.jpg');"></div>
                <div class="zz-text">
                    <h3>Confeitaria Fina</h3>
                    <p>Eclairs, tarteletes e bolos afetivos feitos com chocolate belga e frutas frescas rigorosamente selecionadas.</p>
                </div>
            </div>

            <div class="zigzag-row">
                <div class="zz-img" style="background-image: url('product3.jpg');"></div>
                <div class="zz-text">
                    <h3>Cafés Especiais</h3>
                    <p>Grãos de torra clara e média, extraídos com perfeição para realçar as notas sensoriais em cada xícara.</p>
                </div>
            </div>

            <div class="zigzag-row reverse">
                <div class="zz-img" style="background-image: url('product4.jpg');"></div>
                <div class="zz-text">
                    <h3>Frios e Antepastos</h3>
                    <p>Uma curadoria impecável de queijos curados, charcutaria artesanal e geleias para compartilhar.</p>
                </div>
            </div>
        </div>
    </section>"""

html = re.sub(r'<!-- Vitrine de Produtos -->.*?</section>', new_vitrine, html, flags=re.DOTALL)

with open("emporio-linneo/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Completely replace the CSS from /* Header */ downwards to apply Editorial styles
css_base = css[:css.find("/* Header */")]

new_css = """/* Header Minimalista */
.nav-minimal {
    padding: 2rem 0;
    background-color: var(--bg-light);
}
.nav-content {
    display: flex;
    justify-content: center;
    gap: 3rem;
    align-items: center;
}
.nav-link-dark {
    text-decoration: none;
    color: var(--text-dark);
    font-weight: 400;
    font-size: 0.9rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    transition: color 0.3s ease;
}
.nav-link-dark:hover { color: var(--primary); }
.btn-outline-dark {
    border: 1px solid var(--text-dark);
    padding: 0.5rem 1.5rem;
    text-decoration: none;
    color: var(--text-dark);
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.btn-outline-dark:hover {
    background-color: var(--text-dark);
    color: var(--bg-light);
}

/* Título Editorial */
.editorial-title {
    text-align: center;
    background-color: var(--bg-light);
    padding: 2rem 0 4rem;
}
.logo-editorial {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    object-fit: cover;
    border: 1px solid var(--primary);
}

/* Hero Editorial */
.hero-editorial {
    background-color: var(--bg-light);
    padding-bottom: 6rem;
}
.hero-split {
    display: flex;
    align-items: center;
    gap: 4rem;
}
.hero-text-side {
    flex: 1;
}
.hero-text-side h1 {
    font-size: 4rem;
    line-height: 1.1;
    color: var(--text-dark);
    margin-bottom: 1.5rem;
}
.hero-text-side p {
    font-size: 1.1rem;
    color: var(--text-muted);
    margin-bottom: 2.5rem;
    max-width: 400px;
}
.btn-editorial {
    display: inline-block;
    padding: 1rem 2rem;
    background-color: var(--primary);
    color: var(--bg-light);
    text-decoration: none;
    font-weight: 400;
    letter-spacing: 1px;
    text-transform: uppercase;
    font-size: 0.85rem;
}
.hero-img-side {
    flex: 1;
}
.hero-photo {
    width: 100%;
    height: 600px;
    object-fit: cover;
    border-radius: 2px;
}

/* Vitrine ZigZag */
.vitrine-editorial {
    padding: 6rem 0;
    background-color: #fff;
}
.section-title-dark {
    text-align: center;
    font-size: 2.5rem;
    color: var(--text-dark);
    font-family: 'Lora', serif;
    margin-bottom: 5rem;
}
.zigzag-row {
    display: flex;
    align-items: center;
    gap: 4rem;
    margin-bottom: 6rem;
}
.zigzag-row.reverse {
    flex-direction: row-reverse;
}
.zz-img {
    flex: 1;
    height: 400px;
    background-size: cover;
    background-position: center;
}
.zz-text {
    flex: 1;
    padding: 0 2rem;
}
.zz-text h3 {
    font-size: 2rem;
    color: var(--text-dark);
    margin-bottom: 1rem;
}
.zz-text p {
    color: var(--text-muted);
    font-size: 1.1rem;
    line-height: 1.8;
}

/* Historia e Footer herdados, mas ajustados para o fundo claro */
.historia {
    padding: 8rem 0;
    background-color: var(--bg-light);
    color: var(--text-dark);
}
.historia-wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
}
.historia h2 {
    color: var(--text-dark);
    font-size: 3rem;
    margin-bottom: 1.5rem;
}
.historia p {
    color: var(--text-muted);
    font-size: 1.1rem;
    margin-bottom: 1rem;
}
.historia-img {
    height: 500px;
    background: url('working.webp') no-repeat center center/cover;
}

.footer {
    background-color: var(--bg-dark);
    color: var(--bg-light);
    padding: 4rem 0 1rem;
}
.footer-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 3rem;
    margin-bottom: 3rem;
}
.logo-img-footer {
    height: 80px;
    border-radius: 50%;
    margin-bottom: 1rem;
    border: 2px solid var(--primary);
}
.footer-contact h3 {
    color: var(--primary);
    margin-bottom: 1rem;
    font-size: 1.2rem;
}
.footer-contact p {
    margin-bottom: 0.5rem;
    color: rgba(249, 243, 233, 0.8);
}
.footer-bottom {
    text-align: center;
    border-top: 1px solid rgba(212, 175, 55, 0.2);
    padding-top: 1.5rem;
    font-size: 0.85rem;
    color: rgba(249, 243, 233, 0.5);
}

/* FAB */
.fab-whatsapp {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    background-color: #25D366;
    color: #fff;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
    z-index: 1000;
    transition: transform 0.3s ease;
}
.fab-whatsapp svg { width: 35px; height: 35px; }
.fab-whatsapp:hover { transform: scale(1.1); }

/* Responsividade Editorial */
@media (max-width: 768px) {
    .nav-content { flex-direction: column; gap: 1rem; }
    .hero-split { flex-direction: column; gap: 2rem; text-align: center; }
    .hero-text-side p { margin: 0 auto 2rem; }
    .hero-text-side h1 { font-size: 2.5rem; }
    .hero-photo { height: 300px; }
    .zigzag-row, .zigzag-row.reverse { flex-direction: column; gap: 2rem; text-align: center; margin-bottom: 4rem;}
    .zz-img { width: 100%; height: 250px; }
    .historia-wrapper { grid-template-columns: 1fr; text-align: center; }
    .historia-img { height: 300px; order: -1; }
}
"""

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css_base + new_css)

print("Editorial Layout applied.")
