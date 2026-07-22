import os

files = [
    ('index.html', 'Falar com o Especialista', 'Falar comigo'),
    ('index-en.html', 'Talk to the Expert', 'Talk with me'),
    ('index-es.html', 'Hablar con el Experto', 'Hablar conmigo')
]

for filename, old_text, new_text in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace all occurrences
    content = content.replace(old_text, new_text)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("CTA text changed to 'Talk with me' globally!")
