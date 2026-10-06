import re

with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Slow down carousel even more
css = css.replace("animation: scroll-marquee 45s linear infinite;", "animation: scroll-marquee 70s linear infinite;")

# Increase logo size
old_logo = """.logo-hybrid {
    width: 80px; /* Smaller to fit the fixed header elegantly */
    height: 80px;"""

new_logo = """.logo-hybrid {
    width: 120px; 
    height: 120px;"""

css = css.replace(old_logo, new_logo)

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Speed and logo size adjusted.")
