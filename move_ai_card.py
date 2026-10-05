import sys, re

def move_ai_card():
    files = {
        'index.html': {
            'ai_title': 'Inteligência Artificial',
            'b2b_title': 'Integração B2B'
        },
        'index-en.html': {
            'ai_title': 'Artificial Intelligence',
            'b2b_title': 'B2B Integration'
        },
        'index-es.html': {
            'ai_title': 'Inteligencia Artificial',
            'b2b_title': 'Integración B2B'
        }
    }
    
    for filename, texts in files.items():
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Regex to find the entire AI service card
        # It starts with <div class="service-card"... and ends with </a>\n                    </div>
        ai_pattern = r'(\s*<div class="service-card"[^>]*>.*?<h3[^>]*>' + re.escape(texts['ai_title']) + r'</h3>.*?</a>\s*</div>\n?)'
        
        ai_match = re.search(ai_pattern, content, re.DOTALL)
        if not ai_match:
            print(f"Could not find AI card in {filename}")
            continue
            
        ai_card_html = ai_match.group(1)
        
        # Remove AI card from current position
        content = content.replace(ai_card_html, '')
        
        # Regex to find the B2B Integration card
        # We want to insert the AI card right before this block
        b2b_pattern = r'(\s*<div class="service-card"[^>]*>.*?<h3[^>]*>' + re.escape(texts['b2b_title']) + r'</h3>)'
        
        b2b_match = re.search(b2b_pattern, content, re.DOTALL)
        if not b2b_match:
            print(f"Could not find B2B Integration card in {filename}")
            # put it back if B2B is not found
            content += ai_card_html 
            continue
            
        insert_pos = b2b_match.start(1)
        
        # Insert AI card before B2B Integration card
        content = content[:insert_pos] + ai_card_html + content[insert_pos:]
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Moved AI card before {texts['b2b_title']} in {filename}")

move_ai_card()
