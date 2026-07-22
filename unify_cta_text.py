import os

files = [
    ('index.html', 'Entrar em Contato', 'Falar com o Especialista'),
    ('index-en.html', 'Get in Touch', 'Talk to the Expert'),
    ('index-es.html', 'Ponerse en Contacto', 'Hablar con el Experto')
]

for filename, old_text, new_text in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # We just replace the exact text in the file.
    # It appears exactly in the footer CTA.
    content = content.replace(old_text, new_text)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("CTA text unified successfully!")
