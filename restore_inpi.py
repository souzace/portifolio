import os

files = [
    ('index.html', 'INPI', '<a href="https://busca.inpi.gov.br/pePI/" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color=\'var(--cyan-accent)\'" onmouseout="this.style.color=\'inherit\'"><abbr title="Instituto Nacional da Propriedade Industrial - Brasil" style="cursor: help; text-decoration: none; border-bottom: 1px dotted rgba(255,255,255,0.3);">INPI</abbr></a>'),
    ('index-en.html', 'INPI', '<a href="https://busca.inpi.gov.br/pePI/" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color=\'var(--cyan-accent)\'" onmouseout="this.style.color=\'inherit\'"><abbr title="Instituto Nacional da Propriedade Industrial - Brasil" style="cursor: help; text-decoration: none; border-bottom: 1px dotted rgba(255,255,255,0.3);">INPI</abbr></a>'),
    ('index-es.html', 'INPI', '<a href="https://busca.inpi.gov.br/pePI/" target="_blank" rel="noopener noreferrer" style="color: inherit; text-decoration: none;" onmouseover="this.style.color=\'var(--cyan-accent)\'" onmouseout="this.style.color=\'inherit\'"><abbr title="Instituto Nacional da Propriedade Industrial - Brasil" style="cursor: help; text-decoration: none; border-bottom: 1px dotted rgba(255,255,255,0.3);">INPI</abbr></a>')
]

for filename, old_text, new_html in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # The string to target is exactly 'INPI 917789873' to avoid replacing other INPI mentions (like in JSON-LD)
    target = 'INPI 917789873'
    replacement = f'{new_html} 917789873'
    
    content = content.replace(target, replacement)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Tooltip and link for INPI restored successfully!")
