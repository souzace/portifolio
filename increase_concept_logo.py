with open("alo-agua/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Aumentar a altura do concept-logo de 60px para 90px e ajustar padding do header se necessário
css = css.replace('height: 60px !important;', 'height: 90px !important;')

# Aumentar também o avatar da barra fixa flutuante para destacar o novo símbolo
css = css.replace('width: 46px;\n    height: 46px;', 'width: 58px;\n    height: 58px;')

with open("alo-agua/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Tamanho do logotipo aumentado com sucesso.")
