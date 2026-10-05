import re

with open("nilson-vieira/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the HTML for about section
about_match = re.search(r'<div class="about-section">.*?</div>\n</div>', html, re.DOTALL)
if about_match:
    old_about_html = about_match.group(0)
    
    new_about_html = """<div class="about-section">
    <div class="about-container">
        <div class="about-photo">
            <img src="photo6.png" alt="Nilson Vieira">
        </div>
        <div class="about-text">
            <h2 class="section-title" style="margin-top: 0; text-align: left;">Sobre Mim</h2>
            <p style="font-size: 1.3rem; color: var(--text-main); font-weight: bold;">Prazer, sou o músico Nilson Vieira!</p>
            <p>Sou carioca, atualmente morando em Fortaleza onde presto serviço nas Forças Armadas. Uma pessoa em constante alegria que encontrou na música a verdadeira vocação.</p>
            <p>Sou bacharel em Composição Musical pela Universidade de Brasília (UnB) e aluno do mestrado em Música pela mesma instituição, além de possuir cursos de especialização em outras áreas relacionadas à música e à docência.</p>
            <p>Toco alguns instrumentos e atuo como regente, porém, <strong>a minha grande especialidade é criar arranjos e composições musicais</strong>. Desafios me movem: tenho boa percepção musical para encontrar soluções e descobrir novos talentos. Por ser um profissional curioso, estou em constante aprendizado.</p>
            <p>Para você que está chegando, seja bem-vindo(a)! Aqui irei compartilhar meu trabalho, parcerias, percepções, experiências e tudo que o universo musical me permitir explorar.</p>
        </div>
    </div>
</div>"""
    html = html.replace(old_about_html, new_about_html)


# Update CSS
old_about_css = re.search(r'\.about-section \{.*?\.about-content p \{.*?\}', html, re.DOTALL)
if old_about_css:
    new_about_css = """.about-section {
            background-color: var(--brand-dark);
            padding: 2rem 2rem 5rem 2rem; /* Reduced top padding to bring it closer to hero */
        }
        .about-container {
            max-width: 1100px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 3rem;
        }
        @media (min-width: 768px) {
            .about-container {
                flex-direction: row;
                align-items: center; /* Center vertically relative to text */
            }
        }
        .about-photo {
            flex: 1;
            width: 100%;
            max-width: 400px;
        }
        .about-photo img {
            width: 100%;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            border: 2px solid rgba(212, 175, 55, 0.2);
            object-fit: cover;
        }
        .about-text {
            flex: 1;
            text-align: left;
        }
        .about-text p {
            font-size: 1.15rem;
            line-height: 1.8;
            color: var(--text-muted);
            margin-bottom: 1.5rem;
        }"""
    html = html.replace(old_about_css.group(0), new_about_css)

with open("nilson-vieira/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("About section layout updated.")
