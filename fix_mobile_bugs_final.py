import re

with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix Sticky Footer Text
html = html.replace('<span class="ff-title">Fornada saindo agora!</span>', '<span class="ff-title">Venha nos conhecer!</span>')

with open("emporio-linneo/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Fix Mobile CSS Issues
# 1. Logo overlap: .classic-nav-container needs justify-content: center
# 2. Historia image sliver: needs min-height
# 3. Instagram icon hidden on mobile: remove display: none for .footer-socials

css = css.replace('.hybrid-header { justify-content: center; position: fixed; }', '.classic-nav-container { justify-content: center; }')

# Fix historia image sliver
if '.historia-image-arch { width: 100%; height: 400px; order: -1; }' in css:
    css = css.replace('.historia-image-arch { width: 100%; height: 400px; order: -1; }', '.historia-image-arch { width: 100%; min-height: 400px; order: -1; display: block; }')
else:
    # Append rule to mobile block if not strictly matching
    pass # we'll just append a stronger rule

# Unhide instagram icon
css = css.replace('.footer-socials { display: none !important; /* hide insta on mobile sticky bar to save space */ }', '.footer-socials { display: flex !important; }')

# Fix logo size if needed
css = css.replace('.logo-hybrid { width: 90px; height: 90px; margin: 0 auto; }', '.logo-hybrid { width: 110px; height: 110px; margin: 0 auto; }')

# Add strong overrides
overrides = """
@media (max-width: 992px) {
    .classic-nav-container { justify-content: center !important; }
    .historia-image-arch { min-height: 400px !important; display: block !important; }
    .ff-title { font-size: 1rem !important; margin-right: auto; }
    .footer-fixed-left { flex: 1; }
    .footer-fixed-right { display: flex !important; align-items: center; gap: 10px; }
}
"""
css += overrides

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Mobile bugs fixed.")
