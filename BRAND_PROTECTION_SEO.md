# ⚠️ DOCUMENTAÇÃO DE ESTRATÉGIA DE PROTEÇÃO DE MARCA (SEO)

## O Problema
Existe um conflito internacional de marca pela palavra "Orkes". A Orkes Inc. (EUA) domina as buscas globais com orkes.io (focado em orquestração de microserviços). Nossa entidade brasileira possui a anterioridade da marca (2019) com registro no INPI, mas precisa de indexação local forte para proteger o domínio e forçar a detecção corporativa da empresa estrangeira.

## A Solução Implementada

Para resolver a sobreposição de Entidades no "Cérebro" do Google, foi injetado um bloco de dados estruturados (Schema.org) invisível aos usuários, mas obrigatório para os robôs.

### 1. Injeção de Dados Estruturados (JSON-LD)
Foi injetado um script `<script type="application/ld+json">` no `<head>` do site. Este script define explicitamente para o Googlebot que `orkes.com.br` é uma **entidade legal brasileira** (`"legalName": "FABIO SOUZA DE ANDRADE"` e `@type: LegalService`) fundada em **2019**, com operações em **São Paulo** e **Ceará**.

### 2. Afastamento Semântico (Desambiguação)
Para evitar "brigar" nas buscas gringas pelo termo técnico "Microservice Orchestration" (que a Orkes Inc. já domina com muito orçamento), o **H1 principal** e a **Meta Description** foram reescritos para focar puramente em **"Consultoria em Tecnologia da Informação"**. O Google agora entende que são duas empresas diferentes: uma vende produto SaaS nos EUA, e a outra presta serviço B2B de engenharia legada no Brasil.

### 3. Blindagem Legal no DOM (Footprint)
Foram criadas propriedades declarativas de autoria e marca:
- `"propertyID": "INPI", "value": "917789873"` no JSON-LD.
- O **Rodapé (Footer)** do site visível foi alterado para fixar o alerta de copyright da marca atrelada ao número de registro do INPI e ao CNPJ da empresa, estabelecendo que qualquer rastreador de *Brand Protection* (como os advogados da Dentons) leia este site e veja a legitimidade jurídica inquestionável da Orkes Brasil.

Esta estratégia transforma o portfólio de um simples currículo online para uma **prova documental indexada criptograficamente** pelo cache do Google, assegurando a anterioridade da marca brasileira na rede.
