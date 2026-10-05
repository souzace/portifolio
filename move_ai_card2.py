import sys, re

def move_ai():
    files = {
        'index.html': ('Inteligência Artificial', 'Integração B2B'),
        'index-en.html': ('Artificial Intelligence', 'B2B Integration'),
        'index-es.html': ('Inteligencia Artificial', 'Integración B2B')
    }
    
    for filename, (ai_title, b2b_title) in files.items():
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Find AI card
        ai_match = re.search(r'(<div class="service-card"[^>]*>[\s\S]*?<h3[^>]*>' + re.escape(ai_title) + r'</h3>[\s\S]*?</a>\s*</div>)', content)
        if not ai_match:
            print(f"AI card not found in {filename}")
            continue
            
        ai_card = ai_match.group(1)
        
        # 2. Remove AI card from current position
        content = content.replace(ai_card, '')
        
        # 3. Find B2B card start
        b2b_match = re.search(r'(<div class="service-card"[^>]*>[\s\S]*?<h3[^>]*>' + re.escape(b2b_title) + r'</h3>)', content)
        if not b2b_match:
            print(f"B2B card not found in {filename}")
            continue
            
        insert_pos = b2b_match.start(1)
        
        # 4. Insert AI card with some whitespace
        content = content[:insert_pos] + ai_card + '\n                    ' + content[insert_pos:]
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Moved {ai_title} before {b2b_title} in {filename}")

move_ai()
