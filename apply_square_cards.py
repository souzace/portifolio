import re

with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace product image border radius
css = css.replace("border-radius: 200px 200px 0 0;", "border-radius: 0;")
# Replace history image border radius
css = css.replace("border-radius: 250px 250px 0 0;", "border-radius: 0;")

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Squared cards applied.")
