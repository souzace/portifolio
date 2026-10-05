import re

with open("beloton/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Remove white-space: nowrap from the grouped selector
old_h_group = """h1, h2, h3, .logo {
    white-space: nowrap;"""
new_h_group = """h1, h2, h3, .logo {"""

css = css.replace(old_h_group, new_h_group)

with open("beloton/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Removed white-space nowrap from h1, h2, h3.")
