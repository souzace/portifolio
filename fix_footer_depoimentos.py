import re

with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the regular footer and inject depoimentos before it
old_footer = """    <!-- Regular Footer (Static) -->
    <footer id="contato" class="regular-footer">
        <div class="container">
            <div class="footer-contact-info">
                <p>📍 Av. Lineu Machado, 875 - Jóquei Clube, Fortaleza - CE</p>
                <p>🕒 Aberto todos os dias das 06h às 21h</p>
                <p>📞 WhatsApp: (85) 99936-2255</p>
            </div>
            <p class="copyright">&copy; 2026 Empório Linneo. Tradição & Sabor.</p>
        </div>
    </footer>"""

new_sections = """    <!-- Depoimentos (Animated Marquee) -->
    <section class="testimonial-marquee-section">
        <div class="marquee-container">
            <div class="marquee-track">
                <div class="testimonial-card">
                    <p>"O melhor croissant que já comi fora de Paris."</p>
                    <span>- Revista Sabores</span>
                </div>
                <div class="testimonial-card">
                    <p>"O pão de fermentação natural é simplesmente perfeito."</p>
                    <span>- Cliente Satisfeito</span>
                </div>
                <div class="testimonial-card">
                    <p>"Atendimento impecável e doces inesquecíveis."</p>
                    <span>- Guia Gastronômico</span>
                </div>
                <div class="testimonial-card">
                    <p>"Um verdadeiro refúgio no meio da cidade."</p>
                    <span>- Ana Maria</span>
                </div>
                <!-- Duplicate for seamless scroll -->
                <div class="testimonial-card">
                    <p>"O melhor croissant que já comi fora de Paris."</p>
                    <span>- Revista Sabores</span>
                </div>
                <div class="testimonial-card">
                    <p>"O pão de fermentação natural é simplesmente perfeito."</p>
                    <span>- Cliente Satisfeito</span>
                </div>
                <div class="testimonial-card">
                    <p>"Atendimento impecável e doces inesquecíveis."</p>
                    <span>- Guia Gastronômico</span>
                </div>
                <div class="testimonial-card">
                    <p>"Um verdadeiro refúgio no meio da cidade."</p>
                    <span>- Ana Maria</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Regular Footer (Static) -->
    <footer id="contato" class="regular-footer">
        <div class="container">
            <div class="footer-contact-info">
                <p>📍 Av. Lineu Machado, 875 - Jóquei Clube, Fortaleza - CE</p>
                <p>🕒 Aberto todos os dias das 06h às 21h</p>
            </div>
            <p class="copyright">&copy; 2026 Empório Linneo. Tradição & Sabor.</p>
            <p class="orkes-credits">Desenvolvido por <a href="https://orkes.com.br" target="_blank" style="color: var(--primary); text-decoration: none;">Orkes</a></p>
        </div>
    </footer>"""

html = html.replace(old_footer, new_sections)

with open("emporio-linneo/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Modify footer CSS to reduce padding and add Orkes
old_css_footer = """/* Regular Footer */
.regular-footer {
    background-color: #1a0e0a;
    padding: 6rem 0 4rem;
    text-align: center;
    color: rgba(249, 243, 233, 0.6);
}
.regular-footer .footer-contact-info {
    margin-bottom: 2rem;
    line-height: 2;
    font-size: 1.1rem;
}
.regular-footer .copyright {
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    border-top: 1px solid rgba(212, 175, 55, 0.1);
    padding-top: 2rem;
}"""

new_css_footer = """/* Regular Footer */
.regular-footer {
    background-color: #1a0e0a;
    padding: 3rem 0 2rem;
    text-align: center;
    color: rgba(249, 243, 233, 0.6);
}
.regular-footer .footer-contact-info {
    margin-bottom: 1.5rem;
    line-height: 1.8;
    font-size: 0.95rem;
}
.regular-footer .copyright {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    border-top: 1px solid rgba(212, 175, 55, 0.1);
    padding-top: 1.5rem;
    margin-bottom: 0.5rem;
}
.orkes-credits {
    font-size: 0.75rem;
    color: var(--primary);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}"""

css = css.replace(old_css_footer, new_css_footer)

# Add Testimonials CSS
testimonials_css = """
/* Testimonial Marquee */
.testimonial-marquee-section {
    background-color: var(--bg-light);
    padding: 5rem 0;
    overflow: hidden;
    border-top: 1px solid rgba(53, 28, 21, 0.05);
}
.marquee-container {
    width: 100%;
    overflow: hidden;
    position: relative;
    display: flex;
}
.marquee-track {
    display: flex;
    gap: 2rem;
    animation: scroll-marquee 20s linear infinite;
    width: max-content;
}
.marquee-track:hover {
    animation-play-state: paused;
}
@keyframes scroll-marquee {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}
.testimonial-card {
    background-color: #fff;
    padding: 2.5rem;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(53, 28, 21, 0.03);
    width: 400px;
    border: 1px solid rgba(53, 28, 21, 0.05);
}
.testimonial-card p {
    font-family: 'Lora', serif;
    font-size: 1.15rem;
    color: var(--bg-dark);
    margin-bottom: 1.5rem;
    font-style: italic;
    line-height: 1.5;
}
.testimonial-card span {
    font-family: 'Outfit', sans-serif;
    color: var(--primary);
    font-weight: 600;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 1px;
}
@media (max-width: 768px) {
    .testimonial-card { width: 300px; padding: 1.5rem; }
}
"""

css = testimonials_css + css

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Footer reduced, whatsapp removed, Orkes added, and Depoimentos animated added.")
