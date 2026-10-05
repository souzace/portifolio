import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

old_about = """<h2 class="section-title" style="margin-top: 0;">Sobre o Maestro</h2>
        <p>Com uma carreira sólida e apaixonada pela música, Nilson Vieira atua como maestro e diretor musical, liderando orquestras e espetáculos por todo o Brasil. Sua sensibilidade única o tornou um dos arranjadores mais requisitados por grandes vozes da nossa música.</p>
        <p>Além de moldar o som de outros artistas, Nilson dedica-se à criação de obras autorais, mesclando a erudição da música clássica com a alma vibrante da música brasileira.</p>"""

new_about = """<h2 class="section-title" style="margin-top: 0;">Sobre Mim</h2>
        <p style="font-size: 1.3rem; color: var(--text-main); font-weight: bold;">Prazer, sou o músico Nilson Vieira!</p>
        <p>Sou carioca, atualmente morando em Fortaleza onde presto serviço nas Forças Armadas. Uma pessoa em constante alegria que encontrou na música a verdadeira vocação.</p>
        <p>Sou bacharel em Composição Musical pela Universidade de Brasília (UnB) e aluno do mestrado em Música pela mesma instituição, além de possuir cursos de especialização em outras áreas relacionadas à música e à docência.</p>
        <p>Toco alguns instrumentos e atuo como regente, porém, <strong>a minha grande especialidade é criar arranjos e composições musicais</strong>. Desafios me movem: tenho boa percepção musical para encontrar soluções e descobrir novos talentos. Por ser um profissional curioso, estou em constante aprendizado.</p>
        <p>Para você que está chegando, seja bem-vindo(a)! Aqui irei compartilhar meu trabalho, parcerias, percepções, experiências e tudo que o universo musical me permitir explorar.</p>"""

html = html.replace(old_about, new_about)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("About section updated.")
