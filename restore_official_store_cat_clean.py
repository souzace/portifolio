import re
import time

version = str(int(time.time()))

with open("kuroneko-toys/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Na Hero Section, usar EXATAMENTE official_store_cat.jpg (a arte limpa sem botões na frente)
html = re.sub(
    r'<div class="cat-poster-frame">\s*<img src="[^"]+" alt="Kuro Neko Toys Store Oficial"[^>]*>',
    f'<div class="cat-poster-frame">\n                    <img src="official_store_cat.jpg?v={version}" alt="Kuro Neko Toys Store Oficial" class="cat-official-art">',
    html
)

with open("kuroneko-toys/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("kuroneko-toys/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# O poster vertical com a arte limpa da loja deve ter a largura perfeita
css = css.replace('max-width: 330px;', 'max-width: 400px;')

with open("kuroneko-toys/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Restaurada a imagem oficial_store_cat.jpg (o background limpo com o gato no telefone sem os botões)!")
