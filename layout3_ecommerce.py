import re

with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

new_body = """<body>

    <!-- Header E-commerce Style -->
    <header class="ecommerce-header">
        <div class="container header-inner">
            <a href="#" class="logo-link"><img src="logomark.jpg" alt="Logo" class="ecommerce-logo"></a>
            <div class="search-bar">
                <input type="text" placeholder="O que você deseja provar hoje?">
            </div>
            <a href="https://wa.me/5585999362255" class="btn-cart">🛒 Meu Pedido</a>
        </div>
    </header>

    <!-- Mini Hero Banner -->
    <section class="ecommerce-hero" style="background-image: url('hero_bakery.jpg');">
        <div class="hero-gradient"></div>
        <div class="container hero-content">
            <h1>Sua padaria premium,<br>na porta da sua casa.</h1>
            <p>Pães frescos, cafés e doces entregues em até 40 minutos.</p>
        </div>
    </section>

    <!-- Interactive Categories -->
    <section class="categories-nav">
        <div class="container">
            <div class="cat-scroll">
                <button class="cat-btn active">🥐 Pães</button>
                <button class="cat-btn">🍰 Confeitaria</button>
                <button class="cat-btn">☕ Cafés</button>
                <button class="cat-btn">🧀 Frios</button>
            </div>
        </div>
    </section>

    <!-- E-commerce Vitrine -->
    <section class="ecommerce-products">
        <div class="container">
            <h2 class="section-title">Mais Pedidos da Semana</h2>
            <div class="product-grid">
                
                <!-- Product Card -->
                <div class="shop-card">
                    <div class="shop-img" style="background-image: url('product1.jpg');"></div>
                    <div class="shop-info">
                        <h3>Pão Rústico de Fermentação Natural</h3>
                        <p class="desc">Aproximadamente 500g. Casca crocante.</p>
                        <div class="price-row">
                            <span class="price">R$ 22,00</span>
                            <a href="https://wa.me/5585999362255" class="btn-add">+ Add</a>
                        </div>
                    </div>
                </div>

                <div class="shop-card">
                    <div class="shop-img" style="background-image: url('product2.jpg');"></div>
                    <div class="shop-info">
                        <h3>Tartelete de Frutas Vermelhas</h3>
                        <p class="desc">Massa sablée, creme de baunilha e frutas.</p>
                        <div class="price-row">
                            <span class="price">R$ 18,50</span>
                            <a href="https://wa.me/5585999362255" class="btn-add">+ Add</a>
                        </div>
                    </div>
                </div>

                <div class="shop-card">
                    <div class="shop-img" style="background-image: url('product3.jpg');"></div>
                    <div class="shop-info">
                        <h3>Café Especial Torra Média</h3>
                        <p class="desc">Pacote 250g. Notas de caramelo e nozes.</p>
                        <div class="price-row">
                            <span class="price">R$ 45,00</span>
                            <a href="https://wa.me/5585999362255" class="btn-add">+ Add</a>
                        </div>
                    </div>
                </div>

                <div class="shop-card">
                    <div class="shop-img" style="background-image: url('product4.jpg');"></div>
                    <div class="shop-info">
                        <h3>Tábua de Frios Artesanal</h3>
                        <p class="desc">Seleção do Chef para 2 pessoas.</p>
                        <div class="price-row">
                            <span class="price">R$ 89,00</span>
                            <a href="https://wa.me/5585999362255" class="btn-add">+ Add</a>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Delivery Banner -->
    <section class="delivery-banner">
        <div class="container banner-inner">
            <div class="banner-text">
                <h2>O pão quentinho chega até você.</h2>
                <p>Nossos motoboys possuem mochilas térmicas exclusivas para garantir que o croissant chegue desmanchando e o café pelando.</p>
            </div>
            <div class="banner-img" style="background-image: url('working.webp');"></div>
        </div>
    </section>

    <footer class="ecommerce-footer">
        <p>&copy; 2026 Empório Linneo - Av. Lineu Machado, 875 - Jóquei Clube. Todos os direitos reservados.</p>
    </footer>

</body>"""

html = re.sub(r'<body>.*?</body>', new_body, html, flags=re.DOTALL)

