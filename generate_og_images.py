import asyncio
from playwright.async_api import async_playwright
import os

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            margin: 0;
            padding: 0;
            background-color: #050505;
            width: 1200px;
            height: 630px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            color: #ffffff;
            text-align: center;
            box-sizing: border-box;
            padding: 40px;
        }}
        .logo {{
            width: 150px;
            height: 150px;
            border-radius: 20px;
            margin-bottom: 40px;
            object-fit: cover;
            border: 2px solid #00E5FF;
            box-shadow: 0 0 40px rgba(0, 229, 255, 0.2);
        }}
        h1 {{
            font-size: 56px;
            font-weight: 700;
            margin: 0 0 20px 0;
            color: #ffffff;
            letter-spacing: -0.5px;
        }}
        h2 {{
            font-size: 32px;
            font-weight: 400;
            color: #a0a0a0;
            margin: 0;
            max-width: 900px;
            line-height: 1.4;
        }}
        .accent {{
            color: #00E5FF;
        }}
    </style>
</head>
<body>
    <img src="file:///{logo_path}" class="logo">
    <h1>{title}</h1>
    <h2>{description}</h2>
</body>
</html>
"""

async def generate_images():
    logo_path = os.path.abspath('social-media/logo/logo-quadrada.jpg').replace('\\', '/')
    
    en_html = html_template.format(
        logo_path=logo_path,
        title="Orkes | <span class='accent'>Software Engineering</span> & IT Consulting",
        description="Software Engineer specialized in Architecture, Critical Systems, and DevOps."
    )
    
    es_html = html_template.format(
        logo_path=logo_path,
        title="Orkes | <span class='accent'>Ingeniería de Software</span> y TI",
        description="Ingeniero de Software especialista en Arquitectura, Sistemas Críticos y DevOps."
    )
    
    with open('temp_en.html', 'w', encoding='utf-8') as f:
        f.write(en_html)
    with open('temp_es.html', 'w', encoding='utf-8') as f:
        f.write(es_html)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1200, 'height': 630})
        
        await page.goto(f"file:///{os.path.abspath('temp_en.html').replace(chr(92), '/')}")
        await page.wait_for_load_state("networkidle")
        await page.screenshot(path="social-media/og-image-en.jpg", type="jpeg", quality=90)
        
        await page.goto(f"file:///{os.path.abspath('temp_es.html').replace(chr(92), '/')}")
        await page.wait_for_load_state("networkidle")
        await page.screenshot(path="social-media/og-image-es.jpg", type="jpeg", quality=90)
        
        await browser.close()
        
    os.remove('temp_en.html')
    os.remove('temp_es.html')
    print("Images generated successfully!")

if __name__ == "__main__":
    asyncio.run(generate_images())
