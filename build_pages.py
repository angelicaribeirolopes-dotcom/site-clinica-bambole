pages = {}

def R(tag="div", kind="", delay=0):
    a = ' data-reveal' + (f'="{kind}"' if kind else '')
    return a + (f' data-delay="{delay}"' if delay else '')

TRUST = f'''<div class="trust">
<div{R(delay=0)}><strong><span data-count="5.0">5,0</span>★</strong><span>de nota no Google</span></div>
<div{R(delay=80)}><strong data-count="14">14</strong><span>anos de experiência da fundadora</span></div>
<div{R(delay=160)}><strong data-count="10">10</strong><span>áreas de atendimento na mesma clínica</span></div>
<div{R(delay=240)}><strong><span data-count="50">50</span> min</strong><span>por sessão, atendimento individual</span></div></div>'''

def svc_cards():
    cores = ["var(--ciano)", "var(--laranja)", "var(--rosa)", "var(--amarelo)"]
    return '<ul class="svc-list">' + "".join(
        f'<li{R(delay=(i%2)*80)}><a href="/servicos/{s["slug"]}/"><i class="dot" style="background:{cores[i%4]}"></i><span><b>{s["nome"]}</b><small>{s["linha"]}</small></span><em aria-hidden="true">→</em></a></li>' for i, s in enumerate(SERVICOS)) + '</ul>'

def reviews_block(items=None):
    return f'''<section class="sec" id="avaliacoes"><div class="wrap"><div class="block rev-head"{R(kind="zoom")}><div><span class="over">Google</span><h2>Avaliações da clínica</h2><p>As avaliações das famílias ficam no nosso perfil do Google.</p></div><div class="score"><strong>5,0</strong><div><span class="stars" aria-label="5 de 5 estrelas">★★★★★</span><small>nota no Google</small></div></div><a class="btn btn-line" href="{{NAP["maps"]}}" target="_blank" rel="noopener">Ver no Google →</a></div></div></section>'''

def authority(svc=None):
    return f'''<section class="sec"><div class="wrap"><div class="auth"{R(kind="zoom")}><img class="wm" src="/assets/bo.png" alt="" aria-hidden="true" width="160" height="136" loading="lazy">
<img src="/assets/angelica-principal.jpg" alt="Angélica Lopes, neuropsicóloga e fundadora, em uma sala de atendimento infantil da Clínica Bambolê" width="560" height="799" loading="lazy">
<div><span class="over">Quem cuida de você</span><h2>Angélica Lopes, neuropsicóloga e fundadora</h2>
<div class="creds"><span>CRP 04/37600</span><span>14 anos de experiência</span><span>Formação em ABA</span><span>Especialista em Autismo (TEA)</span><span>TCC</span><span>Reabilitação do TDAH</span><span>CAA</span></div>
<p>A Angélica fundou a Bambolê e acompanha de perto toda a equipe. A neuropsicologia orienta o trabalho da clínica, da avaliação ao plano terapêutico.</p>
<div class="ctas"><a class="btn btn-wa" href="{wa(svc)}" target="_blank" rel="noopener">{wa_icon()}Falar com a equipe</a></div></div></div></div></section>'''

def start_steps(svc=None):
    return f'''<section class="sec"><div class="wrap"><span class="over"{R()}>Como começar</span><h2{R()}>Como agendar</h2>
<ol class="start"><li{R(delay=0)}><b>Fale com a gente</b><span>Pelo WhatsApp {NAP["whats"]}. Conte o que está acontecendo.</span></li>
<li{R(delay=100)}><b>Receba a orientação</b><span>A equipe entende a demanda e indica o serviço mais adequado.</span></li>
<li{R(delay=200)}><b>Agende e comece</b><span>Escolha o melhor horário, de segunda a sábado, presencial ou online.</span></li></ol>
<div class="midcta has-mascot"{R()}><img class="mascot" src="/assets/angelica-personagem.webp" alt="Personagem ilustrada da Angélica Lopes, da Clínica Bambolê" width="312" height="600" loading="lazy"><p>Pronto para dar o primeiro passo?</p><a class="btn btn-wa" href="{wa(svc)}" target="_blank" rel="noopener">{wa_icon()}Agende pelo WhatsApp</a></div></div></section>'''

def espaco_block(fotos, titulo="Um lugar para acolher, brincar e se desenvolver."):
    items = "".join(f'<li{R(delay=i*60)}><b>{a}</b><span>{b}</span></li>' for i, (a, b) in enumerate(ESPACO))
    imgs = "".join(f'<figure class="photo"{R(kind="zoom", delay=i*80)}><img src="/assets/{f}" alt="{E(alt)}" width="720" height="900" loading="lazy"></figure>' for i, (f, alt) in enumerate(fotos))
    return f'<section class="sec"><div class="wrap"><span class="over"{R()}>Nosso espaço</span><h2{R()}>{titulo}</h2><div class="espaco"><ul class="esp-list">{items}</ul><div class="esp-grid">{imgs}</div></div></div></section>'

