import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Realign the Regência card image
html = re.sub(
    r'<img src="photo5\.jpg" alt="Regência de Orquestras" style="object-position: top;">',
    r'<img src="photo5.jpg" alt="Regência de Orquestras" style="object-position: 15% 30%;">',
    html
)

# Replace the sticky footer avatar from photo2 to photo5 with a zoom
old_avatar = '<img src="photo2.jpg" alt="Nilson Vieira" style="width: 50px; height: 50px; border-radius: 50%; object-fit: cover; object-position: center 20%; border: 2px solid var(--brand-gold);">'
# Using a scale to zoom in on his face, which is near the top left of photo5
new_avatar = '<img src="photo5.jpg" alt="Nilson Vieira" style="width: 50px; height: 50px; border-radius: 50%; object-fit: cover; object-position: 15% 30%; transform: scale(1.8); clip-path: circle(50% at 50% 50%); border: 2px solid var(--brand-gold);">'
html = html.replace(old_avatar, new_avatar)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Positions fixed.")
