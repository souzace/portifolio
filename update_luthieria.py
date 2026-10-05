import re

with open("luthieria/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Logo in Header
new_logo = """<div class="logo">Belu<span class="logo-ton">ton</span><br><span class="logo-sub">Luthieria</span></div>"""
html = re.sub(r'<div class="logo">Luthieria<span>Sopros</span></div>', new_logo, html)

# 2. Add Sticky Footer
sticky_html = """
    <!-- Sticky Footer CTA -->
    <div class="sticky-footer-bar">
        <div class="sticky-footer-container">
            <div class="sticky-left">
                <img src="welligthon.jpg" alt="Welligthon - Luthier" class="sticky-avatar">
                <div class="sticky-text">
                    <span class="sticky-title">Fale com o Welligthon</span>
                    <span class="sticky-subtitle">Avaliação gratuita pelo WhatsApp</span>
                </div>
            </div>
            <div class="sticky-right">
                <a href="https://www.instagram.com/" target="_blank" class="sticky-social-icon" aria-label="Instagram">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                </a>
                <a href="https://wa.me/" target="_blank" class="sticky-wa-btn">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                    Fazer Orçamento
                </a>
            </div>
        </div>
    </div>
"""

# Insert right before </body>
html = html.replace('</body>', sticky_html + '\n</body>')

with open("luthieria/index.html", "w", encoding="utf-8") as f:
    f.write(html)

# Update CSS
with open("luthieria/style.css", "r", encoding="utf-8") as f:
    css = f.read()

new_logo_css = """
/* Custom Logo Styling */
.logo {
    font-size: 1.8rem;
    font-weight: 400;
    color: var(--text-light);
    line-height: 1;
    letter-spacing: 1px;
}
.logo-ton {
    color: var(--gold);
    font-weight: 700;
    font-style: normal;
}
.logo-sub {
    font-family: 'Raleway', sans-serif;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 4px;
    color: var(--text-muted);
}
"""

css = css.replace('.logo span {\n    color: var(--gold);\n    font-style: italic;\n}', new_logo_css)

sticky_css = """
/* Sticky Footer CTA */
body {
    padding-bottom: 80px;
}
.sticky-footer-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: rgba(10, 10, 10, 0.98);
    border-top: 1px solid rgba(212, 175, 55, 0.2);
    color: var(--text-light);
    padding: 0.8rem 1rem;
    box-shadow: 0 -5px 20px rgba(0,0,0,0.5);
    z-index: 1000;
}
.sticky-footer-container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.sticky-left {
    display: flex;
    align-items: center;
    gap: 12px;
}
.sticky-avatar {
    width: 45px;
    height: 45px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid var(--gold);
}
.sticky-text {
    display: flex;
    flex-direction: column;
}
.sticky-title {
    font-family: 'Raleway', sans-serif;
    font-weight: 600;
    font-size: 0.95rem;
    line-height: 1.2;
    color: var(--text-light);
}
.sticky-subtitle {
    font-family: 'Raleway', sans-serif;
    font-size: 0.8rem;
    color: var(--text-muted);
}
.sticky-right {
    display: flex;
    align-items: center;
    gap: 15px;
}
.sticky-social-icon {
    color: var(--text-light);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: color 0.3s ease;
}
.sticky-social-icon:hover {
    color: var(--gold);
}
.sticky-wa-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background-color: transparent;
    border: 1px solid var(--gold);
    color: var(--gold);
    text-decoration: none;
    padding: 0.6rem 1.2rem;
    border-radius: 4px;
    font-weight: 600;
    font-family: 'Raleway', sans-serif;
    font-size: 0.9rem;
    transition: all 0.3s ease;
}
.sticky-wa-btn:hover {
    background-color: var(--gold);
    color: var(--bg-dark);
}

@media(max-width: 599px) {
    .sticky-footer-container {
        flex-direction: column;
        gap: 12px;
    }
    .sticky-right {
        width: 100%;
        justify-content: space-between;
    }
    .sticky-wa-btn {
        flex: 1;
        justify-content: center;
    }
}
"""

css += sticky_css

with open("luthieria/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Logo and sticky footer added.")