FOTOS_HOME = [("espaco-sala-ampla.jpg", "Sala de Terapia Ocupacional e Psicomotricidade da Clínica Bambolê"), ("espaco-acervo.jpg", "Brinquedos e jogos usados nas terapias"), ("espaco-piscina-angelica.jpg", "Angélica Lopes na piscina de bolinhas da Clínica Bambolê"), ("espaco-recepcao.jpg", "Sala com poltronas e mesa na Clínica Bambolê")]
FOTOS_SOBRE = FOTOS_HOME + [("espaco-painel-sensorial.jpg", "Painel de atividades e estímulos"), ("espaco-escalada.jpg", "Estrutura de escalada e balanços"), ("espaco-mesa.jpg", "Mesa infantil e cavalete de pintura"), ("espaco-mesinha.jpg", "Espaço de atividades com materiais")]

PAINS = [("Suspeita de autismo ou TDAH?", "A avaliação neuropsicológica mapeia atenção, memória, funções executivas e aspectos emocionais.", "avaliacao-neuropsicologica", "var(--azul)"),
         ("A fala não vem como esperado?", "A fonoaudiologia trabalha fala, linguagem e voz, integrada às outras terapias.", "fonoaudiologia", "var(--rosa)"),
         ("Birras e crises todos os dias?", "Nem todo comportamento difícil é falta de limite. A orientação parental ajuda a família a agir.", "orientacao-parental", "var(--laranja)"),
         ("Dificuldade na escola?", "A psicopedagogia ajuda a aprender com confiança, em parceria com a família e a escola.", "psicopedagogia", "var(--amarelo)")]
TEMAS = ["TEA (autismo)", "TDAH", "TOD", "TOC", "Ansiedade (TAG)", "TPAC", "TDL", "TPS", "Deficiência intelectual", "Altas habilidades", "Dificuldades de aprendizagem", "Regulação emocional", "Atraso de fala", "Processamento auditivo (PAC)", "Questões sensoriais"]
marquee = '<div class="marquee" aria-label="Temas que acompanhamos"><ul>' + "".join(f"<li>{t}</li>" for t in TEMAS * 2) + '</ul></div>'

# ---------- HOME ----------
facts = [("O que é", "Clínica multidisciplinar com foco em autismo (TEA) e TDAH"), ("Onde", "Santa Amélia, Pampulha – Belo Horizonte (MG)"),
         ("Para quem", "Crianças, adolescentes e adultos, típicos e atípicos"), ("Áreas", "10 áreas integradas, da avaliação neuropsicológica à orientação parental"),
         ("Sessões", "50 minutos, individuais (exceto oficinas em grupo)"), ("Modalidade", "Presencial e online, conforme o serviço"),
         ("Pagamento", "Particular, com nota para reembolso do plano"), ("Fundadora", "Angélica Lopes, neuropsicóloga, CRP 04/37600, 14 anos de experiência")]
