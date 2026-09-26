import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Create the avatar HTML
avatar_html = """
    <div style="display: flex; align-items: center; gap: 15px; margin-right: 20px;">
        <img src="avatar.jpg" alt="Chef Dom Bolo" style="width: 50px; height: 50px; border-radius: 50%; object-fit: cover; border: 2px solid var(--brand-orange);">
        <p style="margin: 0;">Gostou dos nossos bolos? Faça sua encomenda agora mesmo!</p>
    </div>
"""

# Replace the existing <p> text with the new flex container containing the avatar + text
html = re.sub(
    r'<p>Gostou dos nossos bolos\? Faça sua encomenda agora mesmo!</p>',
    avatar_html,
    html
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Avatar added to sticky footer.")
