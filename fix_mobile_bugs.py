import re

with open("beloton/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Fix .logo to prevent wrapping of the sax icon
css = css.replace('.logo {', '.logo {\n    white-space: nowrap;')

# Fix floating-notes in mobile media query
old_mobile_notes = """    .floating-notes {
        right: 15px; /* Adjust slightly for scaled sax */
        top: -8px;
    }"""
    
new_mobile_notes = """    .floating-notes {
        right: auto;
        left: 12px;
        top: -6px;
    }"""
    
css = css.replace(old_mobile_notes, new_mobile_notes)

# Fix testimonial animation if needed:
# If gap is 2rem and max-width shrinks, the transform calc(-50% - 1rem) works perfectly 
# as long as the duplicated track is exactly the same size. 
# BUT wait! If there's an odd number of cards, or if the container stretches weirdly...
# I duplicated the 4 cards, so there are 8 cards. This is correct.
# What if flex: 0 0 320px causes cards to shrink below their min-content?
# I'll add min-width: 280px just to be safe.

css = css.replace('flex: 0 0 320px;', 'flex: 0 0 300px;\n        min-width: 280px;')

with open("beloton/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Mobile bugs fixed.")
