
# ---------- ARTIGOS (lidos de artigos/*.md) ----------
import glob as _glob, markdown as _md, datetime as _dt
MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
def data_br(d):
    y, m, dd = d.split("-"); return f"{int(dd)} de {MESES[int(m)-1]} de {y}"

ARTICLES = []
for path in sorted(_glob.glob("artigos/*.md")):
    raw = open(path, encoding="utf-8").read()
    head, body = raw.split("\n---\n", 1)
    meta = {"faq": []}
    for line in head.strip().splitlines():
        k, v = line.split(":", 1); k, v = k.strip(), v.strip()
        if k == "faq":
            q, a = v.split("|", 1); meta["faq"].append((q.strip(), a.strip()))
        else:
            meta[k] = v
    meta["slug"] = os.path.basename(path)[:-3]
    meta["html"] = _md.markdown(body, extensions=["tables"])
    meta["words"] = len(body.split())
    ARTICLES.append(meta)
ARTICLES[:] = [a for a in ARTICLES if a["date"] <= TODAY]  # artigos com data futura ficam agendados
ARTICLES.sort(key=lambda a: a["date"], reverse=True)
SVC_BY = {s["slug"]: s for s in SERVICOS}

def art_cards(items):
    return '<div class="arts">' + "".join(
        f'<a class="art-card" href="/artigos/{a["slug"]}/"{R(delay=(i%3)*80)}><img src="{a["cover"]}" alt="{E(a["cover_alt"])}" loading="lazy"><div><small>{data_br(a["date"])} · {max(1, round(a["words"]/200))} min de leitura</small><b>{E(a["title"])}</b><span>{E(a["description"])}</span><em>Ler artigo →</em></div></a>'
        for i, a in enumerate(items)) + '</div>'

for a in ARTICLES:
    p = f'/artigos/{a["slug"]}/'
    svc = SVC_BY.get(a.get("service", ""))
    mins = max(1, round(a["words"] / 200))
    outros = [o for o in ARTICLES if o["slug"] != a["slug"]][:3]
    svc_cta = ""
    if svc:
        svc_cta = f'<div class="midcta has-mascot"{R()}><img class="mascot" src="/assets/angelica-personagem.webp" alt="" aria-hidden="true" width="312" height="600" loading="lazy"><p>Quer ajuda com isso? Conheça {svc["nome"].split(" (")[0].lower()} na Bambolê.</p><a class="btn btn-wa" href="/servicos/{svc["slug"]}/">Ver o serviço</a></div>'
    body = f'''<article class="post">
<header class="post-head wrap wrap-narrow"><span class="over"{R()}>Artigo · Clínica Bambolê</span><h1{R(delay=60)}>{E(a["title"])}</h1>
<p class="lead"{R(delay=120)}>{E(a["description"])}</p>
<p class="meta"{R(delay=160)}><time datetime="{a["date"]}">{data_br(a["date"])}</time> · {mins} min de leitura · Por Clínica Bambolê · Revisado por <a href="/sobre/">Angélica Lopes</a>, neuropsicóloga, CRP 04/37600</p></header>
<figure class="post-cover wrap wrap-narrow"{R(kind="zoom")}><img src="{a["cover"]}" alt="{E(a["cover_alt"])}" fetchpriority="high"></figure>
{tldr(E(a["tldr"]))}
<div class="prose post-body wrap wrap-narrow">{a["html"]}</div>
<div class="wrap wrap-narrow">{svc_cta}</div>
</article>
{faq_html(a["faq"], "Perguntas frequentes")}
<section class="sec"><div class="wrap wrap-narrow"><div class="author"{R()}><img src="/assets/angelica-perfil.jpg" alt="" width="64" height="64" loading="lazy"><div><b>Revisado por Angélica Lopes</b><span>Neuropsicóloga, CRP 04/37600, especialista em Autismo (TEA) e fundadora da Clínica Bambolê. Conteúdo informativo, que não substitui uma avaliação profissional.</span></div></div></div></section>
{"<section class='sec'><div class='wrap'><span class='over'>Continue lendo</span><h2>Outros artigos</h2>" + art_cards(outros) + "</div></section>" if outros else ""}
{cta_band("Ficou com alguma dúvida?", "Fale com a gente e agende uma conversa.", svc["nome"] if svc else None)}'''
    schema = {"@type": "BlogPosting", "@id": BASE + p + "#artigo", "headline": a["title"], "description": a["description"], "image": BASE + a["cover"],
              "datePublished": a["date"], "dateModified": a.get("updated", a["date"]), "inLanguage": "pt-BR",
              "author": {"@id": CLINIC_ID}, "publisher": {"@id": CLINIC_ID}, "mainEntityOfPage": BASE + p, "wordCount": a["words"]}
    pages[p] = page(p, a.get("seo_title") or f'{a["title"]} | Clínica Bambolê', a["description"], body, [schema, person_schema(), faq_schema(a["faq"])], og_img=a["cover"],
                    crumbs=[("Início", "/"), ("Artigos", "/artigos/"), (a["title"], p)])

hub_a = head_block("Artigos", "Artigos sobre desenvolvimento, autismo e TDAH", "Conteúdo da Clínica Bambolê para famílias, escolas e adultos neurodivergentes.", "ciano") + \
    tldr("Aqui a Clínica Bambolê, de Belo Horizonte, publica artigos sobre desenvolvimento infantil, autismo (TEA), TDAH, avaliação neuropsicológica, comportamento e orientação para famílias.") + \
    f'<section class="sec"><div class="wrap">{art_cards(ARTICLES)}</div></section>' + cta_band()
pages["/artigos/"] = page("/artigos/", "Artigos sobre autismo, TDAH e desenvolvimento | Clínica Bambolê BH",
    "Artigos da Clínica Bambolê sobre autismo, TDAH, avaliação neuropsicológica, comportamento infantil e orientação para famílias.", hub_a,
    [{"@type": "Blog", "@id": BASE + "/artigos/#blog", "name": "Artigos da Clínica Bambolê", "publisher": {"@id": CLINIC_ID},
      "blogPost": [{"@id": f'{BASE}/artigos/{a["slug"]}/#artigo'} for a in ARTICLES]}], crumbs=[("Início", "/"), ("Artigos", "/artigos/")])

# artigos recentes na página inicial (links internos)
_marker = '<section class="sec"><div class="wrap wrap-narrow"><span class="over">Clínica Bambolê em poucas linhas'
pages["/"] = pages["/"].replace(_marker, f'<section class="sec"><div class="wrap"><span class="over"{R()}>Artigos</span><h2{R()}>Conteúdo para famílias</h2>{art_cards(ARTICLES[:3])}<p style="margin-top:18px"><a class="link" href="/artigos/">Ver todos os artigos →</a></p></div></section>' + _marker, 1)
