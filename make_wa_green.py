import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update .cta-btn (hero WhatsApp button)
old_cta_css = re.search(r'\.cta-btn \{.*?\}', html, re.DOTALL).group(0)
new_cta_css = """.cta-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            padding: 1rem 2.5rem;
            background-color: transparent;
            color: #25D366;
            border: 2px solid #25D366;
            text-decoration: none;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-weight: bold;
            border-radius: 5px;
            margin-top: 2rem;
            transition: all 0.3s ease;
        }"""
html = html.replace(old_cta_css, new_cta_css)

old_cta_hover = re.search(r'\.cta-btn:hover \{.*?\}', html, re.DOTALL).group(0)
new_cta_hover = """.cta-btn:hover {
            background-color: rgba(37, 211, 102, 0.1);
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(37, 211, 102, 0.2);
        }"""
html = html.replace(old_cta_hover, new_cta_hover)

# 2. Update .sticky-wa-btn
old_sticky_wa = re.search(r'\.sticky-wa-btn \{.*?\}', html, re.DOTALL).group(0)
new_sticky_wa = """.sticky-wa-btn {
            background-color: transparent;
            color: #25D366;
            border: 2px solid #25D366;
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
            background-color: rgba(37, 211, 102, 0.1);
            transform: translateY(-2px);
        }"""
html = html.replace(old_sticky_wa_hover, new_sticky_wa_hover)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("WhatsApp buttons updated to hollow green.")
