import re

files = [
    ('index.html', 'Vamos conversar', 'Ou envie um e-mail para: '),
    ('index-en.html', "Let's talk", 'Or send an email to: '),
    ('index-es.html', 'Vamos a hablar', 'O env\u00ede un correo electr\u00f3nico a: ')
]

for filename, btn_text, email_text in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix Footer CTA (Remove green background and fix text color)
    # The footer CTA has id="cta-whatsapp-btn"
    content = re.sub(
        r'id="cta-whatsapp-btn" class="cta-btn" style="background-color: #25D366;',
        r'id="cta-whatsapp-btn" class="cta-btn" style="',
        content
    )

    # 2. Add email text below Service Card buttons and make them solid cyan
    # Service card buttons look like:
    # <a href="..." target="_blank" style="display: inline-block; padding: 12px 24px; background: transparent; border: 1px solid var(--cyan-accent); color: var(--cyan-accent); text-decoration: none; border-radius: 4px; text-align: center; font-weight: 600; margin-top: 16px; transition: all 0.2s;" onmouseover="..." onmouseout="...">Let's talk</a>
    
    # We want to replace the style to be solid, and append the email <p> after </a>
    
    # Regex to find the service card buttons
    def replace_card_btn(match):
        href = match.group(1)
        text = match.group(2)
        
        # New solid button style
        new_style = "display: inline-flex; align-items: center; justify-content: center; gap: 8px; padding: 12px 24px; background: var(--cyan-accent); color: var(--bg-color); text-decoration: none; border-radius: 4px; text-align: center; font-weight: 600; margin-top: 16px; transition: all 0.2s;"
        onmouseover = "this.style.background='var(--cyan-hover)';"
        onmouseout = "this.style.background='var(--cyan-accent)';"
        
        button_html = f'<a href="{href}" target="_blank" class="cta-btn" style="{new_style}" onmouseover="{onmouseover}" onmouseout="{onmouseout}">{text}</a>'
        email_html = f'\n                      <p style="margin-top: 12px; font-size: 0.85rem; color: var(--text-muted); text-align: center;">{email_text}<a href="mailto:contato@orkes.com.br" style="color: var(--cyan-accent); text-decoration: none; font-weight: 500;">contato@orkes.com.br</a></p>'
        
        return button_html + email_html

    # Use regex to match the anchor tag for service cards
    # Pattern looks for <a href="(.*?)" ...>Let's talk</a>
    # Note: the text might have differences, we use the btn_text variable
    pattern = r'<a href="([^"]+)" target="_blank" style="display: inline-block; padding: 12px 24px; background: transparent; border: 1px solid var\(--cyan-accent\); color: var\(--cyan-accent\); text-decoration: none; border-radius: 4px; text-align: center; font-weight: 600; margin-top: 16px; transition: all 0.2s;" onmouseover="this\.style\.background=\'var\(--cyan-accent\)\'; this\.style\.color=\'var\(--bg-color\)\';" onmouseout="this\.style\.background=\'transparent\'; this\.style\.color=\'var\(--cyan-accent\)\';">([^<]+)</a>'
    
    content = re.sub(pattern, replace_card_btn, content)

    # Some cards in Spanish might use slightly different text like 'Hablar con el Experto', let's just match the style structure
    pattern_generic = r'<a href="([^"]+)" target="_blank" style="display: inline-block; padding: 12px 24px; background: transparent; border: 1px solid var\(--cyan-accent\); color: var\(--cyan-accent\); text-decoration: none; border-radius: 4px; text-align: center; font-weight: 600; margin-top: 16px; transition: all 0.2s;" onmouseover="[^"]+" onmouseout="[^"]+">([^<]+)</a>'
    content = re.sub(pattern_generic, replace_card_btn, content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Files updated successfully!")
