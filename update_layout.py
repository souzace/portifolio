import re

with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace everything after Hero Section but before </body>
new_content = """
    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-overlay"></div>
        <div class="container hero-content">
            <h1>O aroma fresco da tradição, todos os dias.</h1>
            <p>Pães de fermentação natural, doces artesanais e aquele café perfeito para acompanhar o seu momento.</p>
            <div class="hero-buttons">
                <a href="#vitrine" class="btn-primary">Conheça o Cardápio</a>
                <a href="#historia" class="btn-outline">Nossa História</a>
            </div>
        </div>
    </section>

    <!-- Vitrine de Produtos -->
    <section id="vitrine" class="vitrine">
        <div class="container">
            <h2 class="section-title">Nossas Especialidades</h2>
            <div class="product-grid">
                <!-- Pães -->
                <div class="product-card">
                    <div class="card-img placeholder-paes"></div>
                    <div class="card-content">
                        <h3>Pães Artesanais</h3>
                        <p>Fermentação natural de 48h, crosta rústica e miolo macio. O verdadeiro sabor do trigo.</p>
                    </div>
                </div>
                <!-- Confeitaria -->
                <div class="product-card">
                    <div class="card-img placeholder-doces"></div>
                    <div class="card-content">
                        <h3>Confeitaria Fina</h3>
                        <p>Eclairs, tarteletes e bolos afetivos feitos com chocolate belga e frutas frescas da estação.</p>
                    </div>
                </div>
                <!-- Café -->
                <div class="product-card">
                    <div class="card-img placeholder-cafe"></div>
                    <div class="card-content">
                        <h3>Cafés Especiais</h3>
                        <p>Grãos selecionados e torrados na medida certa para acompanhar suas pausas diárias.</p>
                    </div>
                </div>
                <!-- Frios -->
                <div class="product-card">
                    <div class="card-img placeholder-frios"></div>
                    <div class="card-content">
                        <h3>Frios e Antepastos</h3>
                        <p>Curadoria rigorosa de queijos curados, embutidos artesanais e geleias exclusivas.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- História & Autoridade -->
    <section id="historia" class="historia">
        <div class="container historia-wrapper">
            <div class="historia-text">
                <h2>A Arte do Tempo</h2>
                <p>No Empório Linneo, acreditamos que a boa comida não aceita atalhos. Nossa padaria nasceu do desejo de resgatar as receitas lentas e honestas.</p>
                <p>Nossos padeiros chegam antes do sol nascer para garantir que o croissant esteja na temperatura perfeita quando você entrar pela nossa porta. É uma mistura de técnica, ingredientes de origem e muita paixão.</p>
            </div>
            <div class="historia-img placeholder-baker"></div>
        </div>
    </section>

    <!-- Footer & Infos -->
    <footer class="footer">
        <div class="container footer-grid">
            <div class="footer-info">
                <img src="logomark.jpg" alt="Logo Empório Linneo" class="logo-img-footer">
                <p>O seu refúgio gastronômico no coração da cidade.</p>
            </div>
            <div class="footer-contact">
                <h3>Visite-nos</h3>
                <p>📍 Rua das Araucárias, 1250 - Bairro Nobre</p>
                <p>🕒 Todos os dias: 06h às 21h</p>
                <p>📞 (85) 9988-7766</p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Empório Linneo. Todos os direitos reservados.</p>
        </div>
    </footer>

    <!-- Botão Flutuante WhatsApp -->
    <a href="https://wa.me/558599887766" class="fab-whatsapp" target="_blank" aria-label="Pedir no WhatsApp">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.045.072.045.419-.1.824zm-3.423-14.416c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm.029 18.88c-1.161 0-2.305-.292-3.318-.844l-3.677.964.984-3.595c-.607-1.052-.927-2.246-.926-3.468.001-5.824 4.74-10.563 10.564-10.563 5.826 0 10.564 4.741 10.564 10.564 0 5.825-4.739 10.564-10.564 10.564z"/></svg>
    </a>
"""

html = re.sub(r'<!-- Hero Section -->.*?(?=</body>)', new_content, html, flags=re.DOTALL)

with open("emporio-linneo/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add Hero background image, Product Grid, and Footer CSS
new_css = """
/* Hero Updates */
.hero {
    background: url('hero_bakery.jpg') no-repeat center center/cover;
}
.hero-overlay {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: linear-gradient(rgba(53, 28, 21, 0.75), rgba(53, 28, 21, 0.9));
    z-index: 1;
}

/* Typography Headings */
.section-title {
    text-align: center;
    font-size: 2.5rem;
    color: var(--bg-dark);
    margin-bottom: 3rem;
}

/* Vitrine de Produtos */
.vitrine {
    padding: 6rem 0;
    background-color: var(--bg-light);
}
.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
}
.product-card {
    background-color: #fff;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 10px 20px rgba(53, 28, 21, 0.05);
    border: 1px solid rgba(212, 175, 55, 0.1);
    transition: transform 0.3s ease;
}
.product-card:hover {
    transform: translateY(-5px);
}
.card-img {
    height: 200px;
    background-color: #eaddc7;
    /* We will replace these with real images later */
}
.card-content {
    padding: 1.5rem;
}
.card-content h3 {
    font-size: 1.3rem;
    color: var(--bg-dark);
    margin-bottom: 0.5rem;
}
.card-content p {
    font-size: 0.95rem;
    color: var(--text-muted);
}

/* Historia */
.historia {
    padding: 6rem 0;
    background-color: var(--bg-dark);
    color: var(--bg-light);
}
.historia-wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
}
.historia h2 {
    color: var(--primary);
    font-size: 2.5rem;
    margin-bottom: 1.5rem;
}
.historia p {
    margin-bottom: 1rem;
    font-size: 1.1rem;
    color: rgba(249, 243, 233, 0.9);
}
.historia-img {
    height: 400px;
    background-color: #4a2c20;
    border-radius: 8px;
    border: 2px solid var(--primary);
}

/* Footer */
.footer {
    background-color: #24120e;
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

/* WhatsApp FAB */
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
.fab-whatsapp svg {
    width: 35px;
    height: 35px;
}
.fab-whatsapp:hover {
    transform: scale(1.1);
}

/* Responsive Fixes */
@media (max-width: 768px) {
    .historia-wrapper {
        grid-template-columns: 1fr;
    }
    .historia-img {
        height: 250px;
        order: -1;
    }
}
"""

css += new_css

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Layout updated.")
