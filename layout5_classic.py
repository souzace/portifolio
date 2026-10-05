import re

with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

new_body = """<body>

    <!-- Classic Centered Split Header -->
    <header class="classic-header">
        <div class="container classic-nav-container">
            <nav class="nav-side left">
                <a href="#cardapio">Cardápio</a>
                <a href="#historia">Nossa Arte</a>
            </nav>
            <div class="nav-center">
                <img src="logomark.jpg" alt="Logo Empório Linneo" class="logo-classic">
            </div>
            <nav class="nav-side right">
                <a href="https://wa.me/5585999362255">Fazer Pedido</a>
                <a href="#contato">Localização</a>
            </nav>
        </div>
    </header>

    <!-- Classic Elegant Hero -->
    <section class="classic-hero">
        <div class="classic-hero-bg" style="background-image: url('hero_bakery.jpg');"></div>
        <div class="classic-hero-content">
            <div class="hero-frame">
                <h1>O aroma fresco da tradição.</h1>
                <p>Pães de fermentação natural e doces artesanais.</p>
                <a href="#cardapio" class="btn-classic">Conhecer o Menu</a>
            </div>
        </div>
    </section>

    <!-- Arched Vitrine (Luxury Style) -->
    <section id="cardapio" class="classic-vitrine">
        <div class="container">
            <div class="title-wrapper">
                <span class="subtitle">Descubra Nossas</span>
                <h2 class="section-title-classic">Especialidades</h2>
            </div>
            
            <div class="arch-grid">
                
                <div class="arch-card">
                    <div class="arch-img" style="background-image: url('product1.jpg');"></div>
                    <div class="arch-text">
                        <h3>Pães Rústicos</h3>
                        <p>Fermentação lenta, crosta perfeita e miolo macio.</p>
                    </div>
                </div>

                <div class="arch-card">
                    <div class="arch-img" style="background-image: url('product2.jpg');"></div>
                    <div class="arch-text">
                        <h3>Confeitaria</h3>
                        <p>A arte francesa aplicada aos doces mais afetivos.</p>
                    </div>
                </div>

                <div class="arch-card">
                    <div class="arch-img" style="background-image: url('product3.jpg');"></div>
                    <div class="arch-text">
                        <h3>Cafés</h3>
                        <p>Grãos de altitude, torrados com maestria.</p>
                    </div>
                </div>

                <div class="arch-card">
                    <div class="arch-img" style="background-image: url('product4.jpg');"></div>
                    <div class="arch-text">
                        <h3>Frios</h3>
                        <p>Acompanhamentos curados para celebrar o momento.</p>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Classic Historia Split -->
    <section id="historia" class="classic-historia">
        <div class="container historia-flex">
            <div class="historia-image-arch" style="background-image: url('working.webp');"></div>
            <div class="historia-content-centered">
                <span class="subtitle">Nossa Essência</span>
                <h2>A Arte do Tempo</h2>
                <div class="divider"></div>
                <p>No Empório Linneo, acreditamos que a boa comida não aceita atalhos. Nossa padaria nasceu do desejo de resgatar as receitas lentas e honestas.</p>
                <p>Nossos padeiros chegam antes do sol nascer para garantir que o croissant esteja na temperatura perfeita quando você entrar pela nossa porta.</p>
            </div>
        </div>
    </section>

    <!-- Formal Footer -->
    <footer id="contato" class="classic-footer">
        <div class="container">
            <img src="logomark.jpg" alt="Logo" class="footer-logo-classic">
            <div class="footer-contact-info">
                <p>📍 Av. Lineu Machado, 875 - Jóquei Clube, Fortaleza - CE</p>
                <p>🕒 Aberto todos os dias das 06h às 21h</p>
                <p>📞 WhatsApp: (85) 99936-2255</p>
            </div>
            <p class="copyright">&copy; 2026 Empório Linneo. Tradição & Sabor.</p>
        </div>
    </footer>

    <!-- FAB -->
    <a href="https://wa.me/5585999362255" class="fab-whatsapp" target="_blank" aria-label="Pedir no WhatsApp">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824zm-3.423-14.416c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm.029 18.88c-1.161 0-2.305-.292-3.318-.844l-3.677.964.984-3.595c-.607-1.052-.927-2.246-.926-3.468.001-5.824 4.74-10.563 10.564-10.563 5.826 0 10.564 4.741 10.564 10.564 0 5.825-4.739 10.564-10.564 10.564z"/></svg>
    </a>
</body>"""

html = re.sub(r'<body>.*?</body>', new_body, html, flags=re.DOTALL)

