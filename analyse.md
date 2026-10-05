# analyse.md — Adaptação do Portfólio Orkes como Template de Cliente

> **Autor da análise:** Antigravity (Claude Sonnet 4.6 Thinking) · Setembro de 2026  
> **Propósito:** Guia técnico e estratégico para reutilizar este projeto como template para novos clientes.

---

## 1. Visão Geral do que é reutilizável

O projeto é um **site estático multilíngue** (PT-BR / EN / ES) de portfólio/consultoria construído com HTML, CSS e JavaScript puros — sem framework, sem build tool, sem dependências de runtime.

### ✅ O que pode ser reaproveitado diretamente
- Estrutura de layout (header, carousels, zigzag, marquee, sticky footer)
- Sistema de design completo (variáveis CSS, paleta, tipografia Inter)
- Lógica de redirecionamento de idioma
- Componente de carousel horizontal (scroll-snap + arrows)
- Componente de marquee infinito de depoimentos
- Sticky footer com CTA sempre visível
- Estrutura SEO completa (OG tags, JSON-LD, hreflang, sitemap, robots.txt)
- Template de prompt SEO (`SEO_PROMPT_TEMPLATE.md`)
- Assets da pasta `social-media/` como referência de tamanhos OG

### ⚠️ O que é 100% específico do Fábio/Orkes e deve ser trocado
- Todas as imagens (`foto*.jpg`, `screen*.png`, `orkes*.png`, `open*.png`, `zap*.png`, `insta*.png`, `foto8.jpg`, `foto9_cta.jpg`)
- Logo (`logo.png`) e favicon (`favicon.jpg`)
- Conteúdo de todos os `<h1>`, `<h2>`, `<h3>`, textos de cards e seções
- Dados de contato (WhatsApp `5585991634033`, e-mail `contato@orkes.com.br`)
- Google Analytics ID (`G-3WXQYMZC5C`)
- Redes sociais (`github.com/souzace`, `linkedin.com/in/souzace`, `instagram.com/orkes.tech`)
- JSON-LD completo (nome, legalName, INPI, endereço, knowsAbout, sameAs)
- Todas as meta tags (title, description, OG, Twitter)
- Domínio (`orkes.com.br`) em todos os links canônicos, OG e sitemap
- Depoimentos (nomes, empresas, textos, datas)
- Casos de sucesso (projetos, setores, stacks)
- Serviços oferecidos (podem ter overlap mas devem ser revisados)
- Badges no header ("27 anos em TI", "16 anos em Dev. Sistemas", "Fortaleza, Ceará - Brasil")
- Texto "Sobre Mim" e citação do trombonista
- Número INPI `917789873` no footer

---

## 2. Problemas de Código a Corrigir Antes de Usar como Template

### 🔴 Crítico — duplicação de CSS

O arquivo `index.html` tem blocos CSS inteiros duplicados dentro de um `@media (min-width: 768px)`
começando por volta da linha 600. Regras como `.footer-avatar`, `.footer-links`, `.carousel-btn`,
`.services-grid` e até `@media` aninhados aparecem pela segunda vez. Isso é resultado de scripts
Python que foram aplicados sequencialmente ao longo do tempo.

**Ação:** Consolidar o CSS antes de personalizar — remover todas as regras duplicadas e garantir
que cada seletor apareça apenas uma vez.

### 🔴 Crítico — `@media (max-width: 768px)` duplicado

A regra para `.sobre-layout` e `.sobre-image-container` aparece duas vezes: uma dentro do `<style>`
principal (linha ~761) e outra dentro do `<style>` da seção `#depoimentos` (linha ~1248).

**Ação:** Manter apenas uma ocorrência, no bloco de estilos global.

### 🟡 Importante — CSS totalmente inline no HTML

Todo o CSS está dentro de `<style>` tags no HTML. O arquivo final fica com ~138 KB. Sem arquivo
externo, o browser **não consegue fazer cache do CSS** separadamente.

**Ação recomendada:** Extrair o CSS para um `style.css` externo. Isso reduz o HTML principal para
~50 KB e permite que o CSS seja cacheado entre as 3 páginas de idioma.

