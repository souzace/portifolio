import re

with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the current fixed footer with the new setup (Regular Footer + Fixed Bar)
old_footer = """    <footer id="contato" class="classic-footer-fixed">
        <div class="container footer-fixed-flex">
            <div class="footer-fixed-left">
                <div class="footer-fixed-text">
                    <span class="ff-title">Empório Linneo</span>
                    <span class="ff-sub">📍 Av. Lineu Machado, 875 | 🕒 06h às 21h</span>
                </div>
            </div>
            <div class="footer-fixed-right">
                <a href="https://wa.me/5585999362255" target="_blank" class="btn-footer-wa">
                    Faça seu Pedido
                </a>
            </div>
        </div>
    </footer>"""

new_footers = """    <!-- Regular Footer (Static) -->
    <footer id="contato" class="regular-footer">
        <div class="container">
            <div class="footer-contact-info">
                <p>📍 Av. Lineu Machado, 875 - Jóquei Clube, Fortaleza - CE</p>
                <p>🕒 Aberto todos os dias das 06h às 21h</p>
                <p>📞 WhatsApp: (85) 99936-2255</p>
            </div>
            <p class="copyright">&copy; 2026 Empório Linneo. Tradição & Sabor.</p>
        </div>
    </footer>

    <!-- Fixed Bottom Bar -->
    <div class="sticky-footer-bar">
        <div class="container footer-fixed-flex">
            <div class="footer-fixed-left">
                <img src="avatar.jpg" alt="Padeiro" class="sticky-avatar">
                <div class="footer-fixed-text">
                    <span class="ff-title">Fornada saindo agora!</span>
                    <span class="ff-sub">Fale com nosso mestre padeiro.</span>
                </div>
            </div>
            <div class="footer-fixed-right">
                <a href="https://wa.me/5585999362255" target="_blank" class="btn-footer-wa">
                    Fazer Pedido
                </a>
            </div>
        </div>
    </div>"""

html = html.replace(old_footer, new_footers)

with open("emporio-linneo/index.html", "w", encoding="utf-8") as f:
    f.write(html)


with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace css
old_css_footer = """/* Fixed Footer (Orkes Concept) */
.classic-footer-fixed {"""

new_css_footer = """/* Regular Footer */
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
}

/* Fixed Bottom Bar */
.sticky-footer-bar {"""

css = css.replace(old_css_footer, new_css_footer)

avatar_css = """
.sticky-avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid var(--primary);
}
"""
css += avatar_css

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Both footers applied.")
