# Como publicar um novo artigo no site da Clínica Bambolê

Cada artigo é um arquivo de texto (Markdown) dentro da pasta `artigos/`.
O nome do arquivo vira o endereço: `artigos/sinais-de-tdah-em-adultos.md` → `/artigos/sinais-de-tdah-em-adultos/`.

## Modelo (copie e preencha)

```
title: Título do artigo (com a palavra que as pessoas buscam no Google)
description: Resumo de 1 a 2 frases (até ~155 caracteres) que aparece no Google.
date: 2026-12-01
cover: /assets/nome-da-imagem.jpg
cover_alt: Descrição da imagem para acessibilidade e Google
service: avaliacao-neuropsicologica
tldr: Resumo direto de 2 a 4 frases. É o trecho que as IAs (ChatGPT, Gemini) mais citam.
faq: Pergunta 1? | Resposta curta e direta.
faq: Pergunta 2? | Resposta curta e direta.
faq: Pergunta 3? | Resposta curta e direta.
---
Texto do artigo. Use ## para subtítulos, - para listas e [texto](/servicos/...) para links.

*Este conteúdo é informativo e não substitui uma avaliação profissional.*
```

`service` pode ser: avaliacao-neuropsicologica, terapia-aba, fonoaudiologia, terapia-ocupacional,
psicomotricidade, psicopedagogia, fisioterapia, oficinas-sociais, musicoterapia, orientacao-parental.

## Publicar
1. Salve o arquivo em `artigos/` (e a imagem em `assets/`).
2. Rode `python3 build.py` para conferir se o site é gerado sem erro.
3. Faça o commit e o push para a branch `main` no GitHub. A Netlify gera e publica o site sozinha em cerca de 1 minuto.

Pelo Claude: escreva "publicar artigo Bambolê: [ideia ou texto]" e ele faz todos os passos.

## Dicas de SEO
- Um tema por artigo, respondendo a uma dúvida real (veja o que as famílias perguntam no WhatsApp e no Instagram).
- Título com o termo buscado + contexto (ex.: "… em crianças", "… em BH").
- Sempre linkar para o serviço relacionado e para outro artigo.
- Peça para a Angélica revisar: conteúdo de saúde revisado por profissional ganha confiança no Google.