with open("emporio-linneo/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

css_base = css[:css.find("/* Split Layout Container */")]

new_css = """/* E-commerce Header */
.ecommerce-header {
    background-color: var(--bg-light);
    padding: 1rem 0;
    border-bottom: 1px solid rgba(53, 28, 21, 0.1);
    position: sticky;
    top: 0;
    z-index: 100;
}
.header-inner {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 2rem;
}
.ecommerce-logo {
    height: 70px;
    width: 70px;
    border-radius: 50%;
    border: 2px solid var(--primary);
}
.search-bar {
    flex: 1;
    max-width: 500px;
}
.search-bar input {
    width: 100%;
    padding: 0.8rem 1.5rem;
    border-radius: 30px;
    border: 1px solid rgba(53, 28, 21, 0.2);
    background-color: #fff;
    font-family: 'Outfit', sans-serif;
    outline: none;
}
.search-bar input:focus { border-color: var(--primary); }
.btn-cart {
    background-color: var(--bg-dark);
    color: var(--bg-light);
    padding: 0.8rem 1.5rem;
    border-radius: 30px;
    text-decoration: none;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    transition: transform 0.2s;
}
.btn-cart:hover { transform: scale(1.05); }

/* Mini Hero */
.ecommerce-hero {
    position: relative;
    height: 350px;
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
}
.hero-gradient {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: linear-gradient(to right, rgba(53,28,21,0.9) 0%, rgba(53,28,21,0.4) 100%);
}
.hero-content {
    position: relative;
    z-index: 2;
    color: var(--bg-light);
}
.hero-content h1 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
    font-family: 'Lora', serif;
}
.hero-content p {
    font-size: 1.1rem;
    opacity: 0.9;
}

/* Categories Nav */
.categories-nav {
    background-color: #fff;
    padding: 1rem 0;
    border-bottom: 1px solid rgba(53, 28, 21, 0.05);
}
.cat-scroll {
    display: flex;
    gap: 1rem;
    overflow-x: auto;
    padding-bottom: 0.5rem;
    scrollbar-width: none;
}
.cat-scroll::-webkit-scrollbar { display: none; }
.cat-btn {
    white-space: nowrap;
    padding: 0.6rem 1.5rem;
    border: 1px solid rgba(53, 28, 21, 0.2);
    border-radius: 30px;
    background-color: transparent;
    font-family: 'Outfit', sans-serif;
    font-weight: 600;
    color: var(--bg-dark);
    cursor: pointer;
    transition: all 0.2s;
}
.cat-btn:hover { border-color: var(--primary); color: var(--primary); }
.cat-btn.active {
    background-color: var(--primary);
    color: var(--bg-dark);
    border-color: var(--primary);
}

/* E-commerce Vitrine */
.ecommerce-products {
    padding: 4rem 0;
    background-color: var(--bg-light);
}
.section-title {
    font-size: 2rem;
    color: var(--bg-dark);
    margin-bottom: 2rem;
    font-family: 'Lora', serif;
}
.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 2rem;
}
.shop-card {
    background: #fff;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(53,28,21,0.05);
    border: 1px solid rgba(53,28,21,0.05);
    transition: transform 0.2s;
}
.shop-card:hover { transform: translateY(-5px); box-shadow: 0 8px 25px rgba(53,28,21,0.1);}
.shop-img {
    height: 220px;
    background-size: cover;
    background-position: center;
}
.shop-info {
    padding: 1.5rem;
}
.shop-info h3 {
    font-size: 1.2rem;
    color: var(--bg-dark);
    margin-bottom: 0.5rem;
    line-height: 1.3;
}
.shop-info .desc {
    font-size: 0.9rem;
    color: var(--text-muted);
    margin-bottom: 1.5rem;
    min-height: 40px;
}
.price-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.price {
    font-size: 1.3rem;
    font-weight: 700;
    color: var(--primary);
}
.btn-add {
    background-color: var(--bg-dark);
    color: var(--bg-light);
    padding: 0.5rem 1rem;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 600;
    font-size: 0.9rem;
}
.btn-add:hover { background-color: var(--primary); }

/* Delivery Banner */
.delivery-banner {
    padding: 4rem 0;
    background-color: #fff;
}
.banner-inner {
    background-color: var(--bg-dark);
    border-radius: 20px;
    display: flex;
    overflow: hidden;
}
.banner-text {
    flex: 1;
    padding: 4rem;
    color: var(--bg-light);
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.banner-text h2 {
    font-size: 2.2rem;
    color: var(--primary);
    margin-bottom: 1rem;
    font-family: 'Lora', serif;
}
.banner-text p { font-size: 1.1rem; opacity: 0.9; line-height: 1.6;}
.banner-img {
    flex: 1;
    background-size: cover;
    background-position: center;
}

.ecommerce-footer {
    text-align: center;
    padding: 2rem;
    background-color: var(--bg-light);
    color: var(--text-muted);
    font-size: 0.9rem;
}

@media (max-width: 768px) {
    .header-inner { flex-wrap: wrap; }
    .search-bar { order: 3; width: 100%; max-width: 100%; }
    .ecommerce-hero { height: 300px; text-align: center; }
    .hero-gradient { background: linear-gradient(to bottom, rgba(53,28,21,0.6) 0%, rgba(53,28,21,0.9) 100%); }
    .hero-content h1 { font-size: 2.2rem; }
    .banner-inner { flex-direction: column; }
    .banner-text { padding: 2rem; text-align: center; }
    .banner-img { height: 250px; }
}
"""

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css_base + new_css)

print("Layout 3 applied.")
