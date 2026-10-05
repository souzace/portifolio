import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Update the Hero paragraph
old_hero_p = "<p>O autêntico sabor de casa. Bolos caseiros com produção diária, feitos com afeto e ingredientes selecionados para o seu café da tarde.</p>"
new_hero_p = "<p>🤗 Sabor que abraça. <br>👨‍🍳 Produção Diária de bolos caseiros, feitos com afeto para o seu café da tarde.</p>"
html = html.replace(old_hero_p, new_hero_p)

# Add the location address to the standard footer
old_footer_social = '<div style="margin-bottom: 1.5rem;">\n        <p>Acompanhe nossas fornadas: <a href="https://www.instagram.com/dombolofortal/" target="_blank">@dombolofortal</a></p>\n    </div>'
new_footer_social = """<div style="margin-bottom: 1.5rem; line-height: 1.8;">
        <p>📍 <strong>Jóquei Clube</strong> (Prox. ao North Shopping Jóquei)<br>Av Lineu Machado 768, Fortaleza, CE - 60520-102</p>
        <p style="margin-top: 1rem;">Acompanhe nossas fornadas: <a href="https://www.instagram.com/dombolofortal/" target="_blank">@dombolofortal</a></p>
    </div>"""

html = html.replace(old_footer_social, new_footer_social)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Bio texts added.")
