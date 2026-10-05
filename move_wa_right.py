import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Extract wa-btn
wa_match = re.search(r'<a href="https://wa.me/558597496713" target="_blank" class="sticky-wa-btn">.*?</a>', html, re.DOTALL)
wa_html = wa_match.group(0)

# Extract sticky-socials div entirely
socials_match = re.search(r'<div class="sticky-socials">.*?</div>', html, re.DOTALL)
socials_html = socials_match.group(0)

# Replace the whole sticky-bottom-row content
old_bottom_row = f'{wa_html}\n    {socials_html}'
new_bottom_row = f'{socials_html}\n    {wa_html}'

if old_bottom_row in html:
    html = html.replace(old_bottom_row, new_bottom_row)
else:
    # If indentation is different
    html = html.replace(wa_html, '')
    html = html.replace(socials_html, f'{socials_html}\n    {wa_html}')

# Also, ensure on desktop that it looks correct. The user said "align right". 
# If they literally mean align to the right edge of the screen, we can use margin-left: auto on the wa-btn for desktop.
# Let's add a CSS rule for desktop to push the bottom row or the WA button to the right if needed, but flex gap might be enough.
# Let's just make the sticky-bottom-row take flex-grow if we want it aligned right.
css_addon = """
        @media (min-width: 600px) {
            .sticky-footer-bar {
                justify-content: space-between;
                padding-left: 5%;
                padding-right: 5%;
            }
            .sticky-bottom-row {
                justify-content: flex-end;
            }
        }
"""
# Actually, the user just said "align right". Let's push WA to the right.
# We'll see if the above works, but I'll only add flex order changes for now.

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Swapped WA and Socials.")