facts_html = '<dl class="facts-list">' + "".join(f'<div{R(delay=(i%2)*60)}><dt>{a}</dt><dd>{b}</dd></div>' for i, (a, b) in enumerate(facts)) + '</dl>'
home_faq = FAQ_GERAL[:6]
pains_html = "".join(f'<a class="pain" href="/servicos/{sl}/" style="--c:{c}"{R(delay=i*90)}><b>{t}</b><span>{d}</span><em>Saiba mais →</em></a>' for i, (t, d, sl, c) in enumerate(PAINS))
home_body = f'''
<section class="hero"><i class="blob b1" data-par="0.15"></i><i class="blob b2" data-par="0.08"></i><i class="blob b3" data-par="0.12"></i><div class="wrap">
<div><span class="over"{R()}>Clínica Bambolê · Pampulha · Belo Horizonte</span>
<h1{R(delay=80)}>Clínica de autismo e TDAH em <em>Belo Horizonte</em></h1>
<p class="lead"{R(delay=160)}>Avaliação neuropsicológica e dez terapias integradas para crianças, adolescentes e adultos neurodivergentes. A avaliação e as terapias acontecem na mesma clínica, e a família participa de cada etapa.</p>
<div class="ctas"{R(delay=240)}><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{wa_icon()}Agende pelo WhatsApp</a><a class="btn btn-line" href="#agendar">Prefiro que me chamem</a></div>
<p class="rating"{R(delay=320)}><span class="stars" aria-hidden="true">★★★★★</span> <b>5,0</b> no Google · Atendimento particular</p></div>
<figure class="arch"{R(kind="right", delay=150)}><img src="/assets/angelica-perfil.jpg" alt="Angélica Lopes, neuropsicóloga e fundadora da Clínica Bambolê" width="560" height="841" fetchpriority="high"><figcaption><b>Angélica Lopes</b>Neuropsicóloga e fundadora</figcaption>
<div class="badge-float"><span class="stars">★★★★★</span><b>5,0</b>no Google</div>
<svg class="rings" viewBox="0 0 200 200" aria-hidden="true"><g fill="none" stroke-width="14"><circle cx="200" cy="200" r="40" stroke="#218FCE"/><circle cx="200" cy="200" r="62" stroke="#59C3FF"/><circle cx="200" cy="200" r="84" stroke="#FFD855"/><circle cx="200" cy="200" r="106" stroke="#FF6C1C"/><circle cx="200" cy="200" r="128" stroke="#F41F55"/></g></svg></figure>
</div></section>

<div class="wrap">{TRUST}</div>

<section class="sec"><div class="wrap"><span class="over"{R()}>Por onde começar</span><h2{R()}>Você está passando por isso?</h2>
<div class="pains">{pains_html}</div>{marquee}</div></section>

<section class="sec" id="servicos"><div class="wrap">
<div class="block svc-head" style="--ac:var(--azul)"{R(kind="zoom")}><span class="over">Nossos serviços</span><h2>Dez áreas, um acompanhamento.</h2><p>Cada serviço pode ser feito sozinho ou combinado em um plano integrado.</p></div>
{svc_cards()}
<div class="help"{R()}><img class="mascot" src="/assets/angelica-personagem.webp" alt="Personagem ilustrada da Angélica Lopes, da Clínica Bambolê" width="312" height="600" loading="lazy"><p>Não sabe por onde começar? <a href="#agendar">A gente te orienta.</a></p></div>
</div></section>

{authority()}

{espaco_block(FOTOS_HOME)}

<section class="sec"><div class="wrap">
<div class="block yellow"{R(kind="zoom")}><span class="over">Nossos diferenciais</span><h2>Por que escolher a Bambolê?</h2></div>
<ol class="steps">{"".join(f'<li{R(delay=(i%2)*80)}><b>{a}</b><span>{b}</span></li>' for i, (a, b) in enumerate(DIFERENCIAIS))}</ol>
</div></section>

{reviews_block()}

{start_steps()}

{faq_html(home_faq, mascot=False)}
<p class="wrap wrap-narrow"><a class="link" href="/perguntas-frequentes/">Ver todas as perguntas frequentes →</a></p>

<section class="sec"><div class="wrap wrap-narrow"><span class="over">Resumo</span><h2>A Clínica Bambolê em resumo</h2>{facts_html}</div></section>

<section class="sec" id="contato"><div class="wrap contact">{form_html("Prefere que a gente te chame?", "Deixe seus dados e a equipe da Bambolê retorna pelo WhatsApp.")}{loc_card()}</div></section>
{cta_band()}
'''
pages["/"] = page("/", "Clínica de Autismo e TDAH em Belo Horizonte (Pampulha) | Clínica Bambolê",
    "Avaliação neuropsicológica, terapia ABA, fono, TO e mais 6 áreas para crianças, adolescentes e adultos neurodivergentes. Santa Amélia, Pampulha, BH.",
    home_body, [clinic_schema(), person_schema(), faq_schema(home_faq)], og_img="/assets/angelica-perfil.jpg")

# ---------- SERVIÇOS HUB ----------
hub = f'''<section class="shero"><div class="wrap"><div class="block on-dark" style="--ac:var(--azul)"{R(kind="zoom")}>
<div><span class="over">Nossos serviços</span><h1>Serviços da Clínica Bambolê em Belo Horizonte</h1><p class="lead-on">Dez áreas integradas em um só plano, para crianças, adolescentes e adultos, típicos e atípicos.</p>
<div class="ctas"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{wa_icon()}Me ajude a escolher</a></div></div>
<div class="ph"><img src="/assets/angelica.jpg" alt="Angélica Lopes, neuropsicóloga da Clínica Bambolê" width="400" height="572"></div></div></div></section>''' + \
    tldr("A Clínica Bambolê, na Pampulha, em Belo Horizonte, oferece avaliação neuropsicológica, psicoterapia (ABA, TCC, PECS), fonoaudiologia, terapia ocupacional, psicomotricidade, psicopedagogia, fisioterapia, oficinas sociais, musicoterapia e orientação parental. Cada serviço pode ser feito sozinho ou combinado em um plano integrado.") + \
    f'<section class="sec"><div class="wrap">{svc_cards()}</div></section>' + start_steps() + cta_band("Não sabe por onde começar?", "Conte o que você precisa e a equipe indica o melhor caminho.")
