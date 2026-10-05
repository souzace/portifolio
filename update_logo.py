import re

# Update HTML
with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

old_logo = """<div class="logo">
                    Empório Linneo
                    <span class="logo-sub">Padaria e Confeitaria</span>
                </div>"""
new_logo = """<img src="logomark.jpg" alt="Empório Linneo" class="logo-img">"""

html = html.replace(old_logo, new_logo)

with open("emporio-linneo/index.html", "w", encoding="utf-8") as f:
    f.write(html)

# Update CSS colors and add logo-img class
with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace root variables
css = re.sub(r'--bg-light: #FDFBF7;.*', '--bg-light: #F9F3E9; /* Warm cream/kraft */', css)
css = re.sub(r'--bg-dark: #2C1E16;.*', '--bg-dark: #351C15; /* Deep coffee brown from logo */', css)
css = re.sub(r'--primary: #D35400;.*', '--primary: #D4AF37; /* Gold from logo text */', css)
css = re.sub(r'--primary-hover: #A04000;.*', '--primary-hover: #B8962E;', css)
css = re.sub(r'--text-dark: #3E2723;.*', '--text-dark: #351C15;', css)

# Make header dark to match the elegant vibe or keep it light?
# The logo has a gold background outside the circle. 
# If we set header to dark, we can clip the image to a circle.
header_css = """/* Header */
.header {
    background-color: var(--bg-dark);
    border-bottom: 1px solid rgba(212, 175, 55, 0.2);"""
css = re.sub(r'/\* Header \*/\s*\.header {.*?border-bottom:.*?;', header_css, css, flags=re.DOTALL)

# Update header text colors
css = css.replace('color: var(--text-dark);', 'color: var(--bg-light);')
css = css.replace('.nav-link:hover {\n    color: var(--primary);\n}', '.nav-link {\n    text-decoration: none;\n    color: var(--bg-light);\n    font-weight: 600;\n    font-size: 0.95rem;\n    transition: color 0.3s ease;\n}\n.nav-link:hover {\n    color: var(--primary);\n}')

# Add logo-img style
logo_img_style = """
.logo-img {
    height: 70px;
    width: 70px;
    border-radius: 50%;
    object-fit: cover;
    object-position: center;
    border: 2px solid var(--primary);
    transition: transform 0.3s ease;
}
.logo-img:hover {
    transform: scale(1.05);
}
"""
css += logo_img_style

# Let's fix the nav link replace issue because I might have replaced all text-dark
css = css.replace('color: var(--bg-light);\n    font-family: \'Outfit\', sans-serif;', 'color: var(--text-dark);\n    font-family: \'Outfit\', sans-serif;') # Revert body text color if changed

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Logo and colors updated.")
