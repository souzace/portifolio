import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Change logo to NV
html = html.replace('<div class="logo">Nilson Vieira</div>', '<div class="logo">NV</div>')

# 2. Put Nilson Vieira back in the center
html = html.replace('<h1>Maestro, Arranjador & Compositor</h1>', '<h1>Nilson Vieira</h1>\n        <h2>Maestro, Arranjador & Compositor</h2>')

# 3. Add a touch of elegance to the NV logo using CSS
# Currently .logo is just font-size: 1.5rem; font-weight: bold; color: var(--brand-gold);
# Let's add a slight letter-spacing to make "NV" look like a monogram brand
css_addon = """
        .logo {
            letter-spacing: 2px;
            font-family: serif; /* Gives a more classic maestro vibe */
        }
"""
html = html.replace("</style>", css_addon + "</style>")


with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Option 1 implemented.")