pages["/servicos/"] = page("/servicos/", "Serviços para autismo e TDAH em BH | Clínica Bambolê",
    "Conheça as 10 áreas da Clínica Bambolê em BH: avaliação neuropsicológica, terapia ABA, fonoaudiologia, terapia ocupacional, psicomotricidade e mais.",
    hub, [{"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f'{BASE}/servicos/{s["slug"]}/', "name": s["nome"]} for i, s in enumerate(SERVICOS)]}],
    crumbs=[("Início", "/"), ("Serviços", "/servicos/")], og_img="/assets/angelica.jpg")

# ---------- SERVIÇO (funil) ----------
OBJ = [FAQ_GERAL[3], FAQ_GERAL[5]]
for s in SERVICOS:
    p = f'/servicos/{s["slug"]}/'
    nome_curto = s["nome"].split(" (")[0]
    bg, fg = COR[s["cor"]], COR_TXT[s["cor"]]
    passos = "".join(f'<li{R(delay=i*90)}><b>{a}</b><span>{b}</span></li>' for i, (a, b) in enumerate(s["passos"]))
    ident = "".join(f'<li{R(delay=(i%2)*70)}>{x}</li>' for i, x in enumerate(s["para_quem"]))
    dest = ""
    if s.get("destaque"):
        dest = f'<div class="block cta slim"{R(kind="zoom")}><div><h2>{s["destaque"][0]}</h2><p>{s["destaque"][1]}</p></div><a class="wa" href="{wa(s["nome"])}" target="_blank" rel="noopener"><span>{wa_icon()}</span>Agende pelo WhatsApp</a></div>'
    else:
        dest = f'<div class="midcta"{R()}><p>Não sabe se este atendimento é indicado para o seu caso?</p><a class="btn btn-wa" href="{wa(s["nome"])}" target="_blank" rel="noopener">{wa_icon()}Converse com a equipe</a></div>'
    outros = [o for o in SERVICOS if o["slug"] != s["slug"]][:4]
    rel = "".join(f'<li><a href="/servicos/{o["slug"]}/">{o["nome"]}</a></li>' for o in outros)
    faqs = s["faq"] + OBJ
    titulo_oque = "O que são as oficinas sociais" if s["slug"] == "oficinas-sociais" else "O que é " + nome_curto.lower()
    why = "".join(f'<li>{a}</li>' for a, _ in DIFERENCIAIS[1:5])
    body = f'''<section class="shero"><div class="wrap"><div class="block on-dark" style="--ac:{bg}"{R(kind="zoom")}>
<svg class="rings2" viewBox="0 0 200 200" aria-hidden="true"><g fill="none" stroke-width="14" stroke="currentColor" opacity=".35"><circle cx="200" cy="200" r="50"/><circle cx="200" cy="200" r="80"/><circle cx="200" cy="200" r="110"/></g></svg>
<div><span class="over">{s["linha"]}</span><h1>{s["titulo"]}</h1><p class="lead-on">Na Pampulha, para crianças, adolescentes e adultos, típicos e atípicos, com uma equipe que trabalha integrada.</p>
<div class="ctas"><a class="btn btn-wa" href="{wa(s["nome"])}" target="_blank" rel="noopener">{wa_icon()}Agende pelo WhatsApp</a><a class="btn btn-line" href="#agendar" data-svc="{s["nome"]}">Prefiro que me chamem</a></div>
<p class="proof"><span class="stars" aria-hidden="true">★★★★★</span> 5,0 no Google · Responsável técnica: Angélica Lopes, CRP 04/37600</p></div>
<div class="ph"><img src="/assets/angelica.jpg" alt="Angélica Lopes, neuropsicóloga e fundadora da Clínica Bambolê" width="400" height="572"></div></div></div></section>
{tldr(s["resumo"])}
<section class="sec"><div class="wrap wrap-narrow"><span class="over"{R()}>Você se identifica?</span><h2{R()}>Para quem é {nome_curto.lower() if s["slug"]!="oficinas-sociais" else "a oficina social"}</h2>
<ul class="ident">{ident}</ul>
<div class="ident-cta"{R()}><p>Reconheceu alguma situação? Vamos conversar.</p><a class="btn btn-wa btn-sm" href="{wa(s["nome"])}" target="_blank" rel="noopener">{wa_icon()}Falar agora</a></div></div></section>
<section class="sec"><div class="wrap two-text">
<div class="prose"{R(kind="left")}><h2>{titulo_oque}</h2>{"".join(f"<p>{x}</p>" for x in s["intro"])}</div>
<aside{R(kind="right")}><figure class="photo svc-photo"><img src="/assets/{s["foto"][0]}" alt="{s["foto"][1]}" width="720" height="900" loading="lazy"><figcaption>{s["foto"][1]}</figcaption></figure><div class="side"><span class="over">Nossa equipe nesta área</span><ul class="ticks">{"".join(f"<li>{x}</li>" for x in s["equipe"])}</ul></div>
<div class="mini-auth"><img src="/assets/angelica.jpg" alt="" width="64" height="64" loading="lazy"><div><b>Angélica Lopes</b><span>Neuropsicóloga e fundadora · CRP 04/37600 · acompanha de perto toda a equipe</span></div></div></aside>
</div></section>
<section class="sec"><div class="wrap"><span class="over"{R()}>Como funciona</span><h2{R()}>Como funciona na Bambolê</h2><ol class="steps four">{passos}</ol>{dest}</div></section>
{reviews_block()}
{faq_html(faqs, "Dúvidas sobre " + nome_curto.lower())}
<section class="sec"><div class="wrap contact">{form_html(f"Quero agendar {nome_curto.lower()}", "Deixe seus dados e a equipe da Bambolê retorna pelo WhatsApp.", s["nome"])}{loc_card()}</div></section>
<section class="sec"><div class="wrap wrap-narrow"><span class="over">Plano integrado</span><h2>Outras áreas da Bambolê</h2><ul class="rel">{rel}<li><a href="/servicos/">Ver todos os serviços</a></li></ul></div></section>
{cta_band("Vamos conversar?", "Agende uma visita e conheça a clínica.", s["nome"])}'''
    svc_schema = {"@type": "MedicalTherapy" if s["slug"] != "avaliacao-neuropsicologica" else "DiagnosticProcedure", "@id": BASE + p + "#servico", "name": s["nome"], "description": s["resumo"], "url": BASE + p}
    offer = {"@type": "Service", "name": s["titulo"].replace(" em BH", "") + " – Clínica Bambolê", "serviceType": s["nome"], "description": s["resumo"], "provider": {"@id": CLINIC_ID},
             "areaServed": {"@type": "City", "name": "Belo Horizonte"}, "audience": {"@type": "PeopleAudience", "audienceType": "Crianças, adolescentes e adultos, típicos e atípicos"}, "url": BASE + p}
    desc = s["resumo"] if len(s["resumo"]) <= 158 else s["resumo"][:155].rsplit(" ", 1)[0] + "…"
    pages[p] = page(p, f'{s["titulo"]} (Pampulha) | Clínica Bambolê', desc, body, [svc_schema, offer, faq_schema(faqs)],
                    crumbs=[("Início", "/"), ("Serviços", "/servicos/"), (s["nome"], p)], og_img="/assets/angelica.jpg")

def cond_page(path, over, h1, color, resumo, prose, faqs, img, img_alt, title, desc, cond, svc):
    body = f'''<section class="shero"><div class="wrap"><div class="block on-dark" style="--ac:{COR[color]}"{R(kind="zoom")}>
<div><span class="over">{over}</span><h1>{h1}</h1><p class="lead-on">Avaliação e terapias integradas na Pampulha, para crianças, adolescentes e adultos.</p>
<div class="ctas"><a class="btn btn-wa" href="{wa(svc)}" target="_blank" rel="noopener">{wa_icon()}Agende pelo WhatsApp</a><a class="btn btn-line" href="#agendar">Prefiro que me chamem</a></div>
<p class="proof"><span class="stars" aria-hidden="true">★★★★★</span> 5,0 no Google · Responsável técnica: Angélica Lopes, CRP 04/37600</p></div>
<div class="ph"><img src="/assets/angelica.jpg" alt="Angélica Lopes, neuropsicóloga da Clínica Bambolê" width="400" height="572"></div></div></div></section>
{tldr(resumo)}
<section class="sec"><div class="wrap two-text"><div class="prose"{R(kind="left")}>{prose}</div><figure class="photo"{R(kind="right")}><img src="/assets/{img}" alt="{img_alt}" loading="lazy"></figure></div></section>
{start_steps(svc)}{reviews_block()}{faq_html(faqs, "Perguntas frequentes")}
<section class="sec"><div class="wrap contact">{form_html("Vamos conversar?", "Deixe seus dados e a equipe da Bambolê retorna pelo WhatsApp.")}{loc_card()}</div></section>{cta_band(svc=svc)}'''
    pages[path] = page(path, title, desc, body, [{"@type": "MedicalCondition", **cond}, faq_schema(faqs)], og_img="/assets/angelica.jpg", crumbs=[("Início", "/"), (over, path)])

tea_faq = [("Onde fazer avaliação de autismo em Belo Horizonte?", "A Clínica Bambolê, no bairro Santa Amélia (Pampulha), faz avaliação neuropsicológica para crianças, adolescentes e adultos com suspeita de TEA, em média em 10 a 15 sessões, com laudo e devolutiva."),
           ("Quais terapias a Bambolê oferece para autismo?", "Psicoterapia com psicólogas com formação em ABA (e também TCC, PECS e técnicas lúdicas), fonoaudiologia, terapia ocupacional, psicomotricidade, musicoterapia, psicopedagogia, oficinas sociais e orientação parental, em um plano integrado."),
           ("A Bambolê atende adultos autistas?", "Sim. A clínica atende crianças, adolescentes e adultos neurodivergentes."),
           ("Quem faz o diagnóstico de autismo?", "O diagnóstico de TEA é clínico e feito por médico, geralmente neuropediatra ou psiquiatra, muitas vezes com apoio de uma avaliação multiprofissional. A avaliação neuropsicológica ajuda a mapear o perfil do paciente e orientar o tratamento.")]
tea_prose = '''<h2>O que é o transtorno do espectro autista (TEA)</h2>
<p>O TEA é uma condição do neurodesenvolvimento que afeta, em graus diferentes, a comunicação e a interação social e que costuma vir acompanhada de padrões restritos e repetitivos de comportamento e interesses. Por ser um espectro, cada pessoa tem um perfil próprio.</p>
<h2>Sinais que costumam levar as famílias a buscar ajuda</h2>
<ul class="ticks"><li>Atraso ou diferença no desenvolvimento da fala</li><li>Pouca resposta ao chamado pelo nome ou pouco contato visual</li><li>Dificuldade de interação com outras crianças</li><li>Brincadeiras ou movimentos repetitivos</li><li>Muita sensibilidade a sons, texturas ou mudanças de rotina</li></ul>
<p class="muted">Esses sinais não fecham diagnóstico. Se você tem dúvidas, procure o pediatra e uma avaliação especializada.</p>
<h2>Como a Bambolê acompanha pessoas autistas</h2>
<p>O cuidado começa pela escuta da família e, quando indicado, pela <a href="/servicos/avaliacao-neuropsicologica/">avaliação neuropsicológica</a>. A partir dela, a equipe monta um plano integrado com as áreas necessárias, como <a href="/servicos/terapia-aba/">psicoterapia com ABA</a>, <a href="/servicos/fonoaudiologia/">fonoaudiologia</a>, <a href="/servicos/terapia-ocupacional/">terapia ocupacional</a> e <a href="/servicos/orientacao-parental/">orientação parental</a>. A avaliação e as terapias acontecem na mesma clínica, e a família participa de cada etapa.</p>'''
cond_page("/autismo-tea/", "Autismo (TEA)", "Clínica de autismo (TEA) em Belo Horizonte", "ciano",
    "A Clínica Bambolê atende pessoas neurodivergentes, incluindo autistas. Em Belo Horizonte, no bairro Santa Amélia (Pampulha), oferece avaliação neuropsicológica e terapias integradas, com psicólogas com formação em ABA, para crianças, adolescentes e adultos.",
    tea_prose, tea_faq, "espaco-piscina-angelica.jpg", "Angélica Lopes na piscina de bolinhas da sala de terapia da Clínica Bambolê",
    "Clínica de Autismo (TEA) em BH – Avaliação e Terapia ABA | Clínica Bambolê",
    "Avaliação neuropsicológica e terapias para autismo (TEA) em Belo Horizonte: psicólogas com formação em ABA, fono, TO e mais. Pampulha.",
    {"name": "Transtorno do Espectro Autista (TEA)", "alternateName": "Autismo"}, "autismo (TEA)")

tdah_faq = [("Onde fazer avaliação de TDAH em Belo Horizonte?", "Na Clínica Bambolê, na Pampulha. A avaliação neuropsicológica mapeia atenção, memória, funções executivas e aspectos emocionais de crianças, adolescentes e adultos."),
            ("Adulto pode fazer avaliação de TDAH na Bambolê?", "Sim. A avaliação neuropsicológica atende crianças, adolescentes e adultos."),
            ("Quem diagnostica o TDAH?", "O diagnóstico de TDAH é clínico e feito por médico, geralmente psiquiatra ou neurologista. A avaliação neuropsicológica traz dados sobre atenção e funções executivas que ajudam nessa decisão e no tratamento."),
            ("Quais terapias ajudam no TDAH?", "Na Bambolê, o plano pode incluir psicoterapia (TCC e ABA), psicopedagogia, orientação parental e outras áreas, conforme a avaliação.")]
tdah_prose = '''<h2>O que é TDAH</h2>
<p>O Transtorno do Déficit de Atenção com Hiperatividade (TDAH) é uma condição do neurodesenvolvimento marcada por desatenção e/ou hiperatividade-impulsividade, que aparece em diferentes contextos, como casa, escola e trabalho, e pode continuar na vida adulta.</p>
<h2>Como a avaliação neuropsicológica ajuda</h2>
<p>A <a href="/servicos/avaliacao-neuropsicologica/">avaliação neuropsicológica</a> mapeia atenção, memória, funções executivas e aspectos emocionais. O resultado orienta médicos, família e escola e ajuda a construir o plano terapêutico. Na Bambolê, são em média 10 a 15 sessões, com mais de 40 testes e escalas padronizados.</p>
<h2>Acompanhamento depois da avaliação</h2>
<p>Conforme a necessidade, o plano pode incluir <a href="/servicos/terapia-aba/">psicoterapia (TCC e ABA)</a>, <a href="/servicos/psicopedagogia/">psicopedagogia</a> para a vida escolar e <a href="/servicos/orientacao-parental/">orientação parental</a> para a rotina em casa.</p>'''
cond_page("/tdah/", "TDAH", "Avaliação e terapia para TDAH em Belo Horizonte", "laranja",
    "A Clínica Bambolê, em Belo Horizonte, faz avaliação neuropsicológica para suspeita de TDAH em crianças, adolescentes e adultos e oferece acompanhamento com psicoterapia, psicopedagogia e orientação parental, em um plano integrado.",
    tdah_prose, tdah_faq, "angelica-principal.jpg", "Angélica Lopes, neuropsicóloga e fundadora, em uma sala de atendimento da Clínica Bambolê",
    "Avaliação de TDAH em BH – Crianças e Adultos | Clínica Bambolê",
    "Avaliação neuropsicológica para TDAH em Belo Horizonte, para crianças, adolescentes e adultos, com acompanhamento integrado. Pampulha.",
    {"name": "Transtorno do Déficit de Atenção com Hiperatividade (TDAH)", "alternateName": "TDAH"}, "TDAH")

# ---------- SOBRE ----------
sobre = head_block("Quem somos", "Sobre a Clínica Bambolê", "Cuidar do desenvolvimento, juntos.", "amarelo") + \
    tldr("A Clínica Bambolê – Centro de Desenvolvimento Humano fica na Pampulha, em Belo Horizonte, e foi fundada pela neuropsicóloga Angélica Lopes (CRP 04/37600), com 14 anos de experiência. Atende crianças, adolescentes e adultos, típicos e atípicos, em dez áreas integradas.") + f'''
<section class="sec"><div class="wrap two">
<figure class="arch small"{R(kind="left")}><img src="/assets/angelica.jpg" alt="Angélica Lopes, neuropsicóloga e fundadora da Clínica Bambolê" width="400" height="572" loading="lazy"></figure>
<div{R(kind="right")}><span class="over">Fundadora</span><h2>Angélica Lopes</h2><p class="muted">Neuropsicóloga · CRP 04/37600 · 14 anos de experiência</p>
<p>Angélica Vany Ribeiro Lopes fundou a Bambolê e acompanha de perto toda a equipe. A neuropsicologia orienta o trabalho da clínica: da avaliação ao plano terapêutico e à escolha do acervo de testes e materiais.</p>
<p>A Bambolê nasceu para reunir, em um só lugar, os olhares que o desenvolvimento precisa: vários olhares, um só cuidado.</p>
<ul class="chips">{"".join(f"<li>{c}</li>" for c in CURRICULO)}</ul>
<div class="ctas"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{wa_icon()}Agende uma visita</a></div></div>
</div></section>
<div class="wrap" style="margin-top:56px">{TRUST}</div>
<section class="sec"><div class="wrap"><div class="block yellow"{R(kind="zoom")}><span class="over">Nossos diferenciais</span><h2>Por que escolher a Bambolê?</h2></div><ol class="steps">{"".join(f'<li{R(delay=(i%2)*80)}><b>{a}</b><span>{b}</span></li>' for i, (a, b) in enumerate(DIFERENCIAIS))}</ol></div></section>
{espaco_block(FOTOS_SOBRE, "Nosso espaço, pensado para o desenvolvimento")}
{reviews_block()}{start_steps()}{cta_band("Vamos conversar?", "Agende uma visita e conheça a clínica.")}'''
pages["/sobre/"] = page("/sobre/", "Sobre a Clínica Bambolê e a neuropsicóloga Angélica Lopes | BH",
    "Conheça a Clínica Bambolê, na Pampulha (BH), fundada pela neuropsicóloga Angélica Lopes (CRP 04/37600): dez áreas integradas para o desenvolvimento.", sobre,
    [clinic_schema(), person_schema(), {"@type": "AboutPage", "url": BASE + "/sobre/"}], og_img="/assets/angelica.jpg",
    crumbs=[("Início", "/"), ("Sobre", "/sobre/")])

# ---------- COMO ATENDEMOS ----------
ca_faq = [FAQ_GERAL[3], FAQ_GERAL[5], FAQ_GERAL[6], FAQ_GERAL[4]]
como = head_block("Informações", "Como atendemos", "Sessões de 50 minutos, atendimento individual, presencial e online.", "azul") + \
    tldr("Na Clínica Bambolê, em Belo Horizonte, as sessões duram 50 minutos e são individuais (exceto oficinas em grupo). O atendimento é presencial, na Pampulha, ou online, conforme o serviço. É particular, com nota para reembolso do plano de saúde.") + \
    f'<section class="sec"><div class="wrap"><ol class="steps">{"".join(f"<li{R(delay=(i%2)*80)}><b>{a}</b><span>{b}</span></li>" for i, (a, b) in enumerate(COMO_ATENDEMOS))}</ol></div></section>' + \
    start_steps() + faq_html(ca_faq) + f'<section class="sec"><div class="wrap contact">{form_html()}{loc_card()}</div></section>' + cta_band()
pages["/como-atendemos/"] = page("/como-atendemos/", "Como atendemos: sessões, horários e reembolso | Clínica Bambolê BH",
    "Sessões de 50 minutos, individuais, presenciais na Pampulha ou online. Atendimento particular com nota para reembolso. Saiba como agendar na Clínica Bambolê.", como,
    [faq_schema(ca_faq)], crumbs=[("Início", "/"), ("Como atendemos", "/como-atendemos/")])

# ---------- FAQ ----------
allfaq = FAQ_GERAL + [SERVICOS[0]["faq"][0], SERVICOS[1]["faq"][0], tea_faq[0], tdah_faq[0]]
faqp = head_block("Dúvidas", "Perguntas frequentes", "Respostas rápidas sobre a Clínica Bambolê.", "rosa") + faq_html(allfaq, "Tudo o que as famílias costumam perguntar") + \
    f'<section class="sec"><div class="wrap contact">{form_html("Não achou sua dúvida?", "Mande sua pergunta e a equipe responde pelo WhatsApp.")}{loc_card()}</div></section>' + cta_band("Não achou sua dúvida?", "Pergunte direto para a equipe.")
pages["/perguntas-frequentes/"] = page("/perguntas-frequentes/", "Perguntas frequentes | Clínica Bambolê – Autismo e TDAH em BH",
    "Endereço, horários, plano de saúde, atendimento online, avaliação neuropsicológica e terapia ABA: respostas rápidas sobre a Clínica Bambolê em BH.", faqp,
    [faq_schema(allfaq)], crumbs=[("Início", "/"), ("Perguntas frequentes", "/perguntas-frequentes/")])

# ---------- CONTATO ----------
cont = head_block("Contato", "Fale com a Clínica Bambolê", "WhatsApp, telefones, endereço e horários.", "azul") + \
    tldr(f'A Clínica Bambolê fica na {NAP["rua"]}, bairro {NAP["bairro"]} (Pampulha), Belo Horizonte – MG, {NAP["cep"]}. Atende de segunda a sexta, das 8h às 20h, e aos sábados, das 8h às 16h. WhatsApp: {NAP["whats"]}.') + \
    f'<section class="sec"><div class="wrap contact">{form_html()}{loc_card()}</div></section>' + \
    f'<section class="sec"><div class="wrap wrap-narrow"><span class="over">Outros canais</span><p>Telefones: {NAP["tel2"]} · {NAP["tel3"]}<br>Instagram: <a href="{NAP["instagram"]}" target="_blank" rel="noopener">@clinicabambole</a></p></div></section>'
pages["/contato/"] = page("/contato/", "Contato e endereço | Clínica Bambolê – Santa Amélia, Pampulha, BH",
    f'WhatsApp {NAP["whats"]}. {NAP["rua"]}, Santa Amélia (Pampulha), Belo Horizonte. Seg a sex 8h–20h, sáb 8h–16h. Agende na Clínica Bambolê.', cont,
    [{"@type": "ContactPage", "url": BASE + "/contato/"}, clinic_schema()], crumbs=[("Início", "/"), ("Contato", "/contato/")])

p404 = page("/404.html", "Página não encontrada | Clínica Bambolê", "Página não encontrada.",
    '<section class="sec"><div class="wrap wrap-narrow center"><div class="panel"><h1>Página não encontrada</h1><p class="muted">O endereço pode ter mudado. Veja os serviços ou fale com a gente.</p><p><a class="btn btn-navy" href="/servicos/">Ver serviços</a></p></div></div></section>', [], noindex=True)

