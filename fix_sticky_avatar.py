with open("alo-agua/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Substituir diretamente a linha 196
html = html.replace('<img src="mascotes_puros.jpg" alt="Novo Logotipo Alô Água" class="sticky-avatar">', '<img src="avatar.jpg" alt="Atendente Alô Água" class="sticky-avatar">')

with open("alo-agua/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Avatar substituído com sucesso por avatar.jpg!")
