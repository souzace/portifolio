import re

with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

new_body = """<body>

    <!-- Header Transparente -->
    <header class="masonry-header">
        <a href="#" class="logo-link"><img src="logomark.jpg" alt="Logo" class="masonry-logo"></a>
        <nav class="masonry-nav">
            <a href="#galeria">Galeria</a>
            <a href="#experiencia">Nossa Experiência</a>
            <a href="https://wa.me/5585999362255" class="btn-reservar">Faça seu Pedido</a>
        </nav>
    </header>

    <!-- Hero Cinematográfico -->
    <section class="masonry-hero" style="background-image: url('hero_bakery.jpg');">
        <div class="hero-blur-overlay"></div>
        <div class="container hero-content-center">
            <h1>A arte de pausar.</h1>
            <p>Mais do que uma padaria, um estilo de vida focado nos detalhes, no tempo e no verdadeiro sabor do trigo.</p>
        </div>
    </section>

    <!-- Masonry Gallery (Vitrine Visual) -->
    <section id="galeria" class="masonry-gallery">
        <div class="container">
            <h2 class="section-title-minimal">Nosso Menu Visual</h2>
            
            <div class="masonry-grid">
                
                <div class="masonry-item large" style="background-image: url('product1.jpg');">
                    <div class="masonry-overlay">
                        <h3>Pães Rústicos</h3>
                        <a href="#">Ver detalhes →</a>
                    </div>
                </div>

                <div class="masonry-item tall" style="background-image: url('product2.jpg');">
                    <div class="masonry-overlay">
                        <h3>Confeitaria Fina</h3>
                        <a href="#">Ver detalhes →</a>
                    </div>
                </div>

                <div class="masonry-item wide" style="background-image: url('product3.jpg');">
                    <div class="masonry-overlay">
                        <h3>Cafés Especiais</h3>
                        <a href="#">Ver detalhes →</a>
                    </div>
                </div>

                <div class="masonry-item standard" style="background-image: url('product4.jpg');">
                    <div class="masonry-overlay">
                        <h3>Charcutaria</h3>
                        <a href="#">Ver detalhes →</a>
                    </div>
                </div>

                <!-- Repeating some images just to fill the grid beautifully -->
                <div class="masonry-item tall" style="background-image: url('working.webp');">
                    <div class="masonry-overlay">
                        <h3>Nossa Produção</h3>
                        <a href="#">Conheça a cozinha →</a>
                    </div>
                </div>

                <div class="masonry-item standard" style="background-image: url('hero_bakery.jpg');">
                    <div class="masonry-overlay">
                        <h3>O Ambiente</h3>
                        <a href="#">Venha nos visitar →</a>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Depoimento Destaque -->
    <section class="testimonial-highlight">
        <div class="container">
            <p class="quote">"O melhor croissant que já comi fora de Paris. O Empório Linneo não é só uma padaria, é um refúgio para quem ama gastronomia de verdade."</p>
            <span class="author">- Revista Sabores do Ceará</span>
        </div>
    </section>

    <!-- Minimal Footer -->
    <footer class="masonry-footer">
        <div class="container footer-flex">
            <div class="footer-brand">
                <img src="logomark.jpg" alt="Logo" class="footer-logo-small">
                <p>📍 Av. Lineu Machado, 875 - Jóquei Clube<br>Fortaleza - CE</p>
            </div>
            <div class="footer-links">
                <a href="#">Instagram</a>
                <a href="#">WhatsApp</a>
                <a href="#">Como Chegar</a>
            </div>
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

css_base = css[:css.find("/* E-commerce Header */")]

new_css = """/* Masonry Header */
.masonry-header {
    position: absolute;
    top: 0; left: 0; width: 100%;
    padding: 2rem 4rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 100;
}
.masonry-logo {
    height: 90px;
    width: 90px;
    border-radius: 50%;
    border: 2px solid var(--primary);
}
.masonry-nav {
    display: flex;
    gap: 2rem;
    align-items: center;
}
.masonry-nav a {
    color: var(--bg-light);
    text-decoration: none;
    font-weight: 400;
    font-size: 1rem;
    letter-spacing: 1px;
}
.masonry-nav a:hover { color: var(--primary); }
.btn-reservar {
    border: 1px solid var(--primary);
    padding: 0.6rem 1.5rem;
    border-radius: 30px;
    transition: all 0.3s;
}
.btn-reservar:hover { background-color: var(--primary); color: var(--bg-dark) !important; }

