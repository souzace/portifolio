with open("kuroneko-toys/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Adicionar favicon no <head>
if 'rel="icon"' not in html:
    html = html.replace('<link rel="stylesheet" href="style.css">', '<link rel="icon" type="image/png" href="favicon.png">\n    <link rel="shortcut icon" href="favicon.ico">\n    <link rel="stylesheet" href="style.css">')

# 2. Restaurar a versão anterior na Hero com mais espaço vertical (o card vertical da loja)
# Vamos manter a arte oficial vertical da loja e o gato com o enquadramento equilibrado
with open("kuroneko-toys/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("kuroneko-toys/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Ajustar o poster frame da hero para dar bastante respiro e verticalidade
css = css.replace('max-width: 420px;', 'max-width: 380px;')

with open("kuroneko-toys/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Favicon do gato e proporção vertical ajustados com sucesso!")
