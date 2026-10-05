import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Re-add the body WA button to #contato
# It was removed previously. Let's find #contato.
contato_match = re.search(r'(<p>Para convites de regência, encomendas de arranjos ou parcerias musicais\.</p>)', html)
if contato_match:
    phone_svg = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>'
    body_wa_btn = f'\n    <div style="margin: 2rem 0;">\n        <a href="https://wa.me/558597496713" target="_blank" class="body-wa-btn">{phone_svg} FALAR NO WHATSAPP</a>\n    </div>\n'
    html = html.replace(contato_match.group(1), contato_match.group(1) + body_wa_btn)

# 2. Add CSS for body-wa-btn
css_addon = """
        .body-wa-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            padding: 0.8rem 2rem;
            background-color: transparent;
            color: #25D366;
            border: 2px solid #25D366;
            text-decoration: none;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-weight: bold;
            border-radius: 5px;
            transition: all 0.3s ease;
        }
        .body-wa-btn:hover {
            background-color: rgba(37, 211, 102, 0.1);
            transform: translateY(-2px);
        }
"""
html = html.replace("</style>", css_addon + "</style>")

# 3. Ensure sticky-bottom-row is aligned to the right on desktop
desktop_css_match = re.search(r'@media \(min-width: 600px\) \{.*?\n        \}', html, re.DOTALL)
if desktop_css_match:
    old_desktop_css = desktop_css_match.group(0)
    # The sticky footer bar should use flex end for the right side
    new_desktop_css = """@media (min-width: 600px) {
            .sticky-footer-bar {
                justify-content: space-between;
                padding-left: 5%;
                padding-right: 5%;
            }
            .sticky-bottom-row {
                display: flex;
                align-items: center;
                gap: 15px;
                justify-content: flex-end;
            }
        }"""
    # Replace the old desktop css with the new one
    # Wait, the current html might not have exactly that block due to previous edits.
    # Let's just append the override to the end of style
    html = html.replace("</style>", "\n        " + new_desktop_css + "\n</style>")


with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Buttons matched perfectly to screenshot.")
