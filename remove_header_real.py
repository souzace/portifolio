import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Remove the <header> tag completely
html = re.sub(r'<header>.*?</header>', '', html, flags=re.DOTALL)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Header removed for real.")
