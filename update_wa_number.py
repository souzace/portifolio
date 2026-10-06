with open("alo-agua/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Substituir o número placeholder 5585999999999 pelo número real 5585987482802
html = html.replace('5585999999999', '5585987482802')

with open("alo-agua/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Número do WhatsApp atualizado em todos os botões e links!")
