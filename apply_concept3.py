with open("alo-agua/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Substituir o logo do conceito 2 pelo conceito 3
html = html.replace('src="logo_conceito2.jpg"', 'src="logo_conceito3.jpg"')

with open("alo-agua/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Conceito 3 aplicado em alo-agua/index.html.")
