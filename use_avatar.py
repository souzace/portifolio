import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix the sticky footer avatar to use the properly cropped avatar.jpg
old_avatar = """<div style="width: 50px; height: 50px; border-radius: 50%; overflow: hidden; border: 2px solid var(--brand-gold); flex-shrink: 0; display: inline-block;">
            <img src="photo5.jpg" alt="Nilson Vieira" style="width: 100%; height: 100%; object-fit: cover; object-position: 15% 30%; transform: scale(2.5);">
        </div>"""

new_avatar = """<div style="width: 50px; height: 50px; border-radius: 50%; overflow: hidden; border: 2px solid var(--brand-gold); flex-shrink: 0; display: inline-block;">
            <img src="avatar.jpg" alt="Nilson Vieira" style="width: 100%; height: 100%; object-fit: cover; object-position: center;">
        </div>"""

html = html.replace(old_avatar, new_avatar)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Avatar updated in HTML.")
