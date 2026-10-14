with open("kuroneko-toys/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Substituir a paleta de cores para enriquecer com tons de azul profundo (Cyber Blue / Midnight Tokyo)
old_palette = """:root {
    --bg-dark: #0A0B10;
    --bg-card: #12141F;
    --bg-card-hover: #191C2B;
    --purple-neon: #9333EA;
    --purple-glow: rgba(147, 51, 234, 0.4);
    --yellow-neon: #FACC15;
    --yellow-glow: rgba(250, 204, 21, 0.35);
    --cyan-neon: #06B6D4;
    --cyan-glow: rgba(6, 182, 212, 0.35);
    --text-white: #F8FAFC;
    --text-muted: #94A3B8;
    --border-color: rgba(255, 255, 255, 0.1);
    --border-purple: rgba(147, 51, 234, 0.4);
    --wa-green: #22C55E;
    --wa-green-glow: rgba(34, 197, 94, 0.4);
}"""

new_palette = """:root {
    --bg-dark: #060913; /* Azul meia-noite profundo */
    --bg-dark-accent: #0B132B; /* Azul marinho elétrico sutil */
    --bg-card: #0F172A; /* Slate blue moderno */
    --bg-card-hover: #1E293B;
    --cyber-blue: #0EA5E9; /* Azul ciano elétrico brilhante */
    --cyber-blue-glow: rgba(14, 165, 233, 0.45);
    --blue-neon: #2563EB;
    --purple-neon: #8B5CF6;
    --purple-glow: rgba(139, 92, 246, 0.35);
    --yellow-neon: #FACC15;
    --yellow-glow: rgba(250, 204, 21, 0.35);
    --cyan-neon: #06B6D4;
    --cyan-glow: rgba(6, 182, 212, 0.4);
    --text-white: #F8FAFC;
    --text-muted: #94A3B8;
    --border-color: rgba(14, 165, 233, 0.15); /* Bordas com toque de azul sutil */
    --border-blue: rgba(14, 165, 233, 0.4);
    --border-purple: rgba(139, 92, 246, 0.4);
    --wa-green: #22C55E;
    --wa-green-glow: rgba(34, 197, 94, 0.4);
}"""

css = css.replace(old_palette, new_palette)

# Enriquecer o background do body com uma aura azul ambiente
old_body = """body.dark-theme {
    background-color: var(--bg-dark);
    color: var(--text-white);
    font-family: 'Plus Jakarta Sans', sans-serif;
    line-height: 1.6;
    overflow-x: hidden;
}"""

new_body = """body.dark-theme {
    background-color: var(--bg-dark);
    background-image: 
        radial-gradient(circle at 15% 20%, rgba(14, 165, 233, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 85% 60%, rgba(37, 99, 235, 0.07) 0%, transparent 45%),
        radial-gradient(circle at 50% 90%, rgba(139, 92, 246, 0.06) 0%, transparent 50%);
    background-attachment: fixed;
    color: var(--text-white);
    font-family: 'Plus Jakarta Sans', sans-serif;
    line-height: 1.6;
    overflow-x: hidden;
}"""

css = css.replace(old_body, new_body)

# Ajustar o brilho da hero para integrar com azul ciano
css = css.replace('rgba(147, 51, 234, 0.25) 0%, rgba(10, 11, 16, 0) 70%', 'rgba(14, 165, 233, 0.22) 0%, rgba(139, 92, 246, 0.15) 35%, rgba(6, 9, 19, 0) 70%')

# Ajustar o header background
css = css.replace('background-color: rgba(10, 11, 16, 0.85);', 'background-color: rgba(6, 9, 19, 0.85);')

# Ajustar o footer background
css = css.replace('background-color: #06070B;', 'background-color: #04060C;')

# Ajustar a barra fixa flutuante
css = css.replace('background-color: rgba(9, 10, 16, 0.95);', 'background-color: rgba(6, 9, 19, 0.95); border-top: 2px solid var(--cyber-blue); box-shadow: 0 -10px 30px rgba(14, 165, 233, 0.25);')

with open("kuroneko-toys/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Tons de azul aplicados com sucesso mantendo a harmonia neon!")
