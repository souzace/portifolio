import re

with open("beloton/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the image logo with the HTML/CSS hybrid logo using Unicode C-Clef (Alto Clef)
old_logo_pattern = r'<a href="#"><img src="logomark.png" alt="Beloton Luthieria" class="logo-img"></a>'
new_logo = """<a href="#" style="text-decoration: none;">
                <div class="logo">
                    <span class="logo-clef">&#x1D122;</span>eloton<br>
                    <span class="logo-sub">Luthieria Contemporânea</span>
                </div>
            </a>"""

html = re.sub(old_logo_pattern, new_logo, html, flags=re.DOTALL)

with open("beloton/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("beloton/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add styles for the new text logo
logo_css = """
/* Reverted and Improved Text Logo */
.logo {
    font-size: 2rem;
    font-weight: 700;
    color: var(--gold);
    line-height: 1;
    letter-spacing: 1px;
    display: inline-block;
}
.logo-clef {
    font-family: 'Times New Roman', serif; /* Best fallback for musical symbols */
    font-size: 1.2em;
    font-weight: normal;
    margin-right: 2px;
    display: inline-block;
    transform: translateY(4px);
}
.logo-sub {
    font-family: 'Raleway', sans-serif;
    font-size: 0.75rem;
    font-weight: 400;
    text-transform: uppercase;
    letter-spacing: 3px;
    color: var(--text-light);
    display: block;
    margin-top: 4px;
}
"""

css += logo_css

with open("beloton/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Header logo fixed.")
