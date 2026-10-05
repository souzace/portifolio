import re

with open("beloton/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Wrap the saxophone and notes in a relative span so the notes anchor precisely to the sax
old_sax = '<svg class="logo-sax"'
new_sax = '<span style="position: relative; display: inline-block;"><svg class="logo-sax"'
html = html.replace(old_sax, new_sax)

old_notes_end = '</div><br>'
new_notes_end = '</div></span><br>'
html = html.replace(old_notes_end, new_notes_end)

with open("beloton/index.html", "w", encoding="utf-8") as f:
    f.write(html)


with open("beloton/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Update CSS to anchor from the sax span
css = css.replace('right: 5px;', 'left: 0px;')
css = css.replace('top: -5px;', 'top: -20px;')

with open("beloton/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Notes anchored to sax.")
