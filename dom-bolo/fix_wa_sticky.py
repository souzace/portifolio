import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("5585900000000", "5585991648313")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Sticky footer WhatsApp number updated.")
