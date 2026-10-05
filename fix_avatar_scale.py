import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix the avatar scaling using transform and background color instead of ffmpeg padding
old_wrapper = '<div style="width: 50px; height: 50px; border-radius: 50%; overflow: hidden; border: 2px solid var(--brand-gold); flex-shrink: 0; display: inline-block;">\n            <img src="avatar.png" alt="Nilson Vieira" style="width: 100%; height: 100%; object-fit: cover; object-position: center 15%;">'

new_wrapper = '<div style="width: 50px; height: 50px; border-radius: 50%; overflow: hidden; border: 2px solid var(--brand-gold); flex-shrink: 0; display: inline-block; background-color: #f1f2f4;">\n            <img src="avatar.png" alt="Nilson Vieira" style="width: 100%; height: 100%; object-fit: cover; object-position: center 15%; transform: scale(0.85);">'

html = html.replace(old_wrapper, new_wrapper)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Avatar scaled down.")
