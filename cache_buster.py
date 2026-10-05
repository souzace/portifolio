import os
import re
import time

version = str(int(time.time()))

# List of all project folders
projects = ['beloton', 'el-bethel', 'ideal', 'nilson-vieira', 'orkes']

for project in projects:
    html_path = os.path.join(project, 'index.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Match style.css without or with an existing version query
        # This regex matches href="style.css" or href="style.css?v=..."
        pattern = r'href="(style\.css)(\?v=[0-9.]+)?([^"]*)"'
        
        # Replace with new timestamp
        new_content = re.sub(pattern, f'href="\\1?v={version}\\3"', content)
        
        if content != new_content:
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated cache-buster in {html_path}")
        else:
            print(f"No changes needed or style.css not found in {html_path}")

print("Cache busting script completed.")
