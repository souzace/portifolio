import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add classes to hide avatar and text on mobile
html = html.replace(
    '<div style="display: flex; align-items: center; gap: 15px; margin-right: 20px;">',
    '<div class="sticky-text-group" style="display: flex; align-items: center; gap: 15px; margin-right: 20px;">'
)

# 2. Add media query CSS to fix the mobile layout
mobile_css = """
        /* Mobile UX Fixes for Sticky Footer */
        @media (max-width: 599px) {
            .sticky-footer-bar {
                padding: 10px; /* Reduce vertical footprint */
                justify-content: center;
                gap: 10px;
            }
            .sticky-text-group {
                display: none !important; /* Hide avatar and text to save space */
            }
            .sticky-wa-btn {
                flex-grow: 1; /* Make WA button fill remaining space */
                justify-content: center;
                padding: 0.6rem;
            }
            .sticky-social-btn {
                width: 38px;
                height: 38px;
            }
        }
"""

html = html.replace("</style>", mobile_css + "</style>")

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Mobile UX fixed.")
