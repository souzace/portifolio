import os

files = [
    ('index.html', 'Bora conversar', 'Ou envie um e-mail para: ', 'https://wa.me/5585991634033?text=Ol%C3%A1%20F%C3%A1bio%2C%20acessei%20o%20seu%20portf%C3%B3lio%20e%20gostaria%20de%20conversar%20sobre%20um%20projeto.'),
    ('index-en.html', "Talk to the Expert", 'Or send an email to: ', 'https://wa.me/5585991634033?text=Hello%20Fabio%2C%20I%20accessed%20your%20portfolio%20and%20would%20like%20to%20talk%20about%20a%20project.'),
    ('index-es.html', 'Hablar con el Experto', 'O env\u00ede un correo electr\u00f3nico a: ', 'https://wa.me/5585991634033?text=Hola%20Fabio%2C%20acced%C3%AD%20a%20tu%20portafolio%20y%20me%20gustar%C3%ADa%20hablar%20sobre%20un%20proyecto.')
]

for filename, btn_text, email_text, w_link in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # The exact block that was inserted:
    # <a href="..." target="_blank" class="cta-btn" style="display: inline-flex; align-items: center; justify-content: center; gap: 8px; padding: 12px 24px; background: var(--cyan-accent); color: var(--bg-color); text-decoration: none; border-radius: 4px; text-align: center; font-weight: 600; margin-top: 16px; transition: all 0.2s;" onmouseover="this.style.background='var(--cyan-hover)';" onmouseout="this.style.background='var(--cyan-accent)';">TEXT</a>
    # <p style="margin-top: 12px; font-size: 0.85rem; color: var(--text-muted); text-align: center;">EMAIL_TEXT<a href="mailto:contato@orkes.com.br" style="color: var(--cyan-accent); text-decoration: none; font-weight: 500;">contato@orkes.com.br</a></p>
    
    import re
    # We will use regex to remove anything that looks like the card button.
    # It starts with `<a href="https://wa.me/` and ends with `contato@orkes.com.br</a></p>`
    # But ONLY if it has `margin-top: 12px; font-size: 0.85rem;` (which is unique to the cards, the footer has 0.95rem and 16px margin)
    
    pattern = r'\s*<a href="https://wa\.me/[^"]+" target="_blank" class="cta-btn" style="display: inline-flex; align-items: center; justify-content: center; gap: 8px; padding: 12px 24px; background: var\(--cyan-accent\); color: var\(--bg-color\); text-decoration: none; border-radius: 4px; text-align: center; font-weight: 600; margin-top: 16px; transition: all 0\.2s;" onmouseover="this\.style\.background=\'var\(--cyan-hover\)\';" onmouseout="this\.style\.background=\'var\(--cyan-accent\)\';">.*?</a>\s*<p style="margin-top: 12px; font-size: 0\.85rem; color: var\(--text-muted\); text-align: center;">.*?<a href="mailto:contato@orkes\.com\.br" style="color: var\(--cyan-accent\); text-decoration: none; font-weight: 500;">contato@orkes\.com\.br</a></p>'
    
    content = re.sub(pattern, '', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("CTAs removed from cards successfully!")
