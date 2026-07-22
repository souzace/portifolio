import os

files = ['index.html', 'index-en.html', 'index-es.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # The missing div is before </section> of what-i-do.
    # Currently it looks like:
    #               </div>
    #           </section>
    # 
    #     <!-- ETAPA 4.3: Projetos -->
    
    # We will just replace </section>\n\n    <!-- ETAPA 4.3: Projetos --> 
    # with </div>\n</section>\n\n    <!-- ETAPA 4.3: Projetos -->
    
    # Let's find </section> after what-i-do
    start_idx = content.find('<section id="what-i-do"')
    if start_idx != -1:
        end_idx = content.find('</section>', start_idx)
        if end_idx != -1:
            # Add the missing </div> right before </section>
            content = content[:end_idx] + '</div>\n          ' + content[end_idx:]

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Missing div fixed!")
