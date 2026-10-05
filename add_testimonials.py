import re

with open("beloton/index.html", "r", encoding="utf-8") as f:
    html = f.read()

testimonials_html = """
    <!-- Depoimentos -->
    <section class="testimonials">
        <div class="container">
            <h2 class="section-title">O que dizem os músicos</h2>
        </div>
        <div class="marquee-container">
            <div class="marquee-track">
                <!-- Testimonial 1 -->
                <div class="testimonial-card">
                    <div class="testimonial-header">
                        <div class="avatar">JB</div>
                        <div>
                            <h3>João Batista</h3>
                            <span>Saxofonista Profissional</span>
                        </div>
                    </div>
                    <p>"O sapatilhamento completo deixou meu sax tenor com uma resposta absurdamente rápida. O som está redondo, sem vazamento nenhum. Serviço impecável!"</p>
                    <div class="stars">★★★★★</div>
                </div>
                <!-- Testimonial 2 -->
                <div class="testimonial-card">
                    <div class="testimonial-header">
                        <div class="avatar">CM</div>
                        <div>
                            <h3>Carlos Mendes</h3>
                            <span>Trompetista</span>
                        </div>
                    </div>
                    <p>"Fiz o banho químico e a restauração do meu trompete e ele voltou parecendo que acabou de sair da fábrica. O brilho e a afinação ficaram perfeitos."</p>
                    <div class="stars">★★★★★</div>
                </div>
                <!-- Testimonial 3 -->
                <div class="testimonial-card">
                    <div class="testimonial-header">
                        <div class="avatar">LS</div>
                        <div>
                            <h3>Lucas Silva</h3>
                            <span>Flautista Orquestra</span>
                        </div>
                    </div>
                    <p>"Um luthier que realmente entende a alma do instrumento de sopro. A regulagem de chaves da minha flauta ficou um espetáculo. Recomendo de olhos fechados."</p>
                    <div class="stars">★★★★★</div>
                </div>
                <!-- Testimonial 4 -->
                <div class="testimonial-card">
                    <div class="testimonial-header">
                        <div class="avatar">RV</div>
                        <div>
                            <h3>Roberto Vaz</h3>
                            <span>Trombonista</span>
                        </div>
                    </div>
                    <p>"Tinha um amassado horrível na campana do meu trombone. A funilaria da Beloton deixou a campana lisa, intacta, sem marca nenhuma. Arte pura."</p>
                    <div class="stars">★★★★★</div>
                </div>
                <!-- Duplicate for Marquee Effect -->
                <div class="testimonial-card">
                    <div class="testimonial-header">
                        <div class="avatar">JB</div>
                        <div>
                            <h3>João Batista</h3>
                            <span>Saxofonista Profissional</span>
                        </div>
                    </div>
                    <p>"O sapatilhamento completo deixou meu sax tenor com uma resposta absurdamente rápida. O som está redondo, sem vazamento nenhum. Serviço impecável!"</p>
                    <div class="stars">★★★★★</div>
                </div>
                <div class="testimonial-card">
                    <div class="testimonial-header">
                        <div class="avatar">CM</div>
                        <div>
                            <h3>Carlos Mendes</h3>
                            <span>Trompetista</span>
                        </div>
                    </div>
                    <p>"Fiz o banho químico e a restauração do meu trompete e ele voltou parecendo que acabou de sair da fábrica. O brilho e a afinação ficaram perfeitos."</p>
                    <div class="stars">★★★★★</div>
                </div>
                <div class="testimonial-card">
                    <div class="testimonial-header">
                        <div class="avatar">LS</div>
                        <div>
                            <h3>Lucas Silva</h3>
                            <span>Flautista Orquestra</span>
                        </div>
                    </div>
                    <p>"Um luthier que realmente entende a alma do instrumento de sopro. A regulagem de chaves da minha flauta ficou um espetáculo. Recomendo de olhos fechados."</p>
                    <div class="stars">★★★★★</div>
                </div>
                <div class="testimonial-card">
                    <div class="testimonial-header">
                        <div class="avatar">RV</div>
                        <div>
                            <h3>Roberto Vaz</h3>
                            <span>Trombonista</span>
                        </div>
                    </div>
                    <p>"Tinha um amassado horrível na campana do meu trombone. A funilaria da Beloton deixou a campana lisa, intacta, sem marca nenhuma. Arte pura."</p>
                    <div class="stars">★★★★★</div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Final -->"""

html = html.replace('<!-- CTA Final -->', testimonials_html)

with open("beloton/index.html", "w", encoding="utf-8") as f:
    f.write(html)


with open("beloton/style.css", "r", encoding="utf-8") as f:
    css = f.read()

testimonials_css = """
/* Testimonials Marquee */
.testimonials {
    padding: 5rem 0;
    overflow: hidden;
    background-color: var(--bg-dark);
}
.marquee-container {
    width: 100vw;
    max-width: 100%;
    position: relative;
    padding: 20px 0;
}
.marquee-track {
    display: flex;
    width: max-content;
    gap: 2rem;
    align-items: stretch;
    animation: marquee-scroll 45s linear infinite;
}
.marquee-track:hover {
    animation-play-state: paused;
}
@keyframes marquee-scroll {
    from { transform: translateX(0); }
    to { transform: translateX(calc(-50% - 1rem)); }
}
.marquee-container::before, .marquee-container::after {
    content: "";
    position: absolute;
    top: 0;
    width: 150px;
    height: 100%;
    z-index: 2;
    pointer-events: none;
}
.marquee-container::before {
    left: 0;
    background: linear-gradient(to right, var(--bg-dark), transparent);
}
.marquee-container::after {
    right: 0;
    background: linear-gradient(to left, var(--bg-dark), transparent);
}

.testimonial-card {
    flex: 0 0 400px;
    max-width: 80vw;
    background-color: var(--bg-card);
    padding: 2rem;
    border-radius: 8px;
    border: 1px solid rgba(212, 175, 55, 0.1);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    display: flex;
    flex-direction: column;
    white-space: normal;
}
.testimonial-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
}
.testimonial-header .avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background-color: var(--gold);
    color: var(--bg-dark);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    font-weight: 700;
    font-family: 'Playfair Display', serif;
}
.testimonial-header h3 {
    margin-bottom: 0.2rem;
    font-size: 1.1rem;
}
.testimonial-header span {
    font-size: 0.85rem;
    color: var(--text-muted);
}
.testimonial-card p {
    font-style: italic;
    color: var(--text-light);
    flex-grow: 1;
    margin-bottom: 1.5rem;
}
.testimonial-card .stars {
    color: var(--gold);
    font-size: 1.2rem;
    letter-spacing: 2px;
}

@media (max-width: 768px) {
    .marquee-container::before, .marquee-container::after {
        width: 40px;
    }
    .testimonial-card {
        flex: 0 0 320px;
        padding: 1.5rem;
    }
}
"""

css += testimonials_css

with open("beloton/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Testimonials added.")
