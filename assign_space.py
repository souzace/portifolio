import re

with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

old_historia_img = """.historia-img {
    height: 400px;
    background-color: #4a2c20;
    border-radius: 8px;
    border: 2px solid var(--primary);
}"""

new_historia_img = """.historia-img {
    height: 400px;
    background: url('space.png') no-repeat center center/cover;
    border-radius: 8px;
    border: 2px solid var(--primary);
}"""

css = css.replace(old_historia_img, new_historia_img)

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Space image assigned.")
