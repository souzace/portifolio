import os
import re

files = ['index.html', 'index-en.html', 'index-es.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change border-radius: 100px to border-radius: 4px in .cta-btn CSS
    # It looks like: border-radius: 100px;
    content = re.sub(r'border-radius:\s*100px;', 'border-radius: 4px;', content)
    
    # Just in case, if the footer button has inline style without border-radius, it will now inherit 4px.
    # The middle buttons already have inline border-radius: 4px, which is fine, they will keep it.

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Border radius updated to 4px successfully!")
