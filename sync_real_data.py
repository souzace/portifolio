with open("kuroneko-toys/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Substituir o número placeholder pelo WhatsApp oficial do Carrd
html = html.replace('5585999999999', '558592828087')

with open("kuroneko-toys/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("WhatsApp oficial sincronizado em todos os botões do Kuro Neko Toys!")
