import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add CSS for the sticky footer
css_injection = """
        .sticky-footer-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: var(--brand-brown);
            border-top: 2px solid var(--brand-orange);
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 1rem;
            box-shadow: 0 -4px 10px rgba(0,0,0,0.15);
            z-index: 1000;
            box-sizing: border-box;
        }
        .sticky-footer-bar p {
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
        }
        .sticky-btn {
            background-color: var(--brand-orange);
            color: #fff;
            padding: 0.8rem 2rem;
            text-decoration: none;
            border-radius: 30px;
            font-weight: bold;
            font-family: sans-serif;
            text-transform: uppercase;
            font-size: 0.9rem;
            transition: background 0.3s;
        }
        .sticky-btn:hover {
            background-color: #D9690D;
        }
        /* Add padding to body so the sticky footer doesn't hide content */
        body {
            padding-bottom: 80px;
        }
"""

html = html.replace("</style>", css_injection + "</style>")

# 2. Add the HTML for the sticky footer right before </body>
sticky_html = """
<div class="sticky-footer-bar">
    <p>Gostou dos nossos bolos? Faça sua encomenda agora mesmo!</p>
    <a href="https://www.instagram.com/dombolofortal/" target="_blank" class="sticky-btn">Pedir no WhatsApp</a>
</div>
</body>
"""

html = html.replace("</body>", sticky_html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Sticky footer added.")