/* Hero Cinematografico */
.masonry-hero {
    height: 100vh;
    background-size: cover;
    background-position: center;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}
.hero-blur-overlay {
    position: absolute;
    top:0; left:0; width:100%; height:100%;
    background: rgba(53, 28, 21, 0.6);
    backdrop-filter: blur(2px);
}
.hero-content-center {
    position: relative;
    z-index: 2;
    color: var(--bg-light);
    max-width: 800px;
}
.hero-content-center h1 {
    font-size: 5rem;
    font-family: 'Lora', serif;
    margin-bottom: 1rem;
    letter-spacing: -1px;
}
.hero-content-center p {
    font-size: 1.3rem;
    opacity: 0.9;
    font-weight: 300;
}

/* Masonry Gallery */
.masonry-gallery {
    padding: 8rem 0;
    background-color: var(--bg-dark);
}
.section-title-minimal {
    text-align: center;
    color: var(--bg-light);
    font-family: 'Outfit', sans-serif;
    text-transform: uppercase;
    letter-spacing: 4px;
    font-size: 1.2rem;
    margin-bottom: 4rem;
}

.masonry-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-auto-rows: 250px;
    gap: 15px;
}
.masonry-item {
    position: relative;
    background-size: cover;
    background-position: center;
    border-radius: 4px;
    overflow: hidden;
    cursor: pointer;
}
/* Grid spanning classes */
.masonry-item.large { grid-column: span 2; grid-row: span 2; }
.masonry-item.wide { grid-column: span 2; grid-row: span 1; }
.masonry-item.tall { grid-column: span 1; grid-row: span 2; }

.masonry-overlay {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(53, 28, 21, 0.8);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.4s ease;
    text-align: center;
}
.masonry-item:hover .masonry-overlay { opacity: 1; }
.masonry-overlay h3 {
    color: var(--primary);
    font-family: 'Lora', serif;
    font-size: 2rem;
    margin-bottom: 0.5rem;
}
.masonry-overlay a {
    color: var(--bg-light);
    text-decoration: none;
    font-size: 0.9rem;
    border-bottom: 1px solid var(--bg-light);
    padding-bottom: 2px;
}

/* Testimonial */
.testimonial-highlight {
    background-color: var(--bg-light);
    padding: 8rem 0;
    text-align: center;
}
.testimonial-highlight .quote {
    font-family: 'Lora', serif;
    font-size: 2.2rem;
    color: var(--bg-dark);
    font-style: italic;
    max-width: 900px;
    margin: 0 auto 2rem;
    line-height: 1.4;
}
.testimonial-highlight .author {
    font-family: 'Outfit', sans-serif;
    color: var(--primary);
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* Masonry Footer */
.masonry-footer {
    background-color: var(--bg-dark);
    padding: 4rem 0;
    border-top: 1px solid rgba(212, 175, 55, 0.1);
}
.footer-flex {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.footer-logo-small {
    height: 60px;
    border-radius: 50%;
    margin-bottom: 1rem;
}
.footer-brand p { color: rgba(249, 243, 233, 0.6); font-size: 0.9rem; }
.footer-links { display: flex; gap: 2rem; }
.footer-links a {
    color: var(--bg-light);
    text-decoration: none;
    text-transform: uppercase;
    font-size: 0.85rem;
    letter-spacing: 1px;
}
.footer-links a:hover { color: var(--primary); }

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

/* Mobile */
@media (max-width: 768px) {
    .masonry-header { flex-direction: column; gap: 1rem; padding: 2rem 1rem; }
    .masonry-nav { flex-wrap: wrap; justify-content: center; }
    .hero-content-center h1 { font-size: 3rem; }
    .masonry-grid { grid-template-columns: 1fr; grid-auto-rows: 300px; }
    .masonry-item.large, .masonry-item.wide, .masonry-item.tall { grid-column: span 1; grid-row: span 1; }
    .footer-flex { flex-direction: column; text-align: center; gap: 2rem; }
}
"""

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css_base + new_css)

print("Layout 4 applied.")
