with open("kuroneko-toys/index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if '<div class="header-actions">' in line:
        skip = True
        new_lines.append('            <div class="header-right-store">\n')
        new_lines.append('                <div class="store-comic-badge">STORE</div>\n')
        new_lines.append('            </div>\n')
        continue
    if skip and '</div>' in line:
        skip = False
        continue
    if not skip:
        new_lines.append(line)

with open("kuroneko-toys/index.html", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Header actions removido e substituído por store-comic-badge!")
