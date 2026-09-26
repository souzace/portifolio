import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace Hero Image
html = re.sub(r"url\('https://images\.unsplash\.com/[^']+'\)", "url('photo1.webp')", html)

# Replace Service 1
html = re.sub(r'src="https://images\.unsplash\.com/[^"]+" alt="Bolos Tradicionais"', 'src="photo2.webp" alt="Bolos Tradicionais"', html)

# Replace Service 2
html = re.sub(r'src="https://images\.unsplash\.com/[^"]+" alt="Bolos Vulcão"', 'src="photo3.webp" alt="Bolos Vulcão"', html)

# Replace Service 3
html = re.sub(r'src="https://images\.unsplash\.com/[^"]+" alt="Para o Café da Tarde"', 'src="photo4.webp" alt="Para o Café da Tarde"', html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Photos updated.")
