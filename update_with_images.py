import re

with open("el-bethel/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Hero Image
hero_image_html = """        <div class="hero-image">
            <img src="model.png" alt="Óculos de Grau Estilosos" style="width: 100%; height: 100%; object-fit: cover; border-radius: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
        </div>"""
html = re.sub(r'<div class="hero-image">.*?</div>', hero_image_html, html, flags=re.DOTALL)

# 2. Add Product Showcase (Vitrine) after Services
vitrine_html = """
    <!-- Vitrine de Produtos -->
    <section class="vitrine">
        <div class="vitrine-header">
            <h2 class="vitrine-title">Coleção Exclusiva</h2>
            <p class="vitrine-subtitle">Encontre a armação perfeita que combina com o seu estilo.</p>
        </div>
        <div class="product-grid">
            <div class="product-card"><img src="oculos1.png" alt="Óculos 1"><div class="product-overlay"><a href="https://api.whatsapp.com/send?phone=5585988236302" class="btn-primary" style="padding: 0.5rem 1rem; font-size: 0.8rem;">Eu Quero</a></div></div>
            <div class="product-card"><img src="oculos2.png" alt="Óculos 2"><div class="product-overlay"><a href="https://api.whatsapp.com/send?phone=5585988236302" class="btn-primary" style="padding: 0.5rem 1rem; font-size: 0.8rem;">Eu Quero</a></div></div>
            <div class="product-card"><img src="oculos3.png" alt="Óculos 3"><div class="product-overlay"><a href="https://api.whatsapp.com/send?phone=5585988236302" class="btn-primary" style="padding: 0.5rem 1rem; font-size: 0.8rem;">Eu Quero</a></div></div>
            <div class="product-card"><img src="oculos4.png" alt="Óculos 4"><div class="product-overlay"><a href="https://api.whatsapp.com/send?phone=5585988236302" class="btn-primary" style="padding: 0.5rem 1rem; font-size: 0.8rem;">Eu Quero</a></div></div>
            <div class="product-card"><img src="oculos5.png" alt="Óculos 5"><div class="product-overlay"><a href="https://api.whatsapp.com/send?phone=5585988236302" class="btn-primary" style="padding: 0.5rem 1rem; font-size: 0.8rem;">Eu Quero</a></div></div>
            <div class="product-card"><img src="oculos6.png" alt="Óculos 6"><div class="product-overlay"><a href="https://api.whatsapp.com/send?phone=5585988236302" class="btn-primary" style="padding: 0.5rem 1rem; font-size: 0.8rem;">Eu Quero</a></div></div>
            <div class="product-card"><img src="oculos7.png" alt="Óculos 7"><div class="product-overlay"><a href="https://api.whatsapp.com/send?phone=5585988236302" class="btn-primary" style="padding: 0.5rem 1rem; font-size: 0.8rem;">Eu Quero</a></div></div>
            <div class="product-card"><img src="oculos8.png" alt="Óculos 8"><div class="product-overlay"><a href="https://api.whatsapp.com/send?phone=5585988236302" class="btn-primary" style="padding: 0.5rem 1rem; font-size: 0.8rem;">Eu Quero</a></div></div>
        </div>
        <div style="text-align: center; margin-top: 3rem;">
            <a href="https://api.whatsapp.com/send?phone=5585988236302" target="_blank" class="btn-primary">Ver Catálogo Completo</a>
        </div>
    </section>
"""
html = html.replace('</section>\n\n    <!-- Confiança & Agendamento -->', '</section>\n' + vitrine_html + '\n    <!-- Confiança & Agendamento -->')

# 3. Update Trust Section to be a side-by-side with model2.png
new_trust_html = """
    <!-- Confiança & Agendamento -->
    <section class="trust">
        <div class="trust-container">
            <div class="trust-image">
                <img src="model2.png" alt="Cuidado com a sua visão">
            </div>
            <div class="trust-content">
                <h2 class="trust-title">SAÚDE E PRECISÃO QUE VOCÊ CONFIA</h2>
                <p class="trust-subtitle">Precisa atualizar seu grau? Fale com nossa equipe para orientações sobre exames e avaliações. Sua visão tratada com o carinho que ela merece.</p>
                <a href="https://api.whatsapp.com/send?phone=5585988236302" class="btn-secondary" target="_blank">Agendar Atendimento</a>
            </div>
        </div>
    </section>
"""
html = re.sub(r'<!-- Confiança & Agendamento -->.*?</section>', new_trust_html, html, flags=re.DOTALL)

with open("el-bethel/index.html", "w", encoding="utf-8") as f:
    f.write(html)


# Update CSS
with open("el-bethel/style.css", "r", encoding="utf-8") as f:
    css = f.read()

vitrine_css = """
/* Vitrine */
.vitrine {
    padding: 5rem 2rem;
    background-color: var(--gray-bg);
}
.vitrine-header {
    text-align: center;
    margin-bottom: 3rem;
}
.vitrine-title {
    font-weight: 700;
    font-size: 2.2rem;
    color: var(--brand-blue);
    margin-bottom: 0.5rem;
}
.vitrine-subtitle {
    font-family: 'Dancing Script', cursive;
    font-size: 1.8rem;
    color: var(--brand-red);
}
.product-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
    max-width: 1200px;
    margin: 0 auto;
}
@media(min-width: 768px) {
    .product-grid {
        grid-template-columns: repeat(4, 1fr);
        gap: 2rem;
    }
}
.product-card {
    background-color: var(--white);
    border-radius: 20px;
    padding: 1.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 8px 20px rgba(0,0,0,0.05);
    position: relative;
    overflow: hidden;
    aspect-ratio: 1;
}
.product-card img {
    width: 100%;
    height: auto;
    object-fit: contain;
    transition: transform 0.3s ease;
}
.product-card:hover img {
    transform: scale(1.05);
}
.product-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255,255,255,0.8);
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.3s ease;
}
.product-card:hover .product-overlay {
    opacity: 1;
}

/* Updated Trust Layout */
.trust {
    padding: 0;
    text-align: left;
    background-color: transparent;
    color: var(--text-dark);
    margin: 5rem 2rem;
}
.trust-container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    background-color: var(--brand-blue);
    border-radius: 40px;
    overflow: hidden;
    color: var(--white);
    box-shadow: 0 15px 40px rgba(0, 86, 128, 0.2);
}
@media(min-width: 768px) {
    .trust-container {
        flex-direction: row;
    }
}
.trust-image {
    flex: 1;
    min-height: 300px;
}
.trust-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.trust-content {
    flex: 1;
    padding: 4rem 2rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
@media(min-width: 768px) {
    .trust-content {
        padding: 4rem;
    }
}
"""

css = css.replace('/* Trust */', vitrine_css + '\n/* Trust Legacy */')

with open("el-bethel/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Images integrated and layout updated.")
