import re
import time

version = str(int(time.time()))

with open("kuroneko-toys/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Colocar o carrd_card.jpg com cache buster na Hero na linha 98
html = re.sub(
    r'<div class="cat-poster-frame">\s*<img src="[^"]+" alt="Kuro Neko Toys Store Oficial"[^>]*>',
    f'<div class="cat-poster-frame">\n                    <img src="carrd_card.jpg?v={version}" alt="Kuro Neko Toys Store Oficial" class="cat-official-art">',
    html
)

# 2. Adicionar cache buster em todas as imagens do kuroneko-toys/index.html para forçar recarregamento instantâneo do navegador
html = re.sub(r'src="official_avatar_fb\.jpg(\?v=[0-9]+)?"', f'src="official_avatar_fb.jpg?v={version}"', html)
html = re.sub(r'src="cat_head_phone\.jpg(\?v=[0-9]+)?"', f'src="cat_head_phone.jpg?v={version}"', html)
html = re.sub(r'href="favicon\.png(\?v=[0-9]+)?"', f'href="favicon.png?v={version}"', html)
html = re.sub(r'href="favicon\.ico(\?v=[0-9]+)?"', f'href="favicon.ico?v={version}"', html)

with open("kuroneko-toys/index.html", "w", encoding="utf-8") as f:
    f.write(html)

# 3. Atualizar também no cache_buster.py geral para incluir quebra de cache de imagens além de CSS
with open("cache_buster.py", "r", encoding="utf-8") as f:
    cb = f.read()

# Adicionar quebra de cache para imagens em index.html
if 'img_pattern' not in cb:
    img_cb = """        # Quebrar cache de imagens principais
        img_pattern = r'src="([^"]+\\.(jpg|png|webp))(\\?v=[0-9.]+)?([^"]*)"'
        content = re.sub(img_pattern, f'src="\\\\1?v={version}\\\\4"', content)
"""
    cb = cb.replace('new_content = re.sub(pattern, f\'href="\\\\1?v={version}\\\\3"\', content)', 'new_content = re.sub(pattern, f\'href="\\\\1?v={version}\\\\3"\', content)\n' + img_cb)

    with open("cache_buster.py", "w", encoding="utf-8") as f:
        f.write(cb)

print("Imagens com cache-buster configuradas e carrd_card.jpg garantido na Hero!")