### 🟡 Importante — estilos inline excessivos nos elementos HTML

Muitos elementos usam `style=""` inline com dezenas de propriedades repetidas. Por exemplo, cada
`.service-card` dentro do carousel `#what-i-do` repete propriedades que já estão definidas na
classe CSS.

**Ação:** Limpar os `style=""` redundantes e garantir que as classes CSS cubram tudo.

### 🟡 Importante — scripts Python de migração na raiz

Há ~25 arquivos `.py` na raiz do projeto (ex: `fix_ctas.py`, `add_ai_service.py`,
`apply_gold_border.py`, `compress_about_me.py`). São scripts de uso único já executados.

**Ação:** Mover para uma pasta `scripts/archived/` ou deletar antes de usar como template.

### 🟠 Menor — depoimentos duplicados no DOM

O `marquee-track` contém ~18 cards de depoimentos escritos duas vezes no HTML para criar o efeito
de loop infinito. Isso são ~700 linhas de HTML repetido.

**Ação:** Considerar popular os depoimentos via JavaScript (array de objetos → innerHTML) para
manter o HTML limpo com o loop funcionando igualmente.

---

## 3. Arquitetura do Site

```
┌──────────────────────────────────────────────────────────┐
│                     index.html (PT-BR)                    │
│  ┌──────────────────────────────────────────────────────┐ │
│  │ <head>                                                │ │
│  │   Google Analytics · HTTPS redirect                   │ │
│  │   Language auto-redirect (sessionStorage)             │ │
│  │   Meta tags · OG · Twitter · hreflang                 │ │
│  │   JSON-LD (LegalService schema)                       │ │
│  │   <style> (CSS completo inline)                       │ │
│  └──────────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────────┐ │
│  │ <body>                                                │ │
│  │   Language flags (position:absolute, top-right)       │ │
│  │   <header>   Logo · Brand definition · Badges         │ │
│  │   <section #what-i-do>   Carousel de Serviços         │ │
│  │   <section #servicos>    Carousel de Casos            │ │
│  │   <section #sobre>       Zigzag Sobre Mim             │ │
│  │   <section #depoimentos> Marquee de Depoimentos       │ │
│  │   <footer .sticky-footer-bar>  CTA fixo               │ │
│  │   <script> scrollCarousel()                           │ │
│  └──────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────┘

        index.html ←── auto-redirect ──→ index-en.html
                                    └──→ index-es.html
```

Os três arquivos de idioma são **cópias completas** com conteúdo traduzido. Não há i18n dinâmico.

**Implicação:** Ao atualizar um elemento que aparece nos 3 idiomas (ex: footer, CTA, social links),
é preciso editar os três arquivos.

---

## 4. Estratégia SEO Herdada — Entender Antes de Replicar

O projeto tem uma estratégia SEO sofisticada documentada em `BRAND_PROTECTION_SEO.md`. O ponto
central é a **desambiguação de entidade no Google** via JSON-LD, criado para resolver um conflito
de marca. Para um novo cliente, a mesma lógica se aplica de forma simplificada:

| Elemento JSON-LD   | O que fazer para o cliente                                        |
|--------------------|-------------------------------------------------------------------|
| `@type`            | Definir o tipo correto (Person, LocalBusiness, ProfessionalService) |
| `legalName`        | Nome completo da pessoa física ou razão social                    |
| `identifier`       | CNPJ, OAB, CRM, CREA ou qualquer registro profissional           |
| `knowsAbout`       | 5 especialidades/keywords do cliente                              |
| `sameAs`           | Todos os perfis reais de redes sociais                            |
| `areaServed`       | Cidade/estado de atuação                                          |
| `foundingDate`     | Ano de início de atividade                                        |

O arquivo `SEO_PROMPT_TEMPLATE.md` contém um prompt pronto para rodar em qualquer LLM e otimizar
o SEO técnico do HTML do cliente. **Manter esse arquivo no template.**

---

## 5. Checklist de Adaptação para Novo Cliente

### Fase 1 — Limpeza do Template

