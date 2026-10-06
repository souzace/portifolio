import re

with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Clean up footer text
text_block = """<div class="footer-fixed-text">
                    <span class="ff-title">Venha nos conhecer!</span>
                    <span class="ff-sub">Venha nos conhecer!</span>
                </div>"""
new_text_block = """<div class="footer-fixed-text">
                    <span class="ff-title">Venha nos conhecer!</span>
                </div>"""
html = html.replace(text_block, new_text_block)

# Just in case it was the old text
text_block_2 = """<div class="footer-fixed-text">
                    <span class="ff-title">Fornada saindo agora!</span>
                    <span class="ff-sub">Venha nos conhecer!</span>
                </div>"""
html = html.replace(text_block_2, new_text_block)

# 2. Fix Instagram gap
html = html.replace('margin-right: 1.5rem;', 'margin-right: 0.5rem;')

# 3. Ensure button text is visible
btn_html = '<span class="hide-mobile">Fazer Pedido</span><span class="show-mobile">Pedir</span>'
html = html.replace(btn_html, 'Fazer Pedido')

with open("emporio-linneo/index.html", "w", encoding="utf-8") as f:
    f.write(html)


with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# 4. Remove the border/line from sticky footer
css = css.replace('border-top: 2px solid var(--primary);', 'border-top: none;')

# Fix the padding bottom on iOS safely
if 'env(safe-area-inset-bottom)' not in css:
    css = css.replace('.sticky-footer-bar {', '.sticky-footer-bar {\n    padding-bottom: calc(12px + env(safe-area-inset-bottom));')

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Final mobile issues fixed.")
