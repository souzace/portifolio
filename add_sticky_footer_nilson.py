import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

sticky_css = """
        /* Sticky Footer */
        body {
            padding-bottom: 80px; /* Space for the sticky footer */
        }
        .sticky-footer-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: rgba(10, 10, 10, 0.95);
            backdrop-filter: blur(5px);
            border-top: 1px solid rgba(212, 175, 55, 0.3);
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 10px 20px;
            z-index: 1000;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.5);
            flex-wrap: wrap;
            gap: 15px;
            box-sizing: border-box;
        }
        .sticky-footer-bar p {
            margin: 0;
            color: #fff;
            font-family: sans-serif;
            font-size: 0.9rem;
            text-align: center;
        }
        .sticky-socials {
            display: flex;
            gap: 15px;
            align-items: center;
        }
        .sticky-social-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background-color: transparent;
            color: var(--brand-gold);
            border: 1px solid var(--brand-gold);
            transition: all 0.3s ease;
        }
        .sticky-social-btn:hover {
            background-color: var(--brand-gold);
            color: var(--brand-dark);
            transform: translateY(-2px);
        }
        @media (min-width: 600px) {
            .sticky-footer-bar {
                justify-content: space-between;
                padding: 10px 40px;
            }
            .sticky-footer-bar p {
                font-size: 1rem;
            }
        }
"""

# Insert CSS right before </style>
html = html.replace("</style>", sticky_css + "</style>")

sticky_html = """
<!-- Sticky Footer -->
<div class="sticky-footer-bar">
    <p>Gostou do meu trabalho? Vamos conversar!</p>
    <div class="sticky-socials">
        <a href="#" class="sticky-social-btn" aria-label="WhatsApp" title="Falar no WhatsApp">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
        </a>
        <a href="#" class="sticky-social-btn" aria-label="Instagram" title="Seguir no Instagram">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
        </a>
        <a href="#" class="sticky-social-btn" aria-label="YouTube" title="Ver no YouTube">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33 2.78 2.78 0 0 0 1.94 2c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.33 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
        </a>
    </div>
</div>
</body>"""

# Insert HTML right before </body>
html = html.replace("</body>", sticky_html)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Sticky footer added.")
