import sys

def tweak_music_text():
    files = {
        'index.html': {
            'old': '(E, sim, a inspiração vem da minha atuação como músico de orquestra).',
            'new': '(...e sim, sou músico de orquestra nas horas vagas).'
        },
        'index-en.html': {
            'old': '(And yes, the inspiration comes from my background as an orchestra musician).',
            'new': '(...and yes, I am an orchestra musician in my spare time).'
        },
        'index-es.html': {
            'old': '(Y sí, la inspiración proviene de mi experiencia como músico de orquesta).',
            'new': '(...y sí, soy músico de orquesta en mi tiempo libre).'
        }
    }
    
    for filename, texts in files.items():
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace(texts['old'], texts['new'])
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated music text in {filename}")

tweak_music_text()
