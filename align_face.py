import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix the sticky footer avatar alignment
old_avatar = '<img src="avatar.jpg" alt="Nilson Vieira" style="width: 100%; height: 100%; object-fit: cover; object-position: center;">'
new_avatar = '<img src="avatar.jpg" alt="Nilson Vieira" style="width: 100%; height: 100%; object-fit: cover; object-position: 90% 30%; transform: scale(1.8);">'

html = html.replace(old_avatar, new_avatar)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Avatar aligned.")
