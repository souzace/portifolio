import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the previous mobile CSS
old_css = """        @media (max-width: 599px) {
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
        }"""

new_css = """        @media (max-width: 599px) {
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

html = html.replace(old_css, new_css)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Mobile UX updated to keep avatar compactly.")
