import os

files = ['index.html', 'index-en.html', 'index-es.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the incorrect URL with the correct one
    content = content.replace('https://instagram.com/orkestech', 'https://instagram.com/orkes.tech')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Instagram URL updated successfully!")
