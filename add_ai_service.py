import sys, re

def add_ai_service():
    files = {
        'index.html': {
            'search': 'Soluções B2C',
            'title': 'Inteligência Artificial',
            'sub': 'Automação & GenAI',
            'desc': 'Integração de LLMs (OpenAI, Gemini) e agentes autônomos para automatizar processos e escalar operações de forma inteligente.',
            'btn': 'Bora conversar',
            'link': 'https://wa.me/5585991634033?text=Ol%C3%A1%20F%C3%A1bio%2C%20acessei%20o%20seu%20portf%C3%B3lio%20e%20gostaria%20de%20conversar%20sobre%20IA.'
        },
        'index-en.html': {
            'search': 'B2C Solutions',
            'title': 'Artificial Intelligence',
            'sub': 'Automation & GenAI',
            'desc': 'Integration of LLMs (OpenAI, Gemini) and autonomous agents to automate processes and scale operations intelligently.',
            'btn': 'Let\'s talk',
            'link': 'https://wa.me/5585991634033?text=Hello%20Fabio,%20I%20accessed%20your%20portfolio%20and%20would%20like%20to%20talk%20about%20AI.'
        },
        'index-es.html': {
            'search': 'Soluciones B2C',
            'title': 'Inteligencia Artificial',
            'sub': 'Automatización & GenAI',
            'desc': 'Integración de LLMs (OpenAI, Gemini) y agentes autónomos para automatizar procesos y escalar operaciones de manera inteligente.',
            'btn': 'Hablemos',
            'link': 'https://wa.me/5585991634033?text=Hola%20Fabio,%20acced%C3%AD%20a%20tu%20portafolio%20y%20me%20gustar%C3%ADa%20hablar%20sobre%20IA.'
        }
    }
    
    icon_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="var(--cyan-accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line></svg>'
    
    for filename, texts in files.items():
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find the B2C card block to use as reference for insertion
        # We will split at the end of the B2C card and insert the new one
        # Because we don't have a reliable marker, we will find the B2C title, 
        # then find the closing </div> of that card.
        
        # We look for the exact button of the B2C card.
        # Actually, let's just find the exact block for B2C and append.
        
        # A simple way to append is to find the closing div of the B2C card
        # which is followed by </div>\n                </div>\n                  <button class="carousel-btn left"
        
        # Let's use regex to find the end of the services-grid inside the #servicos section
        # The easiest is to insert right before the closing tag of .services-grid
        # But wait, there are TWO carousels! One for Services and one for Success Stories.
        # We only want to append to the FIRST one.
        
        new_card = f"""
                    <div class="service-card" style="padding: 32px; text-align: left; background: var(--bg-card); border-radius: 8px; border: 1px solid var(--border-color); display: flex; flex-direction: column; gap: 16px;">
                        <div style="margin-bottom: 8px;">{icon_svg}</div>
                        <h3 style="font-size: 1.25rem; color: var(--text-main); margin: 0;">{texts['title']}</h3>
                        <div style="color: var(--cyan-accent); font-size: 0.9rem; font-weight: 600;">{texts['sub']}</div>
                        <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6; flex: 1;">{texts['desc']}</p>
                        <a href="{texts['link']}" target="_blank" style="display: inline-block; padding: 12px 24px; background: transparent; border: 1px solid var(--cyan-accent); color: var(--cyan-accent); text-decoration: none; border-radius: 4px; text-align: center; font-weight: 600; margin-top: 16px; transition: all 0.2s;" onmouseover="this.style.background='var(--cyan-accent)'; this.style.color='var(--bg-color)';" onmouseout="this.style.background='transparent'; this.style.color='var(--cyan-accent)';">{texts['btn']}</a>
                    </div>
"""
        
        # Find the position of the B2C card title
        b2c_pos = content.find(texts['search'])
        if b2c_pos != -1:
            # Find the next </a></div> which closes the B2C card
            end_of_b2c = content.find('</a>\n                    </div>', b2c_pos)
            if end_of_b2c != -1:
                insert_pos = end_of_b2c + len('</a>\n                    </div>')
                content = content[:insert_pos] + new_card + content[insert_pos:]
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Added AI card to {filename}")
            else:
                print(f"Could not find end of B2C card in {filename}")
        else:
            print(f"Could not find B2C card in {filename}")

add_ai_service()
