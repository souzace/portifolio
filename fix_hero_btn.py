import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

old_cta_css = re.search(r'\.cta-btn \{.*?\}', html, re.DOTALL).group(0)
new_cta_css = """.cta-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            padding: 1rem 2.5rem;
            background-color: var(--brand-gold);
            color: var(--brand-dark);
            text-decoration: none;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-weight: bold;
            border-radius: 5px;
            margin-top: 2rem;
            transition: all 0.3s ease;
        }"""
html = html.replace(old_cta_css, new_cta_css)

old_cta_hover = re.search(r'\.cta-btn:hover \{.*?\}', html, re.DOTALL).group(0)
new_cta_hover = """.cta-btn:hover {
            background-color: #f7d154;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
        }"""
html = html.replace(old_cta_hover, new_cta_hover)

# Update HTML to point directly to WhatsApp and add the icon
wa_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>'
html = html.replace('<a href="#contato" class="cta-btn">Entre em Contato</a>', f'<a href="https://wa.me/558597496713" target="_blank" class="cta-btn">{wa_svg} Entre em Contato</a>')

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("CTA button updated.")
