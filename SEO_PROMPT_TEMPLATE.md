# Prompt de Otimização SEO Técnico Avançado

Este prompt foi desenhado para replicar o sucesso de engenharia SEO do site Orkes.tech em outros projetos.
**Instruções de Uso:** Copie o texto abaixo, cole no seu assistente de IA (como o Gemini) e coloque o código fonte do seu outro site no final.

---

Atue como um Especialista Sênior em SEO Técnico e Engenharia Frontend. 

Eu tenho o código HTML de um site e preciso que você aplique uma auditoria e refatoração agressiva de SEO Técnico (On-Page e Estrutural). O objetivo é alcançar as primeiras posições do Google utilizando as melhores práticas modernas de EEAT (Experience, Expertise, Authoritativeness, and Trustworthiness) e Web Semântica.

Execute as seguintes otimizações no meu código de forma cirúrgica:

1. ENTITY DISAMBIGUATION (JSON-LD):
- Crie ou atualize um bloco `<script type="application/ld+json">` no `<head>`.
- Defina o "@type" correto para o negócio (ex: LocalBusiness, ProfessionalService, Organization).
- Inclua as propriedades: "name", "legalName", "description", "logo", "url".
- Adicione o array "knowsAbout" listando as 5 principais especialidades/palavras-chave do negócio.
- Adicione o array "sameAs" contendo os links reais de todas as redes sociais (Instagram, LinkedIn, etc.) para unificação da entidade.
- Se houver algum registro governamental (CNPJ, Marca Registrada), adicione via propriedade "identifier".

2. META TAGS E OPEN GRAPH (OG):
- Otimize a tag `<title>` (máximo 60 caracteres) contendo a palavra-chave principal e o nome da marca.
- Otimize a `<meta name="description">` (máximo 155 caracteres) focada em conversão e com chamada para ação (CTA).
- Adicione as tags Open Graph básicas (og:title, og:description, og:image, og:url, og:type) para compartilhamento perfeito no WhatsApp/LinkedIn.

3. SEMÂNTICA E HIERARQUIA:
- Garanta que exista apenas um único `<h1>` na página. Subtítulos devem respeitar a ordem lógica (`<h2>`, `<h3>`).
- Substitua `<div>`s genéricas por HTML5 semântico (`<header>`, `<main>`, `<section>`, `<article>`, `<footer>`) onde apropriado.

4. ACESSIBILIDADE E UX (Fatores de Rankeamento):
- Certifique-se de que todas as `<img>` possuam o atributo "alt" descritivo com palavras-chave.
- Todos os links (`<a>`) e botões iconográficos devem ter "aria-label".
- Links que apontam para fora do domínio devem ter `rel="noopener noreferrer"`.

5. SINAIS DE AUTORIDADE (EEAT):
- Certifique-se de que as informações de contato, CNPJ, ou registros de marca estejam visíveis no rodapé (`<footer>`) do HTML.

Por favor, analise o código HTML que vou te enviar a seguir, reescreva-o aplicando estritamente todas as 5 regras acima e, no final, me entregue o HTML refatorado e uma breve lista do que você alterou.

[COLE O CÓDIGO HTML DO SEU OUTRO SITE AQUI]
