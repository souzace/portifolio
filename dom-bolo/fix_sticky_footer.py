import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the sticky footer HTML block
new_sticky_html = """<div class="sticky-footer-bar">
    <p>Gostou dos nossos bolos? Faça sua encomenda agora mesmo!</p>
    <div style="display: flex; align-items: center; gap: 15px;">
        <a href="https://wa.me/5585900000000" target="_blank" class="sticky-btn">Pedir no WhatsApp</a>
        <a href="https://www.instagram.com/dombolofortal/" target="_blank" class="social-icon" aria-label="Instagram">
            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
            </svg>
        </a>
    </div>
</div>"""

html = re.sub(r'<div class="sticky-footer-bar">.*?</div>', new_sticky_html, html, flags=re.DOTALL)

# Add CSS for the social icon hover effect if not exists
if '.social-icon {' not in html:
    css_injection = """
        .social-icon {
            color: #fff;
            transition: color 0.3s;
            display: flex;
        }
        .social-icon:hover {
            color: var(--brand-orange);
        }
"""
    html = html.replace("</style>", css_injection + "</style>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Sticky footer fixed.")
