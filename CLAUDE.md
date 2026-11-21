# Site da Clínica Bambolê

Site estático gerado em Python e publicado pela Netlify a cada push na branch `main`
(build: `python3 build.py`, pasta publicada: `dist/`).

- Conteúdo da clínica, serviços e FAQ: `content.py`
- Layout e páginas: `build_head.py`, `build_pages.py`, `build_articles.py`, `build_tail.py`, `site.css`, `site.js`
- Artigos: `artigos/*.md` (formato em `COMO-PUBLICAR-ARTIGOS.md`)
- Antes de commitar: rode `python3 build.py` e confira se termina sem erro.
- Regras: não inventar avaliações, números, prêmios ou fotos; não publicar depoimentos de pacientes,
  preços ou promessa de resultados (CFP/CRP-MG); Angélica Lopes, neuropsicóloga, CRP 04/37600,
  especialista em Autismo (TEA); equipe "com formação em ABA".
- Repositório PÚBLICO: nunca salvar aqui senhas, chaves de API, dados de pacientes, contatos de pessoas
  ou qualquer informação interna da clínica. Só o conteúdo que já aparece no site.
