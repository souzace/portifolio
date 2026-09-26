import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the problematic CSS block
old_css = """        .sticky-footer-bar p {
            margin: 0 1rem 0 0;
            color: #fff;
            font-family: sans-serif;
            font-size: 1rem;
            display: none; /* Hide text on very small screens */
        }
        @media (min-width: 600px) {
            .sticky-footer-bar p {
                display: block;
            }
        }"""

new_css = """        .sticky-footer-bar {
            flex-wrap: wrap;
            gap: 10px;
        }
        .sticky-footer-bar p {
            margin: 0;
            color: #fff;
            font-family: sans-serif;
            font-size: 0.85rem;
            text-align: center;
        }
        .sticky-btn {
            padding: 0.6rem 1.2rem;
            font-size: 0.8rem;
        }
        @media (min-width: 600px) {
            .sticky-footer-bar p {
                font-size: 1rem;
                margin-right: 1rem;
                text-align: left;
            }
            .sticky-btn {
                padding: 0.8rem 2rem;
                font-size: 0.9rem;
            }
            .sticky-footer-bar {
                flex-wrap: nowrap;
            }
        }"""

html = html.replace(old_css, new_css)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Mobile footer fixed.")
