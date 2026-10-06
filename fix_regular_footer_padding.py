with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Reduce padding on regular footer on mobile
mobile_override = """
    .regular-footer { padding: 2rem 0 5rem !important; } /* 5rem padding bottom ensures text is not covered by sticky footer, but removes extra spacing above it */
    .regular-footer .copyright { margin-bottom: 0 !important; padding-bottom: 0 !important; }
    .orkes-credits { margin-bottom: 0 !important; }
"""

# We'll replace a known string inside the media query or just append it safely.
# Let's insert it inside the @media (max-width: 992px) block we added before.
if '.ff-title { font-size: 1rem !important; margin-right: auto; }' in css:
    css = css.replace('.ff-title { font-size: 1rem !important; margin-right: auto; }', '.ff-title { font-size: 1rem !important; margin-right: auto; }\n' + mobile_override)

# Also let's check if there is body padding-bottom. If we use 5rem on the footer, we can remove body padding.
css = css.replace('body { padding-bottom: 80px !important; }', '/* body { padding-bottom: 80px !important; } removed */')

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Regular footer padding fixed.")
