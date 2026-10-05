import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update CSS: Change border-radius of sticky-social-btn to 5px (squared)
html = html.replace('border-radius: 50%;', 'border-radius: 5px;') 
# Wait, the avatar ALSO uses border-radius: 50%. So I shouldn't blanket replace.
# Let's target sticky-social-btn specifically
css_old = """        .sticky-social-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            border-radius: 50%;"""
css_new = """        .sticky-social-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            border-radius: 5px;"""
html = html.replace(css_old, css_new)

# Add CSS for sticky-wa-btn
wa_css = """
        .sticky-wa-btn {
            background-color: var(--brand-gold);
            color: var(--brand-dark);
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
        }
        .sticky-wa-btn:hover {
            background-color: #f7d154;
            transform: translateY(-2px);
        }
"""
html = html.replace("</style>", wa_css + "</style>")

# 2. Extract WhatsApp from sticky-socials and create the button
wa_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>'

# Remove the old WhatsApp button from sticky-socials
old_wa_btn = r'<a href="https://wa.me/558597496713" target="_blank" class="sticky-social-btn" aria-label="WhatsApp" title="Falar no WhatsApp">\s*<svg.*?</svg>\s*</a>'
html = re.sub(old_wa_btn, '', html, flags=re.DOTALL)

# Add the new WhatsApp button inside the sticky-footer-bar, next to sticky-socials
new_wa_btn = f'<a href="https://wa.me/558597496713" target="_blank" class="sticky-wa-btn">{wa_svg} Falar no WhatsApp</a>'
html = html.replace('<div class="sticky-socials">', f'{new_wa_btn}\n    <div class="sticky-socials">')

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Sticky footer updated.")
