with open("alo-agua/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Substituir o texto do subtítulo da barra fixa
old_text = '<span class="st-sub">Entrega expressa no Conjunto Ceará!</span>'
new_text = '<span class="st-sub">Entrega expressa no Conjunto Ceará e Adjacências</span>'

html = html.replace(old_text, new_text)

with open("alo-agua/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Texto atualizado com sucesso.")
