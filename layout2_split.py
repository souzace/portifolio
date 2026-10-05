import re

with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. New HTML Structure for Split Screen
new_body = """<body>

    <div class="split-layout">
        <!-- Left Fixed Side (Brand & Navigation) -->
        <aside class="split-left">
            <div class="left-content">
                <img src="logomark.jpg" alt="Empório Linneo" class="logo-split">
                <h1>O aroma fresco da tradição,<br>todos os dias.</h1>
                <p>Pães de fermentação natural, doces artesanais e aquele café perfeito para acompanhar o seu momento.</p>
                <div class="split-actions">
                    <a href="https://wa.me/5585999362255" class="btn-primary" target="_blank">Pedir Delivery</a>
                    <a href="#vitrine" class="btn-outline">Ver Cardápio</a>
                </div>
            </div>
            
            <div class="left-footer">
                <p>📍 Av. Lineu Machado, 875 - Jóquei Clube<br>Fortaleza - CE</p>
                <p>🕒 Todos os dias: 06h às 21h</p>
            </div>
        </aside>

        <!-- Right Scrolling Side (Visuals & Products) -->
        <main class="split-right">
            <!-- Hero Image Full Height -->
            <section class="split-hero">
                <div class="split-hero-img" style="background-image: url('hero_bakery.jpg');"></div>
            </section>

            <!-- Bento Box / Grid de Produtos -->
            <section id="vitrine" class="split-vitrine">
                <h2 class="section-title-split">Nossas Especialidades</h2>
                <div class="bento-grid">
                    <div class="bento-item pao">
                        <div class="bento-bg" style="background-image: url('product1.jpg');"></div>
                        <div class="bento-overlay">
                            <h3>Pães Artesanais</h3>
                            <p>Fermentação de 48h</p>
                        </div>
                    </div>
                    <div class="bento-item doces">
                        <div class="bento-bg" style="background-image: url('product2.jpg');"></div>
                        <div class="bento-overlay">
                            <h3>Confeitaria Fina</h3>
                            <p>Chocolate Belga</p>
                        </div>
                    </div>
                    <div class="bento-item cafe">
                        <div class="bento-bg" style="background-image: url('product3.jpg');"></div>
                        <div class="bento-overlay">
                            <h3>Cafés Especiais</h3>
                            <p>Torra Perfeita</p>
                        </div>
                    </div>
                    <div class="bento-item frios">
                        <div class="bento-bg" style="background-image: url('product4.jpg');"></div>
                        <div class="bento-overlay">
                            <h3>Frios</h3>
                            <p>Queijos Curados</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- História -->
            <section class="split-historia">
                <div class="historia-box">
                    <h2>A Arte do Tempo</h2>
                    <p>No Empório Linneo, acreditamos que a boa comida não aceita atalhos. Nossa padaria nasceu do desejo de resgatar as receitas lentas e honestas.</p>
                    <p>Nossos padeiros chegam antes do sol nascer para garantir que o croissant esteja na temperatura perfeita quando você entrar pela nossa porta.</p>
                </div>
                <div class="historia-image" style="background-image: url('working.webp');"></div>
            </section>
            
            <footer class="split-footer-bottom">
                <p>&copy; 2026 Empório Linneo. Todos os direitos reservados.</p>
            </footer>
        </main>
    </div>

    <!-- Botão Flutuante WhatsApp -->
    <a href="https://wa.me/5585999362255" class="fab-whatsapp" target="_blank" aria-label="Pedir no WhatsApp">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824zm-3.423-14.416c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm.029 18.88c-1.161 0-2.305-.292-3.318-.844l-3.677.964.984-3.595c-.607-1.052-.927-2.246-.926-3.468.001-5.824 4.74-10.563 10.564-10.563 5.826 0 10.564 4.741 10.564 10.564 0 5.825-4.739 10.564-10.564 10.564z"/></svg>
    </a>
</body>"""

# Replace entire body
html = re.sub(r'<body>.*?</body>', new_body, html, flags=re.DOTALL)

with open("emporio-linneo/index.html", "w", encoding="utf-8") as f:
    f.write(html)


with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

css_base = css[:css.find("/* Header Minimalista */")]

