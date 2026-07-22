import os

en_file = 'index-en.html'
es_file = 'index-es.html'

old_title = 'title="Instituto Nacional da Propriedade Industrial - Brasil"'
en_title = 'title="National Institute of Industrial Property - Brazil"'
es_title = 'title="Instituto Nacional de la Propiedad Industrial - Brasil"'

# Update English
with open(en_file, 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace(old_title, en_title)
with open(en_file, 'w', encoding='utf-8') as f:
    f.write(content)

# Update Spanish
with open(es_file, 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace(old_title, es_title)
with open(es_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Tooltips translated successfully!")
