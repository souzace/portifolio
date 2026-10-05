import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix the mobile override for .sticky-wa-btn
old_mobile_wa = """            .sticky-wa-btn {
                margin: 0;
                padding: 0.5rem 1rem;
                font-size: 0.85rem;
                border-radius: 5px; border: 1px solid var(--brand-gold);
            }"""

new_mobile_wa = """            .sticky-wa-btn {
                margin: 0;
                padding: 0.5rem 1rem;
                font-size: 0.85rem;
                border-radius: 5px;
            }"""

html = html.replace(old_mobile_wa, new_mobile_wa)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Mobile WA border fixed.")
