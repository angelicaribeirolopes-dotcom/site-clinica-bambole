# WhatsApp com o interesse da página em todos os botões
_ALVO = {f"/servicos/{s['slug']}/": s["nome"] for s in SERVICOS}
_ALVO.update({"/autismo-tea/": "autismo (TEA)", "/tdah/": "TDAH"})
for _a in ARTICLES:
    _s = next((s for s in SERVICOS if s["slug"] == _a.get("service")), None)
    if _s: _ALVO["/artigos/" + _a["slug"] + "/"] = _s["nome"]
for _p, _svc in _ALVO.items():
    if _p in pages:
        pages[_p] = pages[_p].replace(WA, wa(_svc)).replace(wa(None), wa(_svc))
# ---------- write ----------
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT + "/assets")
for p, h in pages.items():
    d = OUT + p
    os.makedirs(d, exist_ok=True)
    open(d + "index.html", "w", encoding="utf-8").write(h)
open(OUT + "/404.html", "w", encoding="utf-8").write(p404)
open(OUT + "/assets/site.css", "w", encoding="utf-8").write(CSS)
shutil.copy("site.js", OUT + "/assets/site.js")
for f in os.listdir("assets"): shutil.copy("assets/" + f, OUT + "/assets/" + f)

idx = [p for p in pages if p != "/obrigado/"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f'  <url><loc>{BASE}{p}</loc><lastmod>{TODAY}</lastmod></url>\n' for p in idx) + '</urlset>\n'
open(OUT + "/sitemap.xml", "w").write(sm)
open(OUT + "/robots.txt", "w").write(f"""User-agent: *
Allow: /

# Buscadores e assistentes de IA são bem-vindos
User-agent: Googlebot
Allow: /
User-agent: Bingbot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: GPTBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: Google-Extended
Allow: /

Sitemap: {BASE}/sitemap.xml
""")
svc_md = "\n".join(f'- [{s["nome"]}]({BASE}/servicos/{s["slug"]}/): {s["resumo"]}' for s in SERVICOS)
art_md = "\n".join(f'- [{a["title"]}]({BASE}/artigos/{a["slug"]}/): {a["description"]}' for a in ARTICLES)
faq_md = "\n".join(f"- **{q}** {a}" for q, a in FAQ_GERAL)
open(OUT + "/llms.txt", "w", encoding="utf-8").write(f"""# Clínica Bambolê – Centro de Desenvolvimento Humano

> Clínica multidisciplinar em Belo Horizonte (bairro Santa Amélia, região da Pampulha), dedicada ao atendimento a crianças, adolescentes e adultos neurodivergentes – autismo (TEA), TDAH e outros quadros do neurodesenvolvimento. Avaliação neuropsicológica e dez áreas integradas de terapia. Fundada pela neuropsicóloga Angélica Lopes (CRP 04/37600).

## Dados da clínica
- Nome: Clínica Bambolê (Bambolê Centro de Desenvolvimento Humano)
- Endereço: {NAP["rua"]} – {NAP["bairro"]}, {NAP["cidade"]} – {NAP["uf"]}, {NAP["cep"]}, Brasil
- WhatsApp: {NAP["whats"]} · E-mail: {NAP["email"]}
- Horário: segunda a sexta, 8h às 20h; sábado, 8h às 16h; domingo fechado
- Atendimento: particular, com nota para reembolso do plano de saúde; presencial e online, conforme o serviço
- Sessões: 50 minutos, individuais (exceto oficinas sociais, em grupo)
- Público: crianças, adolescentes e adultos, típicos e atípicos
- Instagram: {NAP["instagram"]}

## Serviços
{svc_md}

## Páginas principais
- [Autismo (TEA)]({BASE}/autismo-tea/)
- [TDAH]({BASE}/tdah/)
- [Sobre e fundadora]({BASE}/sobre/)
- [Como atendemos]({BASE}/como-atendemos/)
- [Perguntas frequentes]({BASE}/perguntas-frequentes/)
- [Contato]({BASE}/contato/)
- [Artigos]({BASE}/artigos/)

## Artigos
{art_md}

## Perguntas frequentes
{faq_md}
""")
print("pages:", len(pages) + 1)

# Redirecionamentos do site antigo (301) e domínio
REDIRECTS = [
 ("/autismo.html", "/autismo-tea/"), ("/tdah.html", "/tdah/"),
 ("/avaliacao_neuropsicologica.html", "/servicos/avaliacao-neuropsicologica/"),
 ("/psicologia.html", "/servicos/terapia-aba/"), ("/depressao.html", "/servicos/terapia-aba/"), ("/toc.html", "/servicos/terapia-aba/"),
 ("/fonoaudiologia.html", "/servicos/fonoaudiologia/"), ("/musicoterapia.html", "/servicos/musicoterapia/"),
 ("/oficinas_sociais.html", "/servicos/oficinas-sociais/"), ("/oficinas_em_grupo.html", "/servicos/oficinas-sociais/"),
 ("/psicomotricidade.html", "/servicos/psicomotricidade/"), ("/terapia_ocupacional.html", "/servicos/terapia-ocupacional/"),
 ("/treinamento_pais.html", "/servicos/orientacao-parental/"),
 ("/artigo_ansiedade.html", "/artigos/ansiedade-sintomas-causas-tratamento/"),
 ("/artigo_autismo.html", "/artigos/autismo-o-que-e-sinais-diagnostico/"),
 ("/artigo_auto_estima.html", "/artigos/autoestima-o-que-e-como-melhorar/"),
 ("/artigo_tdah.html", "/artigos/tdah-dicas-hora-da-tarefa/"),
]
for _o, _n in REDIRECTS:
    assert _n == "/" or _n in pages, "redirecionamento para página inexistente: " + _n
_r = ["https://www.clinicabambole.com.br/* https://clinicabambole.com.br/:splat 301!"]
_r += [f"{o} {n} 301!" for o, n in REDIRECTS]
open(OUT + "/_redirects", "w").write("\n".join(_r) + "\n")
