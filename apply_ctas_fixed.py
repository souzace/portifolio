import re

files = [
    ('index.html', 'Bora conversar', 'Ou envie um e-mail para: ', 'https://wa.me/5585991634033?text=Ol%C3%A1%20F%C3%A1bio%2C%20acessei%20o%20seu%20portf%C3%B3lio%20e%20gostaria%20de%20conversar%20sobre%20um%20projeto.'),
    ('index-en.html', "Talk to the Expert", 'Or send an email to: ', 'https://wa.me/5585991634033?text=Hello%20Fabio%2C%20I%20accessed%20your%20portfolio%20and%20would%20like%20to%20talk%20about%20a%20project.'),
    ('index-es.html', 'Hablar con el Experto', 'O env\u00ede un correo electr\u00f3nico a: ', 'https://wa.me/5585991634033?text=Hola%20Fabio%2C%20acced%C3%AD%20a%20tu%20portafolio%20y%20me%20gustar%C3%ADa%20hablar%20sobre%20un%20proyecto.')
]

# We need to remove the exact CTA and email from inside the cards.
# Notice we use re.DOTALL so .* matches newlines.

pattern_btn = r'\s*<a href="[^"]+" target="_blank" class="cta-btn" style="display: inline-flex; align-items: center; justify-content: center; gap: 8px; padding: 12px 24px; background: var\(--cyan-accent\); color: var\(--bg-color\); text-decoration: none; border-radius: 4px; text-align: center; font-weight: 600; margin-top: 16px; transition: all 0\.2s;" onmouseover="[^"]+" onmouseout="[^"]+">.*?</a>\s*<p style="margin-top: 12px; font-size: 0\.85rem; color: var\(--text-muted\); text-align: center;">.*?<a href="mailto:contato@orkes\.com\.br"[^>]+>contato@orkes\.com\.br</a></p>'

for filename, btn_text, email_text, w_link in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # REMOVE FROM CARDS
    content = re.sub(pattern_btn, '', content, flags=re.DOTALL)
    
    # ADD UNIFIED CTA
    unified_cta = f'''
              <div style="text-align: center; margin-top: 56px;">
                  <a href="{w_link}" target="_blank" class="cta-btn" style="display: inline-flex; align-items: center; gap: 8px; font-size: 1.05rem; padding: 14px 32px; border-radius: 4px; font-weight: 600; text-decoration: none;">
                      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="22" height="22" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                      {btn_text}
                  </a>
                  <p style="margin-top: 16px; font-size: 0.95rem; color: var(--text-muted);">{email_text}<a href="mailto:contato@orkes.com.br" style="color: var(--cyan-accent); text-decoration: none; font-weight: 500;">contato@orkes.com.br</a></p>
              </div>'''

    # We need to insert this exactly at the end of <section id="what-i-do">.
    # The end of this section is around lines 964-967. Let's find exactly that.
    # The structure:
    #                   </div>
    #               </div>
    #           </section>
    # 
    #     <!-- ETAPA 4.3: Projetos -->
    
    # We will look for <section id="what-i-do" and then its closing </section>
    
    start_idx = content.find('<section id="what-i-do"')
    if start_idx != -1:
        end_idx = content.find('</section>', start_idx)
        if end_idx != -1:
            # We want to insert the unified CTA right before </section> but inside the <div class="container">... wait, does what-i-do have a container?
            # <section id="what-i-do" style="...">\n        <div class="container">
            # So the structure closes like: </div></div></section>
            
            # Let's find the last </div> before </section> within this block
            block = content[start_idx:end_idx]
            last_div_idx = block.rfind('</div>')
            # wait, actually the carousel-wrapper closes, then the container closes?
            # let's just insert it before the last </div>
            
            # Since the section closes with:
            #                   </div>
            #               </div>
            #           </section>
            
            # Let's insert it before the VERY LAST </div> in the block.
            new_block = block[:last_div_idx] + unified_cta + "\n              " + block[last_div_idx:]
            
            content = content[:start_idx] + new_block + content[end_idx:]

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed CTAs successfully!")
