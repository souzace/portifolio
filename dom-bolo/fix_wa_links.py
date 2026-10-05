import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the hero CTA button href
html = re.sub(
    r'<a href="https://www\.instagram\.com/dombolofortal/" target="_blank" class="cta-btn">(.*?)Faça sua Encomenda</a>',
    r'<a href="https://wa.me/5585999999999" target="_blank" class="cta-btn">\1Faça sua Encomenda</a>',
    html
)

# Replace the standard footer CTA button href
html = re.sub(
    r'<a href="https://www\.instagram\.com/dombolofortal/" target="_blank" class="cta-btn" style="padding: 0\.8rem 2rem; display: inline-block;">(.*?)Falar no WhatsApp</a>',
    r'<a href="https://wa.me/5585999999999" target="_blank" class="cta-btn" style="padding: 0.8rem 2rem; display: inline-block;">\1Falar no WhatsApp</a>',
    html
)

# Replace the sticky footer CTA button href if it's still instagram (should be wa.me but just in case)
html = re.sub(
    r'<a href="https://www\.instagram\.com/dombolofortal/" target="_blank" class="sticky-btn">(.*?)Pedir no WhatsApp</a>',
    r'<a href="https://wa.me/5585999999999" target="_blank" class="sticky-btn">\1Pedir no WhatsApp</a>',
    html
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("WhatsApp links fixed.")
