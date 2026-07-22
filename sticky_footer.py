import os
import re

files = [
    ('index.html', 'Sua operação técnica precisa escalar?', 'Falar comigo'),
    ('index-en.html', 'Ready to scale your operation?', 'Talk with me'),
    ('index-es.html', '¿Su operación técnica necesita escalar?', 'Hablar conmigo')
]

for filename, title_text, btn_text in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the footer block to replace
    start_idx = content.find('<footer>')
    if start_idx != -1:
        end_idx = content.find('</footer>', start_idx)
        if end_idx != -1:
            
            # The new sticky footer HTML
            sticky_footer = f'''
    <style>
        body {{ padding-bottom: 90px; }} /* Give space so content isn't hidden behind the fixed bar */
        
        .sticky-footer-bar {{
            position: fixed; 
            bottom: 0; 
            left: 0; 
            width: 100%; 
            z-index: 999; 
            background: rgba(17, 17, 17, 0.98); 
            backdrop-filter: blur(10px); 
            border-top: 1px solid var(--border-color); 
            padding: 16px 32px; 
            display: flex; 
            align-items: center; 
            justify-content: space-between; 
            box-shadow: 0 -10px 30px rgba(0,0,0,0.6);
        }}
        .sticky-footer-left {{ display: flex; align-items: center; gap: 16px; }}
        .sticky-footer-right {{ display: flex; align-items: center; gap: 32px; }}
        .sticky-footer-title-wrap {{ display: flex; flex-direction: column; }}
        .sticky-footer-title {{ color: var(--text-main); font-weight: 600; font-size: 1.05rem; }}
        .sticky-footer-sub {{ color: var(--text-muted); font-size: 0.8rem; }}
        
        @media (max-width: 900px) {{
            .sticky-footer-bar {{ padding: 12px 16px; flex-direction: column; gap: 12px; }}
            .sticky-footer-left {{ width: 100%; justify-content: center; }}
            .sticky-footer-right {{ width: 100%; justify-content: space-between; gap: 16px; }}
            .sticky-footer-title {{ font-size: 0.95rem; text-align: center; }}
            .sticky-footer-sub {{ display: none; }}
            body {{ padding-bottom: 140px; }}
        }}
    </style>

    <footer class="sticky-footer-bar">
        
        <div class="sticky-footer-left">
            <img src="foto8.jpg" alt="Avatar" style="width: 48px; height: 48px; border-radius: 50%; object-fit: cover; object-position: center 20%; border: 2px solid var(--cyan-accent);">
            <div class="sticky-footer-title-wrap">
                <span class="sticky-footer-title">{title_text}</span>
                <span class="sticky-footer-sub">Orkes® - CNPJ: 41.950.774/0001-60</span>
            </div>
        </div>

        <div class="sticky-footer-right">
            <div style="display: flex; gap: 16px;">
                <a href="https://github.com/souzace" target="_blank" style="color: var(--text-muted); text-decoration: none; font-weight: 500; transition: color 0.3s ease;" onmouseover="this.style.color='var(--cyan-accent)'" onmouseout="this.style.color='var(--text-muted)'">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
                </a>
                <a href="https://www.linkedin.com/in/souzace" target="_blank" style="color: var(--text-muted); text-decoration: none; font-weight: 500; transition: color 0.3s ease;" onmouseover="this.style.color='var(--cyan-accent)'" onmouseout="this.style.color='var(--text-muted)'">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                </a>
                <a href="mailto:contato@orkes.com.br" style="color: var(--text-muted); text-decoration: none; font-weight: 500; transition: color 0.3s ease;" onmouseover="this.style.color='var(--cyan-accent)'" onmouseout="this.style.color='var(--text-muted)'">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                </a>
            </div>
            
            <a href="https://wa.me/5585991634033?text=Ol%C3%A1%20F%C3%A1bio%2C%20acessei%20o%20seu%20portf%C3%B3lio%20e%20gostaria%20de%20conversar%20sobre%20um%20projeto." target="_blank" class="cta-btn" style="display: inline-flex; align-items: center; gap: 8px; padding: 10px 24px; font-size: 0.95rem; white-space: nowrap;">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                {btn_text}
            </a>
        </div>
    </footer>'''

            # Replace the old footer
            content = content[:start_idx] + sticky_footer + content[end_idx + 9:]

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)

print("Sticky footer (Option B) applied successfully!")
