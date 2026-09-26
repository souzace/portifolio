import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

new_footer = """<footer>
    <div style="margin-bottom: 2rem;">
        <h2 style="color: var(--brand-orange); margin-bottom: 1rem;">Gostou? Peça o seu!</h2>
        <a href="https://www.instagram.com/dombolofortal/" target="_blank" class="cta-btn" style="padding: 0.8rem 2rem; display: inline-block;">Falar no WhatsApp</a>
    </div>
    <div style="margin-bottom: 1.5rem;">
        <p>Acompanhe nossas fornadas: <a href="https://www.instagram.com/dombolofortal/" target="_blank">@dombolofortal</a></p>
    </div>
    <div style="font-size: 0.9rem; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 1.5rem; margin-top: 2rem;">
        <p>&copy; 2026 Dom Bolo. Todos os direitos reservados.</p>
        <p style="margin-top: 0.5rem; font-size: 0.8rem; color: #aaa;">Desenvolvido por <a href="https://orkes.com.br" target="_blank" style="color: #aaa; text-decoration: underline;">Orkes</a></p>
    </div>
</footer>"""

html = re.sub(r'<footer>.*?</footer>', new_footer, html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Footer updated!")