- [ ] Remover todos os ~25 scripts `.py` (ou mover para `scripts/archived/`)
- [ ] Eliminar CSS duplicado (consolidar o `<style>` do `index.html`)
- [ ] Remover `@media (max-width: 768px)` duplicado da seção `#depoimentos`
- [ ] Limpar `style=""` inline redundantes nos `.service-card` do `#what-i-do`
- [ ] Extrair CSS para `style.css` externo (opcional mas recomendado)
- [ ] Deletar todas as imagens específicas do Fábio (`foto*.jpg`, `screen*.png`, etc.)
- [ ] Deletar OG images da pasta `social-media/` (serão substituídas)
- [ ] Deletar subpastas de social-media (facebook/, instagram/, linkedin/, olx/) — ou revisar
- [ ] Remover `Screenshot_1.png` e `Screenshot_2.png` da raiz

### Fase 2 — Coleta de Dados do Cliente

- [ ] Nome completo e nome da marca
- [ ] Foto profissional de alta qualidade (mínimo 1200×800px)
- [ ] Logo (PNG com fundo transparente)
- [ ] Favicon (formato quadrado, ao menos 512×512px)
- [ ] WhatsApp de contato (com DDI)
- [ ] E-mail profissional
- [ ] Domínio do site
- [ ] Perfis de redes sociais (LinkedIn, GitHub/Behance/Instagram — depende do setor)
- [ ] Google Analytics ID (criar conta GA4 se não tiver)
- [ ] Registro profissional (CNPJ, OAB, CRM, CREA, INPI, etc.)
- [ ] Cidade/estado de atuação
- [ ] Ano de início da carreira/empresa
- [ ] Lista de serviços (mínimo 4, máximo 9 para o carousel)
- [ ] Lista de projetos/casos de sucesso (mínimo 3, máximo 9)
- [ ] Depoimentos/recomendações (mínimo 5, ideal 10+)
- [ ] Bio resumida (2–3 parágrafos)
- [ ] Fotos de contexto (working, ambiente profissional — para o zigzag)
- [ ] Paleta de cores da marca (opcional — padrão preto/cyan pode ser mantido ou ajustado)

### Fase 3 — Substituições no HTML

**Global (nos 3 arquivos HTML — usar busca e substituição):**
- [ ] Domínio (`orkes.com.br` → domínio do cliente)
- [ ] `G-3WXQYMZC5C` → novo ID do Google Analytics
- [ ] `5585991634033` → WhatsApp do cliente (nos ~6 links `wa.me` por arquivo)
- [ ] `contato@orkes.com.br` → e-mail do cliente
- [ ] Links de redes sociais (GitHub/LinkedIn/Instagram no footer e no `sameAs` do JSON-LD)
- [ ] `logo.png` e `favicon.jpg` → ativos do cliente
- [ ] Mensagem pré-preenchida do WhatsApp (parâmetro `text=...` nos links `wa.me`)

**Conteúdo (por idioma):**
- [ ] `<title>` e `<meta name="description">`
- [ ] Tags OG e Twitter (og:title, og:description, og:image, og:url)
- [ ] JSON-LD completo (name, legalName, description, foundingDate, identifier, knowsAbout, sameAs, address)
- [ ] `<h1>` — subtítulo do header
- [ ] Card de definição da marca no header (bloco tipo "dicionário")
- [ ] Badges do header (localização, anos de experiência)
- [ ] Cards de serviços (`#what-i-do`) — título, subtítulo, descrição, ícone SVG
- [ ] Cards de casos de sucesso (`#servicos`) — projeto, setor, bullet points, stack
- [ ] Seção "Sobre" — zigzag rows (textos + fotos)
- [ ] Depoimentos — nome, cargo, empresa, data, texto
- [ ] Sticky footer — texto de CTA principal

**Arquivos auxiliares:**
- [ ] `sitemap.xml` — substituir todas as URLs para o domínio do cliente
- [ ] `robots.txt` — atualizar URL do Sitemap
- [ ] `social-media/og-image.jpg` (e EN/ES) — gerar novas OG images com a marca do cliente

### Fase 4 — Validação Técnica

