import re

with open("beloton/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add SVG to logo
old_logo = '<span class="logo-clef">&#x1D121;</span>eloton'
new_logo = '<svg class="logo-sax" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M4,2A1,1 0 0,0 3,3A1,1 0 0,0 4,4A3,3 0 0,1 7,7V8.66L7,15.5C7,19.1 9.9,22 13.5,22C17.1,22 20,19.1 20,15.5V13A1,1 0 0,0 21,12A1,1 0 0,0 20,11H14A1,1 0 0,0 13,12A1,1 0 0,0 14,13V15A1,1 0 0,1 13,16A1,1 0 0,1 12,15V11A1,1 0 0,0 13,10A1,1 0 0,0 12,9V8A1,1 0 0,0 13,7A1,1 0 0,0 12,6V5.5A3.5,3.5 0 0,0 8.5,2H4Z" /></svg><span class="logo-clef">&#x1D121;</span>eloton'

html = html.replace(old_logo, new_logo)

with open("beloton/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("beloton/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add CSS for logo-sax
sax_css = """
.logo-sax {
    fill: var(--gold);
    width: 32px;
    height: 32px;
    vertical-align: middle;
    margin-right: 6px;
    transform: translateY(-2px);
}
.logo-clef {
"""
css = css.replace('.logo-clef {\n', sax_css)

with open("beloton/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Saxophone added.")