# CSS for Split Layout
new_css = """/* Split Layout Container */
.split-layout {
    display: flex;
    min-height: 100vh;
}

/* Left Side - Fixed Panel */
.split-left {
    width: 40%;
    background-color: var(--bg-dark);
    color: var(--bg-light);
    height: 100vh;
    position: sticky;
    top: 0;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 4rem;
    box-shadow: 5px 0 20px rgba(0,0,0,0.2);
    z-index: 10;
}
.logo-split {
    width: 140px;
    height: 140px;
    border-radius: 50%;
    border: 2px solid var(--primary);
    margin-bottom: 3rem;
}
.left-content h1 {
    font-size: 3rem;
    line-height: 1.1;
    margin-bottom: 1.5rem;
    color: var(--bg-light);
}
.left-content p {
    font-size: 1.1rem;
    color: rgba(249, 243, 233, 0.8);
    margin-bottom: 2.5rem;
}
.split-actions {
    display: flex;
    gap: 1rem;
}
.left-footer {
    font-size: 0.9rem;
    color: rgba(249, 243, 233, 0.5);
    border-top: 1px solid rgba(212, 175, 55, 0.2);
    padding-top: 1.5rem;
}
.left-footer p { margin-bottom: 0.5rem; }

/* Buttons inside dark background */
.btn-primary {
    display: inline-block;
    padding: 0.8rem 1.8rem;
    background-color: var(--primary);
    color: var(--bg-dark);
    text-decoration: none;
    font-weight: 600;
    border-radius: 4px;
    transition: background-color 0.3s ease;
}
.btn-primary:hover { background-color: var(--primary-hover); }

.btn-outline {
    display: inline-block;
    padding: 0.8rem 1.8rem;
    border: 1px solid var(--primary);
    color: var(--primary);
    text-decoration: none;
    font-weight: 600;
    border-radius: 4px;
    transition: all 0.3s ease;
}
.btn-outline:hover { background-color: var(--primary); color: var(--bg-dark); }


/* Right Side - Scrolling Panel */
.split-right {
    width: 60%;
    background-color: var(--bg-light);
    overflow-x: hidden;
}

/* Split Hero Image */
.split-hero-img {
    height: 100vh;
    background-size: cover;
    background-position: center;
}

/* Bento Box Vitrine */
.split-vitrine {
    padding: 6rem 4rem;
}
.section-title-split {
    font-size: 2.5rem;
    color: var(--text-dark);
    margin-bottom: 3rem;
    font-family: 'Lora', serif;
}
.bento-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-auto-rows: 250px;
    gap: 1.5rem;
}
.bento-item {
    position: relative;
    border-radius: 12px;
    overflow: hidden;
}
.bento-item.pao { grid-column: span 2; grid-row: span 2; } /* Makes bread item huge */
.bento-bg {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background-size: cover;
    background-position: center;
    transition: transform 0.5s ease;
}
.bento-item:hover .bento-bg { transform: scale(1.08); }

.bento-overlay {
    position: absolute;
    bottom: 0; left: 0; width: 100%;
    padding: 2rem;
    background: linear-gradient(transparent, rgba(53, 28, 21, 0.9));
    color: var(--bg-light);
}
.bento-overlay h3 { font-size: 1.5rem; font-family: 'Lora', serif; margin-bottom: 0.2rem;}
.bento-item.pao .bento-overlay h3 { font-size: 2.5rem; }

/* Split Historia */
.split-historia {
    background-color: #fff;
    display: flex;
    align-items: center;
}
.historia-box {
    flex: 1;
    padding: 4rem;
}
.historia-box h2 {
    font-size: 2.5rem;
    color: var(--text-dark);
    margin-bottom: 1.5rem;
}
.historia-box p {
    font-size: 1.1rem;
    color: var(--text-muted);
    margin-bottom: 1.5rem;
}
.historia-image {
    flex: 1;
    height: 600px;
    background-size: cover;
    background-position: center;
}

.split-footer-bottom {
    padding: 3rem;
    text-align: center;
    background-color: var(--bg-light);
    color: var(--text-muted);
    font-size: 0.9rem;
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

/* Responsive Mobile Stacking */
@media (max-width: 992px) {
    .split-layout { flex-direction: column; }
    .split-left {
        width: 100%;
        height: auto;
        position: relative;
        padding: 3rem 2rem;
    }
    .split-right { width: 100%; }
    .split-hero-img { height: 60vh; }
    .bento-grid { grid-template-columns: 1fr; grid-auto-rows: 250px; }
    .bento-item.pao { grid-column: span 1; grid-row: span 1; }
    .split-historia { flex-direction: column; }
    .historia-box { padding: 3rem 2rem; }
    .historia-image { width: 100%; height: 300px; }
    .split-actions { flex-direction: column; }
    .btn-primary, .btn-outline { text-align: center; }
}
"""

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css_base + new_css)

print("Layout 2 applied.")
