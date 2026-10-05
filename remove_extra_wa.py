import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Remove .body-wa-btn entirely (and its wrapping div if any, but we can just remove the <a>)
html = re.sub(r'<div style="margin: 2rem 0;">\s*<a href="https://wa\.me/558597496713" target="_blank" class="body-wa-btn">.*?</a>\s*</div>', '', html, flags=re.DOTALL)
html = re.sub(r'<a href="https://wa\.me/558597496713" target="_blank" class="body-wa-btn">.*?</a>', '', html, flags=re.DOTALL)

# Remove the .cta-btn that is in the #contato section or hero section
html = re.sub(r'<a href="https://wa\.me/558597496713" target="_blank" class="cta-btn".*?</a>', '', html, flags=re.DOTALL)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Extra WhatsApp buttons removed.")
