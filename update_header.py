import re

with open("beloton/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Remove the button from the header
button_pattern = r'<a href="[^"]*" class="btn-outline-gold" target="_blank">Falar com o Luthier</a>'
html = re.sub(button_pattern, '', html)

with open("beloton/index.html", "w", encoding="utf-8") as f:
    f.write(html)


with open("beloton/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Change mobile alignment
old_mobile_header = """@media (max-width: 768px) {
    .header-content {
        flex-direction: column;
        gap: 12px;
        padding: 1rem;
        text-align: center;
    }"""
    
new_mobile_header = """@media (max-width: 768px) {
    .header-content {
        flex-direction: column;
        align-items: flex-start; /* Align logo to left on mobile */
        padding: 1rem;
        text-align: left;
    }"""
    
css = css.replace(old_mobile_header, new_mobile_header)

with open("beloton/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Header updated.")
