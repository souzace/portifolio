import re

with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Fix desktop regular footer: replace the broken padding block
css = css.replace('.regular-footer {\n    padding-bottom: 6rem;\n    background-color: #1a0e0a;\n    padding: 3rem 0 2rem;\n    text-align: center;', '.regular-footer {\n    background-color: #1a0e0a;\n    padding: 3rem 0 100px !important;\n    text-align: center;')

# Fix mobile regular footer
css = css.replace('.regular-footer {\n    padding-bottom: 6rem; padding: 2rem 0 5rem !important; }', '.regular-footer { padding: 2rem 0 100px !important; }')

# Just in case the replace didn't hit exactly because of spacing, let's use regex to enforce padding-bottom on regular footer globally
css += "\n.regular-footer { padding-bottom: 110px !important; }\n"

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Footer padding overridden.")
