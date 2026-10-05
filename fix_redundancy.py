import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Remove the redundant <h1>Nilson Vieira</h1> and promote the <h2>
html = html.replace('<h1>Nilson Vieira</h1>\n        <h2>Maestro, Arranjador & Compositor</h2>', '<h1>Maestro, Arranjador & Compositor</h1>')

# If the previous replace failed because of spaces:
html = re.sub(r'<h1>Nilson Vieira</h1>\s*<h2>Maestro, Arranjador & Compositor</h2>', '<h1>Maestro, Arranjador & Compositor</h1>', html)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Redundancy fixed.")
