import re

with open("emporio-linneo/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Remove sticky from header to allow a giant logo
header_old = """/* Header */
.header {
    background-color: var(--bg-dark);
    border-bottom: 1px solid rgba(212, 175, 55, 0.2);
    position: sticky;
    top: 0;
    z-index: 100;
}"""

header_new = """/* Header */
.header {
    background-color: var(--bg-dark);
    border-bottom: 1px solid rgba(212, 175, 55, 0.2);
    position: relative; /* Removed sticky so giant logo doesn't block screen on scroll */
    z-index: 100;
}"""

css = css.replace(header_old, header_new)

# 2. Increase logo size massively
logo_old = """.logo-img {
    height: 70px;
    width: 70px;"""

logo_new = """.logo-img {
    height: 140px;
    width: 140px;"""

css = css.replace(logo_old, logo_new)

# 3. Add a mobile query tweak for the larger logo
mobile_query_end = css.rfind("}")
if mobile_query_end != -1:
    # Just append to the end
    css += """
@media (max-width: 768px) {
    .logo-img {
        height: 120px;
        width: 120px;
    }
}
"""

with open("emporio-linneo/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Logo size fixed and header un-stickied.")
