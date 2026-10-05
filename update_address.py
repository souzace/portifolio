import re

with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace address
old_addr = "📍 Rua das Araucárias, 1250 - Bairro Nobre"
new_addr = "📍 Av. Lineu Machado, 875 - Jóquei Clube, Fortaleza - CE, 60520-101"

html = html.replace(old_addr, new_addr)

with open("emporio-linneo/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Address updated.")
