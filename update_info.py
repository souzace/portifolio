import re

with open("el-bethel/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Update WhatsApp links
html = html.replace('https://wa.me/5585999999999', 'https://api.whatsapp.com/send?phone=5585988236302')

# Update Address
old_address = 'Rua Exemplo, 123 - Centro<br>Sua Cidade - Estado'
new_address = 'Av. Ministro Albuquerque Lima, 163 - Lj C<br>Conj. Ceará, Fortaleza - CE, Brasil'
html = html.replace(old_address, new_address)

# Update Hours
old_hours = 'Seg - Sex: 08:00 às 18:00<br>Sáb: 08:00 às 13:00'
new_hours = 'Segunda a sexta: 08h às 18h<br>Sábado: 08h às 12h'
html = html.replace(old_hours, new_hours)

# Update Maps link (Como Chegar)
maps_url = 'https://www.google.com/maps/search/?api=1&query=Av.+Ministro+Albuquerque+Lima,+163+-+Conj.+Ceará,+Fortaleza'
html = html.replace('<a href="#" class="btn-outline">Como Chegar</a>', f'<a href="{maps_url}" target="_blank" class="btn-outline">Como Chegar</a>')


with open("el-bethel/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Informations updated.")
