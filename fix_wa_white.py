import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Update .sticky-wa-btn
old_sticky_wa = re.search(r'\.sticky-wa-btn \{.*?\}', html, re.DOTALL).group(0)
new_sticky_wa = """.sticky-wa-btn {
            background-color: transparent;
            color: #fff;
            border: 2px solid #fff;
            padding: 0.6rem 1.2rem;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            font-family: sans-serif;
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.3s ease;
            white-space: nowrap;
        }"""
html = html.replace(old_sticky_wa, new_sticky_wa)

old_sticky_wa_hover = re.search(r'\.sticky-wa-btn:hover \{.*?\}', html, re.DOTALL).group(0)
new_sticky_wa_hover = """.sticky-wa-btn:hover {
            background-color: rgba(255, 255, 255, 0.1);
            transform: translateY(-2px);
        }"""
html = html.replace(old_sticky_wa_hover, new_sticky_wa_hover)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("WhatsApp button line made white.")
