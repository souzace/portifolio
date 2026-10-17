import os
import re
import time

version = str(int(time.time()))

# List of all project folders
projects = ['beloton', 'el-bethel', 'ideal', 'nilson-vieira', 'orkes', 'emporio-linneo', 'alo-agua', 'kuroneko-toys', 'barba-shopping', 'picanha-do-savio']

for project in projects:
    html_path = os.path.join(project, 'index.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # 1. Match style.css without or with an existing version query
        pattern_css = r'href="(style\.css)(\?v=[0-9.]+)?([^"]*)"'
        new_content = re.sub(pattern_css, f'href="\\1?v={version}\\3"', content)

        # 2. Match script.js without or with an existing version query
        pattern_js = r'src="(script\.js)(\?v=[0-9.]+)?([^"]*)"'
        new_content = re.sub(pattern_js, f'src="\\1?v={version}\\3"', new_content)
        
        # 3. Quebrar cache de imagens principais no HTML (src="...jpg/png/webp")
        img_pattern = r'src="([^"]+\.(?:jpg|jpeg|png|webp))(\?v=[0-9.]+)?([^"]*)"'
        new_content = re.sub(img_pattern, f'src="\\1?v={version}\\3"', new_content)

        if content != new_content:
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated cache-buster in {html_path}")
        else:
            print(f"No changes needed in {html_path}")

print("Cache busting script completed.")
