import re

with open("beloton/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Fix the .floating-notes position
old_css = """/* Floating Music Notes Animation */
.floating-notes {
    position: absolute;
    right: -10px; /* Adjust based on where the sax is */
    top: -15px;"""

new_css = """/* Floating Music Notes Animation */
.floating-notes {
    position: absolute;
    right: 5px; /* Moved inwards closer to the sax bell */
    top: -5px;  /* Lowered closer to the sax body */"""

css = css.replace(old_css, new_css)

# Also tighten the spread of notes slightly so they don't wander off too far
css = css.replace('left: 10px;', 'left: 6px;')
css = css.replace('left: 20px;', 'left: 12px;')

with open("beloton/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Notes repositioned.")
