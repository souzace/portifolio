import os

files = [
    ('index.html', 'Orkes® - CNPJ: 41.950.774/0001-60', 'Orkes® - Marca registrada INPI 917789873'),
    ('index-en.html', 'Orkes® - CNPJ: 41.950.774/0001-60', 'Orkes® - Registered Trademark INPI 917789873'),
    ('index-es.html', 'Orkes® - CNPJ: 41.950.774/0001-60', 'Orkes® - Marca registrada INPI 917789873')
]

for filename, old_text, new_text in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace(old_text, new_text)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("CNPJ replaced with INPI successfully!")
