import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

wa_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px; vertical-align: middle; position: relative; top: -1px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>"""

# Replace the normal footer button
html = re.sub(
    r'(<a href="https://www\.instagram\.com/dombolofortal/" target="_blank" class="cta-btn" style="padding: 0.8rem 2rem; display: inline-block;">)Falar no WhatsApp</a>',
    r'\1' + wa_svg + 'Falar no WhatsApp</a>',
    html
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("WhatsApp icon added to standard footer button.")
