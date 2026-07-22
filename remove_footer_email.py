import os

files = ['index.html', 'index-en.html', 'index-es.html']

target_str = """                <a href="mailto:contato@orkes.com.br" style="color: var(--text-muted); text-decoration: none; font-weight: 500; transition: color 0.3s ease;" onmouseover="this.style.color='var(--cyan-accent)'" onmouseout="this.style.color='var(--text-muted)'">
                    contato@orkes.com.br
                </a>\n"""

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # If the exact string is slightly different (e.g. spaces), let's use a regex to be safe
    import re
    pattern = r'\s*<a href="mailto:contato@orkes\.com\.br" style="color: var\(--text-muted\); text-decoration: none; font-weight: 500; transition: color 0\.3s ease;" onmouseover="this\.style\.color=\'var\(--cyan-accent\)\'" onmouseout="this\.style\.color=\'var\(--text-muted\)\'">\s*contato@orkes\.com\.br\s*</a>'
    
    content = re.sub(pattern, '', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Email link removed from footer-links successfully!")
