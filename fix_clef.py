import re

with open("beloton/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace F-clef with C-clef
html = html.replace('&#x1D122;', '&#x1D121;')

with open("beloton/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Clef fixed.")
