import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace .social-icon CSS
old_css = """        .social-icon {
            color: #fff;
            transition: color 0.3s;
            display: flex;
        }"""
new_css = """        .social-icon {
            color: #fff;
            transition: color 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            padding: 5px;
        }
        .social-container {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
        }
"""
html = html.replace(old_css, new_css)

# Update the wrapper div
html = html.replace('<div style="display: flex; align-items: center; gap: 15px;">', '<div class="social-container">')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("IG alignment fixed.")