- [ ] Validar HTML no validator.w3.org
- [ ] Testar redirect de idioma (navegador em inglês, espanhol e outros idiomas)
- [ ] Verificar todos os links de CTA (WhatsApp abre com a mensagem correta?)
- [ ] Testar responsividade (mobile 375px, tablet 768px, desktop 1280px)
- [ ] Verificar carousels em touch (swipe funciona?)
- [ ] Checar o marquee de depoimentos (pausa ao hover, loop suave)
- [ ] Testar sticky footer em mobile (não cobre conteúdo?)
- [ ] Testar Open Graph com opengraph.xyz ou Meta Debugger
- [ ] Validar JSON-LD com validator.schema.org
- [ ] Verificar Lighthouse score (Performance, Accessibility, SEO)
- [ ] Confirmar que o favicon carrega na aba do browser

---

## 6. Considerações de Performance

| Ponto                      | Status atual                      | Recomendação                                    |
|----------------------------|-----------------------------------|-------------------------------------------------|
| CSS inline                 | ~40 KB de CSS embutido            | Extrair para `style.css` — permite cache        |
| Imagens                    | JPEGs até 1.5 MB (`foto1.jpg`)    | Comprimir para < 200 KB; usar WebP              |
| Fontes                     | Google Fonts com `preconnect`     | ✅ Já otimizado                                 |
| Scripts externos           | Apenas `gtag.js`                  | ✅ Mínimo                                       |
| HTML bloat (depoimentos)   | ~700 linhas duplicadas            | Popular via JS para reduzir tamanho             |
| Favicon                    | `.jpg` (não ideal)                | Preferir `.ico` ou `.png` para compatibilidade  |

---

## 7. Considerações de Manutenção

Como o site é **HTML puro sem CMS**, toda atualização futura exige edição direta dos arquivos HTML:

| Ação                        | Impacto                                                              |
|-----------------------------|----------------------------------------------------------------------|
| Adicionar novo depoimento   | Editar 3 HTMLs + duplicar card no marquee de cada um                 |
| Adicionar novo projeto      | Editar 3 HTMLs                                                       |
| Mudar WhatsApp              | Busca e substituição em ~18 ocorrências (6 por arquivo × 3 idiomas)  |
| Atualizar foto              | Substituir o arquivo mantendo o mesmo nome                           |
| Mudar cor de destaque       | Alterar variável `--cyan-accent` no CSS (propagação automática)      |

**Recomendação:** Entregar junto com o site um mini-guia de manutenção documentando as zonas
editáveis e os arquivos que precisam ser sincronizados.

---

## 8. Estimativa de Esforço para Adaptação

| Tarefa                                          | Esforço estimado   |
|-------------------------------------------------|--------------------|
| Limpeza e consolidação do CSS                   | 2–3h               |
| Coleta e preparação de assets do cliente        | 1–5 dias (cliente) |
| Substituição de conteúdo (1 idioma)             | 3–5h               |
| Tradução e adaptação para EN e ES               | 2–4h por idioma    |
| Geração de OG images (3 idiomas)               | 1–2h               |
| Validação e testes                              | 1–2h               |
| **Total (1 idioma)**                            | **~8–12h**         |
| **Total (3 idiomas)**                           | **~15–22h**        |

---

## 9. Melhorias Opcionais Recomendadas

Não obrigatórias, mas elevariam a qualidade do template significativamente:

1. **Extrair CSS para `style.css`** — melhora cacheabilidade e elimina redundância entre os 3 HTMLs
2. **Popular depoimentos via JS** — array JSON de testimonials renderizado programaticamente,
   eliminando a duplicação de HTML e facilitando manutenção futura
3. **Adicionar `<main>` tag** — envolver as `<section>`s melhora semântica e acessibilidade
4. **Adicionar `loading="lazy"`** nas imagens abaixo do fold — melhora LCP
5. **Converter imagens para WebP** — redução de ~30–50% no tamanho sem perda visual
6. **Garantir `rel="noopener noreferrer"`** em todos os links `target="_blank"` — segurança
7. **Adicionar `aria-label`** nos botões de carousel (já existe em alguns, verificar todos)
8. **Adicionar `<meta name="theme-color" content="#000000">`** — personaliza barra do browser mobile
