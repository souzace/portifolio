with open("kuroneko-toys/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Substituir o texto estático dos créditos pelo link para orkes.com.br
html = html.replace(
    '<p class="orkes-credits">Desenvolvido por Orkes</p>',
    '<p class="orkes-credits">Desenvolvido por <a href="https://orkes.com.br" target="_blank" rel="noopener noreferrer" class="orkes-link">Orkes</a></p>'
)

with open("kuroneko-toys/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("kuroneko-toys/style.css", "r", encoding="utf-8") as f:
    css = f.read()

css += """
.orkes-link {
    color: var(--kuro-orange);
    text-decoration: none;
    font-weight: 800;
    transition: color 0.2s, text-shadow 0.2s;
}

.orkes-link:hover {
    color: #fff;
    text-shadow: 0 0 10px var(--kuro-orange);
}
"""

with open("kuroneko-toys/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Link oficial da Orkes adicionado com sucesso!")
