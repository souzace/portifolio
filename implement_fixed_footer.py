import re

with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the footer HTML
old_footer = """    <footer id="contato" class="classic-footer">
        <div class="container">
            <img src="logomark.jpg" alt="Logo" class="footer-logo-classic">
            <div class="footer-contact-info">
                <p>📍 Av. Lineu Machado, 875 - Jóquei Clube, Fortaleza - CE</p>
                <p>🕒 Aberto todos os dias das 06h às 21h</p>
                <p>📞 WhatsApp: (85) 99936-2255</p>
            </div>
            <p class="copyright">&copy; 2026 Empório Linneo. Tradição & Sabor.</p>
        </div>
    </footer>"""

new_footer = """    <footer id="contato" class="classic-footer-fixed">
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

html = html.replace(old_footer, new_footer)

# Also remove the FAB since the fixed footer has the CTA
html = re.sub(r'<!-- FAB -->.*?</a>', '', html, flags=re.DOTALL)

with open("emporio-linneo/index.html", "w", encoding="utf-8") as f:
    f.write(html)


with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add padding to body to prevent overlap
if "body {" in css:
    css = css.replace("body {", "body {\n    padding-bottom: 80px;")

# Replace footer CSS
old_css_footer = """/* Formal Footer */
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
}"""

new_css_footer = """/* Fixed Footer (Orkes Concept) */
.classic-footer-fixed {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #1a0e0a;
    border-top: 2px solid var(--primary);
    padding: 12px 0;
    z-index: 1000;
    box-shadow: 0 -10px 30px rgba(0,0,0,0.5);
}
.footer-fixed-flex {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 2rem;
}
.footer-fixed-left {
    display: flex;
    align-items: center;
    gap: 16px;
}
.footer-fixed-text {
    display: flex;
    flex-direction: column;
}
.ff-title {
    color: var(--primary);
    font-family: 'Lora', serif;
    font-size: 1.2rem;
    font-weight: bold;
}
.ff-sub {
    color: rgba(249, 243, 233, 0.6);
    font-size: 0.85rem;
}
.btn-footer-wa {
    background-color: #25D366;
    color: #fff;
    padding: 10px 24px;
    border-radius: 4px;
    text-decoration: none;
    font-weight: bold;
    text-transform: uppercase;
    font-size: 0.9rem;
    letter-spacing: 1px;
    transition: background 0.3s;
}
.btn-footer-wa:hover {
    background-color: #1ebd5a;
}

@media (max-width: 768px) {
    .footer-fixed-flex {
        flex-direction: column;
        gap: 10px;
        text-align: center;
    }
    .btn-footer-wa {
        width: 100%;
        text-align: center;
    }
    body { padding-bottom: 120px; }
}"""

css = css.replace(old_css_footer, new_css_footer)

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed footer applied.")
