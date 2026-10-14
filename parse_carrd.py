import re

with open("/home/fsouza/.gemini/antigravity-cli/brain/f889fbae-fa01-4f54-81c2-1a2c07cf5799/.system_generated/steps/1481/content.md", "r", encoding="utf-8") as f:
    text = f.read()

# Extrair todos os links href
links = re.findall(r'href="([^"]+)"', text)
print("LINKS ENCONTRADOS NO CARRD:")
for l in set(links):
    if not l.startswith("data:") and not "fonts.googleapis" in l and not "carrd.co" in l:
        print("->", l)

# Extrair textos dos botões / títulos
headings = re.findall(r'>([^<]{3,60})<', text)
clean_headings = [h.strip() for h in headings if h.strip() and not h.startswith("window.") and not "{" in h]
print("\nTEXTOS ENCONTRADOS:")
for h in set(clean_headings[:40]):
    print("-", h)
