import os
import re

files = ['index.html', 'index-en.html', 'index-es.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update JSON-LD sameAs
    # Look for: "https://www.linkedin.com/in/souzace"
    if '"https://www.linkedin.com/in/souzace"' in content and '"https://instagram.com/orkestech"' not in content:
        content = content.replace(
            '"https://www.linkedin.com/in/souzace"\n      ]',
            '"https://www.linkedin.com/in/souzace",\n            "https://instagram.com/orkestech"\n      ]'
        )
        # just in case the spaces are different:
        content = content.replace(
            '"https://www.linkedin.com/in/souzace"\n        ]',
            '"https://www.linkedin.com/in/souzace",\n            "https://instagram.com/orkestech"\n        ]'
        )

    # 2. Add Instagram icon to sticky footer
    # Look for the linkedin a tag
    linkedin_a_tag = '''<a href="https://www.linkedin.com/in/souzace" target="_blank" style="color: var(--text-muted); text-decoration: none; font-weight: 500; transition: color 0.3s ease;" onmouseover="this.style.color='var(--cyan-accent)'" onmouseout="this.style.color='var(--text-muted)'">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                </a>'''
    
    instagram_a_tag = '''<a href="https://instagram.com/orkestech" target="_blank" style="color: var(--text-muted); text-decoration: none; font-weight: 500; transition: color 0.3s ease;" onmouseover="this.style.color='var(--cyan-accent)'" onmouseout="this.style.color='var(--text-muted)'" aria-label="Instagram">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                </a>'''

    if linkedin_a_tag in content and 'href="https://instagram.com/orkestech"' not in content:
        content = content.replace(linkedin_a_tag, linkedin_a_tag + '\n                ' + instagram_a_tag)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Instagram added!")
