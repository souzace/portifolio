import sys, re

def update_all_zigzag():
    files = {
        'index.html': {
            'r1_text': 'Sou <strong>Fábio Souza</strong>, parceiro estratégico de engenharia por trás da <strong>Orkes</strong>. O propósito da marca é transformar complexidade técnica em operações corporativas seguras, escaláveis e ininterruptas.',
            'r1_comp': '<strong>Competências Principais:</strong> Modernização de Legados &bull; APIs de Alta Performance &bull; Arquitetura Cloud (AWS)',
            'r2_text': '<strong style="color: var(--text-main); font-size: 1.125rem; display: block; margin-bottom: 12px;">Visão Sistêmica & Resiliência</strong>Com 27 anos de tecnologia, construí uma visão de ponta a ponta para prever falhas estruturais antes que aconteçam.<br><br>A expertise da Orkes é blindar sua operação, eliminando gargalos de performance e construindo a fundação ideal para escalar.',
            'r3_quote': 'Tocar em uma orquestra exige alinhar várias frentes para garantir a harmonia perfeita. Como trombonista, levo essa mesma dinâmica para o desenvolvimento: atenção cirúrgica a cada linha de código, alinhamento constante e foco absoluto em evitar retrabalhos.',
            'r4_title': 'Pronto para escalar sua operação?',
            'r4_desc': 'Se a tecnologia atual gargala o crescimento do seu negócio, é hora de agir. Vamos conversar sobre como preparar sua infraestrutura para o próximo nível.',
            'r4_btn': 'Falar com o Especialista',
            'r4_link': 'https://wa.me/5585991634033?text=Ol%C3%A1%20F%C3%A1bio%2C%20acessei%20o%20seu%20portf%C3%B3lio%20e%20gostaria%20de%20conversar%20sobre%20como%20escalar%20minha%20opera%C3%A7%C3%A3o.'
        },
        'index-en.html': {
            'r1_text': 'I am <strong>Fábio Souza</strong>, the strategic engineering partner behind <strong>Orkes</strong>. The brand\'s purpose is to transform technical complexity into secure, scalable, and uninterrupted corporate operations.',
            'r1_comp': '<strong>Core Competencies:</strong> Legacy Modernization &bull; High-Performance APIs &bull; Cloud Architecture (AWS)',
            'r2_text': '<strong style="color: var(--text-main); font-size: 1.125rem; display: block; margin-bottom: 12px;">Systemic Vision & Resilience</strong>With 27 years in technology, I\'ve built an end-to-end vision to foresee structural failures before they happen.<br><br>Orkes\' expertise is to bulletproof your operation, eliminating performance bottlenecks and building the ideal foundation to scale.',
            'r3_quote': 'Playing in an orchestra requires aligning multiple fronts to ensure perfect harmony. As a trombonist, I bring this dynamic to development: surgical attention to every line of code, constant alignment, and absolute focus on avoiding rework.',
            'r4_title': 'Ready to scale your operation?',
            'r4_desc': 'If your current technology bottlenecks your business growth, it\'s time to act. Let\'s talk about preparing your infrastructure for the next level.',
            'r4_btn': 'Talk to the Expert',
            'r4_link': 'https://wa.me/5585991634033?text=Hello%20Fabio,%20I%20accessed%20your%20portfolio%20and%20would%20like%20to%20talk%20about%20scaling%20my%20operation.'
        },
        'index-es.html': {
            'r1_text': 'Soy <strong>Fábio Souza</strong>, el socio estratégico de ingeniería detrás de <strong>Orkes</strong>. El propósito de la marca es transformar la complejidad técnica en operaciones corporativas seguras, escalables e ininterrumpidas.',
            'r1_comp': '<strong>Competencias Principales:</strong> Modernización de Legados &bull; APIs de Alto Rendimiento &bull; Arquitectura Cloud (AWS)',
            'r2_text': '<strong style="color: var(--text-main); font-size: 1.125rem; display: block; margin-bottom: 12px;">Visión Sistémica y Resiliencia</strong>Con 27 años en tecnología, he construido una visión integral para prever fallas estructurales antes de que ocurran.<br><br>La experiencia de Orkes es blindar su operación, eliminando cuellos de botella y construyendo la base ideal para escalar.',
            'r3_quote': 'Tocar en una orquesta exige alinear múltiples frentes para asegurar la armonía perfecta. Como trombonista, llevo esta dinámica al desarrollo: atención quirúrgica a cada línea de código, alineación constante y enfoque absoluto en evitar retrabajos.',
            'r4_title': '¿Listo para escalar su operación?',
            'r4_desc': 'Si su tecnología actual limita el crecimiento de su negocio, es hora de actuar. Hablemos sobre cómo preparar su infraestructura para el próximo nivel.',
            'r4_btn': 'Hablar con el Experto',
            'r4_link': 'https://wa.me/5585991634033?text=Hola%20Fabio,%20acced%C3%AD%20a%20tu%20portafolio%20y%20me%20gustar%C3%ADa%20hablar%20sobre%20c%C3%B3mo%20escalar%20mi%20operaci%C3%B3n.'
        }
    }
    
    for filename, texts in files.items():
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # We need to replace the content of the zigzag section.
        # It starts at `<div class="sobre-zigzag">` and ends at `</div>` before `<div id="contato"`
        # Actually it's easier to find the exact blocks and replace them.
        
        # Let's replace CSS for image size first!
        # Change .zigzag-photo { flex: 1; -> flex: 0.7;
        # Change .zigzag-text { flex: 1.2; -> flex: 1.3;
        content = content.replace('.zigzag-photo { flex: 1;', '.zigzag-photo { flex: 0.7;')
        content = content.replace('.zigzag-text { flex: 1.2;', '.zigzag-text { flex: 1.3;')
        
        # Now construct the entire new sobre-zigzag
        new_zigzag = f"""<div class="sobre-zigzag">
                  <!-- Row 1: Photo Left, Text Right -->
                  <div class="zigzag-row">
                      <div class="zigzag-photo">
                          <img src="foto3.jpeg" alt="Fabio Souza Developer">
                      </div>
                      <div class="zigzag-text info-card" style="background: var(--bg-card); padding: 32px; border-radius: 8px; border: 1px solid var(--border-color); border-right: 4px solid var(--cyan-accent); display: flex; flex-direction: column; justify-content: center;">
                          <p style="color: var(--text-main); margin-bottom: 16px; font-size: 1.125rem; font-weight: 500;">
                              {texts['r1_text']}
                          </p>
                          <div style="color: var(--text-muted); font-size: 1rem; line-height: 1.6;">
                              {texts['r1_comp']}
                          </div>
                      </div>
                  </div>
                  <!-- Row 2: Text Left, Photo Right -->
                  <div class="zigzag-row reverse">
                      <div class="zigzag-photo">
                          <img src="foto7.jpeg" alt="Fabio Souza Trombonist" style="object-position: center center;">
                      </div>
                      <div class="zigzag-text info-card" style="background: var(--bg-card); padding: 32px; border-radius: 8px; border: 1px solid var(--border-color); border-left: 4px solid var(--cyan-accent); display: flex; flex-direction: column; justify-content: center;">
                          <div style="color: var(--text-muted); font-size: 1rem; line-height: 1.6;">
                              {texts['r2_text']}
                          </div>
                      </div>
                  </div>
                  <!-- Row 3: Photo Left, Text Right -->
                  <div class="zigzag-row">
                      <div class="zigzag-photo">
                          <img src="foto5.jpg" alt="Orchestra Trombone" style="object-position: center 70%;">
                      </div>
                      <div class="zigzag-text quote-container" style="position: relative; background: var(--bg-card); padding: 32px; border-radius: 8px; border: 1px solid var(--border-color); border-right: 4px solid var(--cyan-accent); display: flex; flex-direction: column; justify-content: center;">
                          <span style="position: absolute; top: 16px; left: 16px; font-size: 4rem; color: var(--cyan-accent); font-family: Georgia, serif; line-height: 0.8; opacity: 1;">&ldquo;</span>
                          <p class="quote-text" style="font-size: 1rem; color: var(--text-main); font-style: italic; line-height: 1.6; position: relative; z-index: 1; padding-left: 32px; margin: 0;">
                              {texts['r3_quote']}
                          </p>
                      </div>
                  </div>
                  <!-- Row 4: Text Left, Photo Right (CTA) -->
                  <div class="zigzag-row reverse">
                      <div class="zigzag-photo">
                          <img src="foto9_cta.jpg" alt="Developer coding in VSCode" style="object-position: center;">
                      </div>
                      <div class="zigzag-text info-card" style="background: var(--bg-card); padding: 32px; border-radius: 8px; border: 1px solid var(--border-color); border-left: 4px solid var(--cyan-accent); display: flex; flex-direction: column; justify-content: center; align-items: flex-start;">
                          <h3 style="color: var(--text-main); font-size: 1.4rem; margin-bottom: 16px; margin-top: 0;">{texts['r4_title']}</h3>
                          <p style="color: var(--text-muted); font-size: 1rem; line-height: 1.6; margin-bottom: 24px;">{texts['r4_desc']}</p>
                          <a href="{texts['r4_link']}" target="_blank" class="cta-btn" style="display: inline-flex; align-items: center; gap: 8px; font-size: 0.95rem; padding: 12px 24px; border-radius: 4px; font-weight: 600; text-decoration: none;">
                              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                              {texts['r4_btn']}
                          </a>
                      </div>
                  </div>
              </div>"""
        
        # Regex to match the whole block from <div class="sobre-zigzag"> to the end of Row 4
        # Since I might have nested divs, I can use split based on known strings
        start_marker = '<div class="sobre-zigzag">'
        end_marker = '<!-- End of sobre-zigzag or container -->'
        
        # In current HTML, the zigzag section ends with:
        #                  </div>
        #            </div>
        #        </div>
        #    </section>
        
        start_idx = content.find(start_marker)
        # Search for </section> after start_idx
        end_section_idx = content.find('</section>', start_idx)
        # The closing tag of `div class="container"` is right before `</section>`
        
        # A safer way is to find the exact text of the last row's button to find the end of the zigzag
        
        if start_idx != -1:
            # We want to replace from start_idx up to the closing div of sobre-zigzag
            # Let's find `<section id="contato"` which comes immediately after the sobre-layout
            contato_idx = content.find('<section id="contato"', start_idx)
            if contato_idx != -1:
                # The section ends some divs before. We can extract what's between `<div class="sobre-zigzag">` and the closing `</div>` that is before `</section>` or `<div class="tags-container">`
                
                # Using regex to extract the block
                block_pattern = r'<div class="sobre-zigzag">[\s\S]*?<!-- Row 4: Text Left, Photo Right \(CTA\) -->[\s\S]*?</a>\s*</div>\s*</div>\s*</div>'
                match = re.search(block_pattern, content)
                if match:
                    content = content[:match.start()] + new_zigzag + content[match.end():]
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated About Me completely in {filename}")
                else:
                    print(f"Could not regex match block in {filename}")

update_all_zigzag()
