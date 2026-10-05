import re

with open("beloton/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the text logo with the image logo
old_logo_pattern = r'<div class="logo">.*?</div>'
new_logo = '<a href="#"><img src="logomark.png" alt="Beloton Luthieria" class="logo-img"></a>'

html = re.sub(old_logo_pattern, new_logo, html, flags=re.DOTALL)

with open("beloton/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("beloton/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add styles for the logo image
logo_css = """
/* Logo Image */
.logo-img {
    height: 60px;
    width: auto;
    background-color: var(--text-light); /* white background to match the image */
    padding: 5px 15px;
    border-radius: 6px;
    object-fit: contain;
    transition: transform 0.3s ease;
}
.logo-img:hover {
    transform: scale(1.05);
}
"""

css += logo_css

with open("beloton/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Logo replaced on site.")
