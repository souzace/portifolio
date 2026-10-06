import shutil

# Copiar a versão melhorada em alta definição do mascote original
shutil.copy("/home/fsouza/.gemini/antigravity-cli/brain/f889fbae-fa01-4f54-81c2-1a2c07cf5799/alo_agua_logo_vetorial_1791303110368.jpg", "alo-agua/logo_mascote_moderno.jpg")

with open("alo-agua/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Atualizar no index.html
html = html.replace('src="logo_conceito3.jpg"', 'src="logo_mascote_moderno.jpg"')

with open("alo-agua/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("alo-agua/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Ajustar tamanho para o mascote ter destaque no cabeçalho
css = css.replace('height: 90px !important;', 'height: 95px !important;')

with open("alo-agua/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Mascote original melhorado restaurado com sucesso.")
