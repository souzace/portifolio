with open("alo-agua/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Substituir o logo do conceito 1 pelo conceito 2
html = html.replace('src="logo_conceito1.jpg"', 'src="logo_conceito2.jpg"')

with open("alo-agua/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Conceito 2 aplicado em alo-agua/index.html.")
