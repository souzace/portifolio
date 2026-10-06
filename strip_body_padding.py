with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Strip all body padding-bottom
css = css.replace('padding-bottom: 80px;', '')
css = css.replace('body { padding-bottom: 120px; }', '')
css = css.replace('body { padding-bottom: 80px !important; }', '')

# Ensure regular-footer has enough padding to hide behind the sticky bar on ALL screen sizes
css = css.replace('.regular-footer {', '.regular-footer {\n    padding-bottom: 6rem;')

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Body padding removed.")
