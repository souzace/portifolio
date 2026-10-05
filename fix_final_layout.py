import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Contact section: Remove social icons if they exist, ensure ONE green button below text.
# The current HTML has:
# <h2 ...>Vamos criar música juntos?</h2>
# <p>Para convites...</p>
# <div style="margin: 2rem 0;">
#    <a href="..." class="body-wa-btn">...FALAR NO WHATSAPP</a>
# </div>
# (and maybe the old social-links div if it's still there)
# Let's cleanly rebuild the inner content of <footer id="contato">
wa_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>'
new_contato_content = f"""
    <div style="max-width: 800px; margin: 0 auto; text-align: left;">
        <h2 style="color: var(--brand-gold); margin-bottom: 1rem; font-family: 'Georgia', serif;">Vamos criar música juntos?</h2>
        <p style="margin-bottom: 2rem;">Para convites de regência, encomendas de arranjos ou parcerias musicais.</p>
        
        <div style="margin: 2rem 0;">
            <a href="https://wa.me/558597496713" target="_blank" class="body-wa-btn">
                {wa_svg} FALAR NO WHATSAPP
            </a>
        </div>

        <p style="margin-top: 4rem; font-size: 0.85rem; text-align: center;">&copy; 2026 Nilson Vieira. Todos os direitos reservados.</p>
        <p style="margin-top: 0.5rem; font-size: 0.75rem; color: #666; text-align: center;">Desenvolvido por <a href="https://orkes.com.br" target="_blank" style="color: #666; text-decoration: underline;">Orkes</a></p>
    </div>
"""

# Replace everything inside <footer id="contato"> ... </footer>
html = re.sub(r'<footer id="contato".*?>.*?</footer>', f'<footer id="contato" style="padding: 5rem 2rem; background-color: var(--brand-dark); border-top: 1px solid rgba(212, 175, 55, 0.2);">{new_contato_content}</footer>', html, flags=re.DOTALL)


# 2. Sticky Footer: Remove Avatar and Text! Keep only the bottom row, aligned right.
# Current sticky footer HTML:
# <div class="sticky-footer-bar">
#    <div class="sticky-text-group"...>...</div>
#    <div class="sticky-bottom-row">...</div>
# </div>
html = re.sub(r'<div class="sticky-text-group".*?</div>\s*<div class="sticky-bottom-row">', '<div class="sticky-bottom-row" style="width: 100%; justify-content: flex-end;">', html, flags=re.DOTALL)

# Ensure the sticky footer bar itself doesn't have weird padding/gaps meant for the top row
html = html.replace('flex-direction: column;', '') # Remove column stacking since there's only one row now
# We'll just let CSS handle it. 

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Layout updated perfectly.")
