import re

with open("beloton/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Force display block on mobile header
old_mobile = """    .header-content {
        flex-direction: column;
        align-items: flex-start; /* Align logo to left on mobile */
        padding: 1rem;
        text-align: left;
    }"""
    
new_mobile = """    .header-content {
        display: block;
        padding: 1rem 1.5rem;
        text-align: left;
    }
    .header-content a {
        display: inline-block;
        text-align: left;
    }"""
    
css = css.replace(old_mobile, new_mobile)

with open("beloton/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Mobile header alignment forced to left.")
