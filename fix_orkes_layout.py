import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. We need to restructure the HTML of the sticky footer to have a clear top row and bottom row
# Current HTML has: 
# <div class="sticky-text-group">...</div>
# <a class="sticky-wa-btn">...</a>
# <div class="sticky-socials">...</div>
# all as direct children of .sticky-footer-bar

# We will wrap the wa-btn and socials in a bottom-row div
html = html.replace(
    '<a href="https://wa.me/558597496713" target="_blank" class="sticky-wa-btn">',
    '<div class="sticky-bottom-row">\n    <a href="https://wa.me/558597496713" target="_blank" class="sticky-wa-btn">'
)
html = html.replace(
    '</div>\n</div>\n</body>',
    '</div>\n</div>\n</div>\n</body>'
) # Close the sticky-bottom-row div

# Update the CSS to style this new layout for mobile
old_css = """        @media (max-width: 599px) {
            .sticky-footer-bar {
                padding: 8px 10px;
                justify-content: center;
                gap: 8px;
                flex-direction: column; /* Stack top and bottom rows compactly */
            }
            .sticky-text-group {
                display: flex !important;
                gap: 10px !important;
                margin-right: 0 !important;
                width: 100%;
                justify-content: center;
            }
            .sticky-text-group > div {
                width: 35px !important;
                height: 35px !important;
            }
            .sticky-text-group p {
                font-size: 0.8rem !important;
                line-height: 1.2;
                text-align: left;
            }
            .sticky-socials {
                width: 100%;
                justify-content: center;
                gap: 8px;
            }
            .sticky-wa-btn {
                flex-grow: 1;
                justify-content: center;
                padding: 0.4rem 0.6rem;
                font-size: 0.8rem;
            }
            .sticky-wa-btn svg {
                width: 16px;
                height: 16px;
            }
            .sticky-social-btn {
                width: 32px;
                height: 32px;
            }
            .sticky-social-btn svg {
                width: 16px;
                height: 16px;
            }
        }"""

new_css = """        @media (max-width: 599px) {
            .sticky-footer-bar {
                padding: 12px 15px;
                flex-direction: column;
                gap: 12px;
                align-items: stretch;
            }
            .sticky-text-group {
                display: flex !important;
                gap: 12px !important;
                margin-right: 0 !important;
                width: 100%;
                justify-content: center;
            }
            .sticky-text-group > div {
                width: 40px !important;
                height: 40px !important;
                border-radius: 50% !important; /* Make it circular like Orkes */
            }
            .sticky-text-group p {
                font-size: 0.85rem !important;
                font-weight: bold;
                margin: 0;
            }
            .sticky-bottom-row {
                display: flex;
                justify-content: space-between;
                align-items: center;
                width: 100%;
            }
            .sticky-socials {
                display: flex;
                gap: 10px;
            }
            .sticky-social-btn {
                width: auto; /* Remove fixed width to match Orkes minimal style */
                height: auto;
                border: none !important; /* Remove borders */
                background: transparent !important;
                padding: 0;
            }
            .sticky-social-btn svg {
                width: 22px;
                height: 22px;
                color: #aaa;
            }
            .sticky-wa-btn {
                margin: 0;
                padding: 0.5rem 1rem;
                font-size: 0.85rem;
                border-radius: 5px;
            }
        }
        
        /* Desktop fix for the new wrapper */
        @media (min-width: 600px) {
            .sticky-bottom-row {
                display: flex;
                align-items: center;
                gap: 15px;
            }
        }
"""

html = html.replace(old_css, new_css)

# Also remove the inline border from sticky-social-btn and let CSS handle it
html = html.replace('border: 1px solid var(--brand-gold);', '')
html = html.replace('border-radius: 5px;', 'border-radius: 5px; border: 1px solid var(--brand-gold);') # restore it for desktop

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML updated.")
