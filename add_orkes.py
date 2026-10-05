import re

with open("el-bethel/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add Orkes credit to the footer
old_copy = '<p>&copy; 2026 Óptica El Bethel. Todos os direitos reservados.</p>'
new_copy = '<p>&copy; 2026 Óptica El Bethel. Todos os direitos reservados.</p>\n            <p style="margin-top: 0.5rem; font-size: 0.75rem; color: #888;">Desenvolvido por <a href="https://orkes.com.br" target="_blank" style="color: #888; text-decoration: underline;">Orkes</a></p>'

html = html.replace(old_copy, new_copy)

with open("el-bethel/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Orkes added.")
