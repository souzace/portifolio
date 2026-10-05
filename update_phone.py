import re

with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Update visible phone number
html = html.replace('📞 (85) 9988-7766', '📞 (85) 99936-2255')

# Update WhatsApp link
html = html.replace('https://wa.me/558599887766', 'https://wa.me/5585999362255')

with open("emporio-linneo/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Phone number updated.")
