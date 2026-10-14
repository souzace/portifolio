import re
import time

version = str(int(time.time()))

with open("kuroneko-toys/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Substituir a imagem da hero por carrd_inner_phone_card.jpg
html = re.sub(r'src="carrd_card\.jpg(\?v=[0-9]+)?"', f'src="carrd_inner_phone_card.jpg?v={version}"', html)

with open("kuroneko-toys/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("kuroneko-toys/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Ajustar o frame do poster para o formato do smartphone/card vertical esbelto
css = css.replace('max-width: 440px;', 'max-width: 330px;')

with open("kuroneko-toys/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Card vertical exato do Carrd aplicado!")
