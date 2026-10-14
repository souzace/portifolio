with open("kuroneko-toys/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Substituir official_store_cat.jpg por carrd_card.jpg na Hero Section
html = html.replace('src="official_store_cat.jpg"', 'src="carrd_card.jpg"')

with open("kuroneko-toys/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Imagem do card vertical da Hero substituída exatamente pelo carrd_card.jpg original!")
