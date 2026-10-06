import re

with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add GPU acceleration to marquee
if 'will-change: transform;' not in css:
    css = css.replace('.marquee-track {', '.marquee-track {\n    will-change: transform;\n    transform: translateZ(0);')

# Also add translateZ to the keyframes
css = css.replace('transform: translateX(-50%);', 'transform: translateX(-50%) translateZ(0);')
css = css.replace('transform: translateX(0);', 'transform: translateX(0) translateZ(0);')

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

# Add lazy loading to images
with open("emporio-linneo/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace img tags in grid and historia to lazy load
# For example, <img src="product1.jpg" alt="Pão rústico" class="arch-img">
html = re.sub(r'(<img[^>]+class="arch-img"[^>]*)(>)', r'\1 loading="lazy"\2', html)
# Do the same for the avatar just in case, though it's above the fold. Actually we'll leave avatar as is.

with open("emporio-linneo/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Performance tweaks applied.")
