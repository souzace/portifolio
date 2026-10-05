import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("5585999999999", "5585991648313")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("WhatsApp number updated.")
