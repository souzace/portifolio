with open("alo-agua/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Remover .st-sub { display: none; } da media query mobile e ajustar tipografia para caber com elegância
css = css.replace('.st-sub { display: none; }', """
    .st-sub {
        display: block !important;
        font-size: 0.7rem !important;
        color: #94A3B8 !important;
        line-height: 1.1;
    }
    .st-title {
        font-size: 0.85rem !important;
    }
    .sticky-avatar {
        width: 40px !important;
        height: 40px !important;
    }
""")

with open("alo-agua/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Texto do subtítulo ativado no mobile com sucesso!")
