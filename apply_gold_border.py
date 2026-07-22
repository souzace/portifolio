import os

files = ['index.html', 'index-en.html', 'index-es.html']

old_border = 'border: 2px solid var(--cyan-accent);'
new_border = 'border: 2px solid #D4AF37; box-shadow: 0 0 8px rgba(212, 175, 55, 0.4);'

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We only want to replace it for the sticky footer avatar
    # So we'll look for the specific img tag to be safe, but since old_border only appears here in this context,
    # wait, the carousel buttons also had some cyan borders. Let's be specific to the img tag.
    
    target_img = '<img src="foto8.jpg" alt="Avatar" style="width: 48px; height: 48px; border-radius: 50%; object-fit: cover; object-position: center 20%; border: 2px solid var(--cyan-accent);">'
    replacement_img = f'<img src="foto8.jpg" alt="Avatar" style="width: 48px; height: 48px; border-radius: 50%; object-fit: cover; object-position: center 20%; {new_border}">'
    
    content = content.replace(target_img, replacement_img)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Gold border applied to avatar successfully!")
