import re

with open("beloton/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Change all Beluton to Beloton
html = html.replace('Beluton', 'Beloton')
html = html.replace('beluton', 'beloton')

with open("beloton/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Name updated to Beloton.")
