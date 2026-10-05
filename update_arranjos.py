import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Replace the "Arranjos Musicais" image
html = re.sub(
    r'<img src="photo1\.jpg" alt="Arranjos Musicais">',
    r'<img src="sheet_music.jpg" alt="Arranjos Musicais" style="object-position: center;">',
    html
)

# 2. Add the avatar to the sticky footer
avatar_html = """<div style="display: flex; align-items: center; gap: 15px; margin-right: 20px;">
        <img src="photo2.jpg" alt="Nilson Vieira" style="width: 50px; height: 50px; border-radius: 50%; object-fit: cover; object-position: center 20%; border: 2px solid var(--brand-gold);">
        <p style="margin: 0; color: #fff; font-family: sans-serif; font-size: 0.9rem;">Gostou do meu trabalho? Vamos conversar!</p>
    </div>"""

# Replace the existing sticky footer <p> with the flex container
html = re.sub(
    r'<p>Gostou do meu trabalho\? Vamos conversar!</p>',
    avatar_html,
    html
)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updates applied.")