with open("emporio-linneo/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

css_base = css[:css.find("/* Masonry Header */")]

new_css = """/* Classic Header */
.classic-header {
    background-color: var(--bg-dark);
    padding: 1.5rem 0;
    border-bottom: 3px solid var(--primary);
}
.classic-nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.nav-side {
    flex: 1;
    display: flex;
    gap: 3rem;
}
.nav-side.left { justify-content: flex-end; }
.nav-side.right { justify-content: flex-start; }
.nav-side a {
    color: var(--primary);
    text-decoration: none;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 0.9rem;
    font-family: 'Outfit', sans-serif;
    transition: color 0.3s;
}
.nav-side a:hover { color: var(--bg-light); }
.nav-center {
    padding: 0 4rem;
}
.logo-classic {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    border: 2px solid var(--primary);
}

/* Classic Hero */
.classic-hero {
    position: relative;
    height: 80vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}
.classic-hero-bg {
    position: absolute;
    top:0; left:0; width:100%; height:100%;
    background-size: cover;
    background-position: center;
}
.classic-hero-bg::after {
    content: '';
    position: absolute;
    top:0; left:0; width:100%; height:100%;
    background: rgba(53, 28, 21, 0.7);
}
.classic-hero-content {
    position: relative;
    z-index: 2;
    padding: 3rem 4rem;
    border: 1px solid var(--primary);
    background-color: rgba(53, 28, 21, 0.4);
    backdrop-filter: blur(5px);
}
.hero-frame h1 {
    color: var(--primary);
    font-size: 3.5rem;
    font-family: 'Lora', serif;
    margin-bottom: 1rem;
}
.hero-frame p {
    color: var(--bg-light);
    font-size: 1.2rem;
    margin-bottom: 2rem;
    font-style: italic;
    font-family: 'Lora', serif;
}
.btn-classic {
    display: inline-block;
    padding: 0.8rem 2.5rem;
    background-color: var(--primary);
    color: var(--bg-dark);
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 600;
    text-decoration: none;
    transition: background 0.3s;
}
.btn-classic:hover { background-color: var(--bg-light); }

/* Classic Vitrine (Arches) */
.classic-vitrine {
    padding: 8rem 0;
    background-color: var(--bg-light);
    text-align: center;
}
.title-wrapper { margin-bottom: 5rem; }
.subtitle {
    display: block;
    color: var(--primary);
    text-transform: uppercase;
    letter-spacing: 4px;
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
}
.section-title-classic {
    font-size: 3rem;
    color: var(--bg-dark);
    font-family: 'Lora', serif;
}
.arch-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 3rem;
}
.arch-card {
    text-align: center;
}
.arch-img {
    height: 350px;
    border-radius: 200px 200px 0 0;
    background-size: cover;
    background-position: center;
    margin-bottom: 1.5rem;
    border: 1px solid rgba(53, 28, 21, 0.1);
    box-shadow: 0 10px 20px rgba(53, 28, 21, 0.05);
}
.arch-text h3 {
    font-family: 'Lora', serif;
    font-size: 1.5rem;
    color: var(--bg-dark);
    margin-bottom: 0.5rem;
}
.arch-text p {
    color: var(--text-muted);
    font-size: 0.95rem;
}

/* Classic Historia */
.classic-historia {
    background-color: var(--bg-dark);
    padding: 8rem 0;
    color: var(--bg-light);
}
.historia-flex {
    display: flex;
    align-items: center;
    gap: 5rem;
}
.historia-image-arch {
    flex: 1;
    height: 500px;
    border-radius: 250px 250px 0 0;
    background-size: cover;
    background-position: center;
    border: 2px solid var(--primary);
}
.historia-content-centered {
    flex: 1;
    text-align: center;
    padding: 0 2rem;
}
.historia-content-centered h2 {
    font-size: 3rem;
    font-family: 'Lora', serif;
    color: var(--primary);
}
.divider {
    width: 50px;
    height: 2px;
    background-color: var(--primary);
    margin: 2rem auto;
}
.historia-content-centered p {
    font-size: 1.1rem;
    color: rgba(249, 243, 233, 0.8);
    margin-bottom: 1.5rem;
    line-height: 1.8;
}

/* Formal Footer */
.classic-footer {
    background-color: #1a0e0a;
    padding: 6rem 0 2rem;
    text-align: center;
    color: rgba(249, 243, 233, 0.6);
}
.footer-logo-classic {
    height: 100px;
    border-radius: 50%;
    margin-bottom: 2rem;
    border: 1px solid var(--primary);
}
.footer-contact-info {
    margin-bottom: 3rem;
    line-height: 2;
}
.copyright {
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    border-top: 1px solid rgba(212, 175, 55, 0.1);
    padding-top: 2rem;
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
}
.fab-whatsapp svg { width: 35px; height: 35px; }

/* Responsive Classic */
@media (max-width: 992px) {
    .nav-side { display: none; } /* Hide side nav on mobile for this concept */
    .nav-center { padding: 0; }
    .classic-header { text-align: center; }
    .classic-hero-content { padding: 2rem 1.5rem; }
    .hero-frame h1 { font-size: 2.5rem; }
    .historia-flex { flex-direction: column; }
    .historia-image-arch { width: 100%; height: 400px; order: -1; }
}
"""

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css_base + new_css)

print("Layout 5 applied.")
