import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace Hero Background
html = re.sub(
    r"url\('https://images\.unsplash\.com/photo-1465847899084-d164df4dedc6\?auto=format&fit=crop&w=1200&q=80'\)",
    r"url('photo4.jpg')",
    html
)

# Replace Regência Image
html = re.sub(
    r'<img src="https://images\.unsplash\.com/photo-1514320291840-2e0a9bf2a9ae\?auto=format&fit=crop&w=600&q=80" alt="Regência de Orquestras">',
    r'<img src="photo5.jpg" alt="Regência de Orquestras" style="object-position: top;">',
    html
)

# Replace Arranjos Image
html = re.sub(
    r'<img src="https://images\.unsplash\.com/photo-1507838153414-b4b713384a76\?auto=format&fit=crop&w=600&q=80" alt="Arranjos Musicais">',
    r'<img src="photo1.jpg" alt="Arranjos Musicais">',
    html
)

# Replace Autoral Image
html = re.sub(
    r'<img src="https://images\.unsplash\.com/photo-1520523839897-bd0b52f945a0\?auto=format&fit=crop&w=600&q=80" alt="Composições Autorais">',
    r'<img src="photo3.jpg" alt="Composições Autorais">',
    html
)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Photos replaced.")
