import re

with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Restore the two lines of text
old_text = """<div class="footer-fixed-text">
                    <span class="ff-title">Venha nos conhecer!</span>
                </div>"""
new_text = """<div class="footer-fixed-text">
                    <span class="ff-title">Fornada saindo agora!</span>
                    <span class="ff-sub">Venha nos conhecer!</span>
                </div>"""
html = html.replace(old_text, new_text)

# 2. Instagram gap
html = html.replace('margin-right: 0.5rem;', 'margin-right: 0.2rem;')

with open("emporio-linneo/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# 3. Restore border-top
css = css.replace('border-top: none;', 'border-top: 2px solid var(--primary);')

# 4. Show ff-sub on mobile
css = css.replace('.ff-sub { display: none; /* Hide subtitle to save vertical space */ }', '.ff-sub { display: block !important; font-size: 0.75rem !important; color: rgba(249, 243, 233, 0.6) !important; margin-top: 2px; font-weight: normal; }')

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Final mobile issues v2 fixed.")
