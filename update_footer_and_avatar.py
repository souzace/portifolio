with open("alo-agua/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remover logo do footer tradicional e centralizar o conteúdo
old_footer = """    <!-- Footer Tradicional -->
    <footer class="footer">
        <div class="container footer-container">
            <div class="footer-brand">
                <img src="mascotes_puros.jpg" alt="Alô Água" class="footer-logo">
                <p>Alô Água & Gás — O delivery de confiança da sua família no Conjunto Ceará.</p>
            </div>
            <div class="footer-info">
                <p>📍 Conjunto Ceará, Fortaleza - CE</p>
                <p>🕒 Segunda a Sábado: 07h às 19h | Domingo: 07h às 13h</p>
                <p class="orkes-credits">Desenvolvido por Orkes</p>
            </div>
        </div>
    </footer>"""

new_footer = """    <!-- Footer Tradicional -->
    <footer class="footer">
        <div class="container footer-container-center">
            <p class="footer-tagline">Alô Água & Gás — O delivery de confiança da sua família no Conjunto Ceará.</p>
            <p class="footer-address">📍 Conjunto Ceará, Fortaleza - CE</p>
            <p class="footer-hours">🕒 Segunda a Sábado: 07h às 19h | Domingo: 07h às 13h</p>
            <p class="orkes-credits">Desenvolvido por Orkes</p>
        </div>
    </footer>"""

html = html.replace(old_footer, new_footer)

# 2. No fixed footer, mudar o avatar para avatar.jpg
html = html.replace('<img src="mascotes_puros.jpg" alt="Mascote Alô Água" class="sticky-avatar">', '<img src="avatar.jpg" alt="Atendente Alô Água" class="sticky-avatar">')

with open("alo-agua/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("alo-agua/style.css", "r", encoding="utf-8") as f:
    css = f.read()

css += """
/* Centralização do Footer Tradicional */
.footer-container-center {
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.6rem;
}
.footer-tagline {
    font-size: 1rem;
    color: #fff;
    font-weight: 600;
}
.footer-address, .footer-hours {
    font-size: 0.9rem;
    color: #94A3B8;
}
.sticky-avatar {
    object-fit: cover !important;
}
"""

with open("alo-agua/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Footer e Avatar atualizados com sucesso.")
