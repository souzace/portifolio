import re

with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

new_body = """<body>

    <!-- Hybrid Header: Symmetrical (Prop 5) + Fixed/Immersive (Prop 4) -->
    <header class="hybrid-header">
        <div class="container classic-nav-container">
            <nav class="nav-side left">
                <a href="#cardapio">Cardápio</a>
                <a href="#historia">Nossa Arte</a>
            </nav>
            <div class="nav-center">
                <a href="#"><img src="logomark.jpg" alt="Logo Empório Linneo" class="logo-hybrid"></a>
            </div>
            <nav class="nav-side right">
                <a href="https://wa.me/5585999362255">Delivery</a>
                <a href="#contato">Contato</a>
            </nav>
        </div>
    </header>

    <!-- Immersive Hero (Prop 4) -->
    <section class="hybrid-hero" style="background-image: url('hero_bakery.jpg');">
        <div class="hero-blur-overlay"></div>
        <div class="container hero-content-center">
            <h1>A arte de pausar.</h1>
            <p>Mais do que uma padaria, um refúgio focado no tempo e no verdadeiro sabor do trigo.</p>
            <a href="#cardapio" class="btn-classic-hollow">Conhecer o Menu</a>
        </div>
    </section>

    <!-- Arched Vitrine (Prop 5) -->
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
                        <p>Fermentação lenta e crosta perfeita.</p>
                    </div>
                </div>

                <div class="arch-card">
                    <div class="arch-img" style="background-image: url('product2.jpg');"></div>
                    <div class="arch-text">
                        <h3>Confeitaria</h3>
                        <p>A arte francesa aplicada aos doces afetivos.</p>
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
                        <p>Acompanhamentos curados para celebrar.</p>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Classic Historia Split (Prop 5) -->
    <section id="historia" class="classic-historia">
        <div class="container historia-flex">
            <div class="historia-image-arch" style="background-image: url('working.webp');"></div>
            <div class="historia-content-centered">
                <span class="subtitle">Nossa Essência</span>
                <h2>A Arte do Tempo</h2>
                <div class="divider"></div>
                <p>Acreditamos que a boa comida não aceita atalhos. Nossa padaria nasceu do desejo de resgatar as receitas lentas e honestas.</p>
                <p>Nossos padeiros chegam antes do sol nascer para garantir que o croissant esteja na temperatura perfeita quando você entrar pela nossa porta.</p>
            </div>
        </div>
    </section>

    <!-- Formal Footer (Prop 5) -->
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

css_base = css[:css.find("/* Classic Header */")]

new_css = """/* Hybrid Header (Fixed + Symmetrical) */
.hybrid-header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    /* Dark semi-transparent background to remain legible while scrolling */
    background-color: rgba(44, 30, 22, 0.95);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid rgba(212, 175, 55, 0.2);
    padding: 0.8rem 0;
    z-index: 1000;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
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
    font-size: 0.85rem;
    font-family: 'Outfit', sans-serif;
    transition: color 0.3s;
    font-weight: 600;
}
.nav-side a:hover { color: var(--bg-light); }
.nav-center {
    padding: 0 4rem;
}
.logo-hybrid {
    width: 80px; /* Smaller to fit the fixed header elegantly */
    height: 80px;
    border-radius: 50%;
    border: 2px solid var(--primary);
    transition: transform 0.3s;
    display: block;
}
.logo-hybrid:hover { transform: scale(1.05); }

/* Immersive Hero */
.hybrid-hero {
    height: 100vh;
    background-size: cover;
    background-position: center;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    /* Margin top is NOT needed because we want the hero to go under the transparent fixed header */
}
.hero-blur-overlay {
    position: absolute;
    top:0; left:0; width:100%; height:100%;
    background: rgba(44, 30, 22, 0.6);
}
.hero-content-center {
    position: relative;
    z-index: 2;
    color: var(--bg-light);
    max-width: 800px;
    padding: 0 2rem;
    margin-top: 80px; /* Push content down so it doesn't hide behind header */
}
.hero-content-center h1 {
    font-size: 4.5rem;
    font-family: 'Lora', serif;
    margin-bottom: 1rem;
    color: var(--primary);
}
.hero-content-center p {
    font-size: 1.3rem;
    opacity: 0.9;
    font-style: italic;
    font-family: 'Lora', serif;
    margin-bottom: 3rem;
}
.btn-classic-hollow {
    display: inline-block;
    padding: 1rem 2.5rem;
    border: 1px solid var(--primary);
    color: var(--bg-light);
    text-transform: uppercase;
    letter-spacing: 2px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s;
}
.btn-classic-hollow:hover { background-color: var(--primary); color: var(--bg-dark); }

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
    transition: transform 0.3s;
}
.arch-card:hover .arch-img { transform: translateY(-10px); }
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

/* Responsive Mobile */
@media (max-width: 992px) {
    .nav-side { display: none; } /* Hide side nav on mobile to keep header clean */
    .nav-center { padding: 0; }
    .hybrid-header { justify-content: center; padding: 0.5rem 0; }
    .logo-hybrid { width: 60px; height: 60px; }
    
    .hero-content-center h1 { font-size: 3rem; }
    .historia-flex { flex-direction: column; }
    .historia-image-arch { width: 100%; height: 400px; order: -1; }
}
"""

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css_base + new_css)

print("Layout 6 applied.")
