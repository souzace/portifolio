import re

with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add Hamburger toggle and Mobile overlay to Header
header_start = '<header class="hybrid-header">\n        <div class="container classic-nav-container">'
new_header_start = """<header class="hybrid-header">
        <div class="container classic-nav-container">
            <button class="mobile-menu-toggle" aria-label="Abrir menu">
                <svg viewBox="0 0 24 24" width="28" height="28" stroke="var(--primary)" stroke-width="2" fill="none"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
            </button>
            
            <nav class="mobile-nav-overlay">
                <button class="mobile-menu-close" aria-label="Fechar menu">&times;</button>
                <a href="#cardapio" class="mobile-link">Cardápio</a>
                <a href="#historia" class="mobile-link">Nossa Arte</a>
                <a href="#contato" class="mobile-link">Contato</a>
                <a href="https://wa.me/5585999362255" class="mobile-link highlight">Fazer Pedido</a>
            </nav>"""
html = html.replace(header_start, new_header_start)

# Alter Sticky Footer content for Mobile
# We will change "Fazer Pedido" to just "Pedir" on small screens using a span class
btn_wa = "Fazer Pedido"
new_btn_wa = '<span class="hide-mobile">Fazer Pedido</span><span class="show-mobile">Pedir</span>'
html = html.replace(btn_wa, new_btn_wa)

# Add JS script before </body>
js_code = """
    <script>
        const toggleBtn = document.querySelector('.mobile-menu-toggle');
        const closeBtn = document.querySelector('.mobile-menu-close');
        const overlay = document.querySelector('.mobile-nav-overlay');
        const links = document.querySelectorAll('.mobile-link');

        if(toggleBtn && overlay) {
            toggleBtn.addEventListener('click', () => overlay.classList.add('active'));
            closeBtn.addEventListener('click', () => overlay.classList.remove('active'));
            links.forEach(link => link.addEventListener('click', () => overlay.classList.remove('active')));
        }
    </script>
</body>"""
html = html.replace("</body>", js_code)

with open("emporio-linneo/index.html", "w", encoding="utf-8") as f:
    f.write(html)

# CSS Updates
with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add Mobile CSS Fixes
mobile_css = """
/* Hamburger & Mobile Menu Base */
.mobile-menu-toggle { display: none; background: none; border: none; cursor: pointer; padding: 5px; z-index: 1001; position: absolute; left: 1rem; }
.mobile-nav-overlay {
    position: fixed; top: 0; left: -100%; width: 80%; max-width: 300px; height: 100vh;
    background-color: var(--bg-dark); z-index: 2000;
    display: flex; flex-direction: column; padding: 4rem 2rem;
    transition: left 0.3s ease;
    box-shadow: 2px 0 20px rgba(0,0,0,0.5);
}
.mobile-nav-overlay.active { left: 0; }
.mobile-menu-close {
    position: absolute; top: 1rem; right: 1rem; background: none; border: none;
    color: var(--primary); font-size: 2.5rem; cursor: pointer;
}
.mobile-link {
    color: var(--bg-light); text-decoration: none; font-size: 1.2rem;
    padding: 1rem 0; border-bottom: 1px solid rgba(212, 175, 55, 0.1);
    font-family: 'Outfit', sans-serif; text-transform: uppercase;
}
.mobile-link.highlight { color: var(--primary); font-weight: bold; border: none; margin-top: 1rem; }

.show-mobile { display: none; }

@media (max-width: 992px) {
    .mobile-menu-toggle { display: block; }
    .logo-hybrid { width: 90px; height: 90px; margin: 0 auto; }
    .hybrid-header { justify-content: center; position: fixed; }
    .hero-content-center h1 { font-size: 2.5rem; }
    
    /* Smart Bar Fixes */
    .footer-fixed-flex {
        flex-direction: row !important;
        gap: 10px;
        padding: 0 1rem !important;
        text-align: left !important;
    }
    .footer-fixed-left { gap: 10px !important; }
    .sticky-avatar { width: 40px !important; height: 40px !important; }
    .ff-title { font-size: 1rem !important; }
    .ff-sub { display: none; /* Hide subtitle to save vertical space */ }
    
    .btn-footer-wa { padding: 8px 16px !important; font-size: 0.8rem !important; }
    .hide-mobile { display: none; }
    .show-mobile { display: inline; }
    
    .footer-socials { display: none !important; /* hide insta on mobile sticky bar to save space */ }
    
    body { padding-bottom: 80px !important; } /* Restore body padding */
}
"""

css += mobile_css

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Mobile UX fixes applied.")
