# -*- coding: utf-8 -*-
import json, os, html, shutil, datetime
from content import *

OUT = "dist"
TODAY = "2026-11-20"
E = html.escape

CSS = open("site.css", encoding="utf-8").read()

from urllib.parse import quote
def wa(svc=None):
    alvo = (svc[0].lower() + svc[1:]) if svc and not svc[:2].isupper() else svc
    msg = (f"Olá! Vim pelo site da Clínica Bambolê e tenho interesse em {alvo}. Gostaria de saber como agendar." if svc
           else "Olá! Vim pelo site da Clínica Bambolê e gostaria de agendar.")
    return "https://wa.me/5531996225819?text=" + quote(msg)

def wa_icon(cls=""):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#wa"/></svg>'

SVG_DEFS = '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><symbol id="wa" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2c0 1.3.9 2.5 1.1 2.7.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2l-.7-.3Z"/></symbol></svg>'

NAV = [("/servicos/", "Serviços"), ("/autismo-tea/", "Autismo"), ("/tdah/", "TDAH"), ("/artigos/", "Artigos"), ("/sobre/", "Sobre"), ("/perguntas-frequentes/", "Dúvidas"), ("/contato/", "Contato")]

CLINIC_ID = BASE + "/#clinica"
PERSON_ID = BASE + "/sobre/#angelica-lopes"
ADDR_FULL = f'{NAP["rua"]} – {NAP["bairro"]}, {NAP["cidade"]} – {NAP["uf"]}, {NAP["cep"]}'

def clinic_schema():
    return {
        "@type": "MedicalClinic",
        "@id": CLINIC_ID,
        "name": NAP["nome"],
        "alternateName": ["Bambolê Centro de Desenvolvimento Humano", "Clínica Bambolê – Autismo e TDAH em BH"],
        "description": "Clínica multidisciplinar em Belo Horizonte dedicada ao atendimento a crianças, adolescentes e adultos neurodivergentes (autismo/TEA, TDAH e outros), com avaliação neuropsicológica e dez áreas integradas de terapia.",
        "url": BASE + "/",
        "logo": BASE + "/assets/logo.png",
        "image": [BASE + "/assets/angelica-principal.jpg", BASE + "/assets/angelica-perfil.jpg", BASE + "/assets/sala-atendimento.jpg", BASE + "/assets/angelica.jpg", BASE + "/assets/espaco-sala-ampla.jpg", BASE + "/assets/espaco-recepcao.jpg", BASE + "/assets/espaco-acervo.jpg"],
        "telephone": NAP["whats_e164"],
        "email": NAP["email"],
        "priceRange": "Particular, com nota para reembolso",
        "address": {"@type": "PostalAddress", "streetAddress": NAP["rua"] + " – " + NAP["bairro"], "addressLocality": NAP["cidade"], "addressRegion": NAP["uf"], "postalCode": NAP["cep"], "addressCountry": "BR"},
        "hasMap": NAP["maps"],
        "areaServed": [{"@type": "City", "name": "Belo Horizonte"}, {"@type": "Place", "name": "Pampulha, Belo Horizonte"}],
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "20:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "08:00", "closes": "16:00"},
        ],
        "sameAs": [NAP["instagram"]],
        "founder": {"@id": PERSON_ID},
        "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": True} for n in ["Salas climatizadas e silenciosas", "Sala de Terapia Ocupacional e Psicomotricidade", "Banheiro acessível"]],
        "knowsAbout": ["Transtorno do Espectro Autista (TEA)", "TDAH", "Avaliação neuropsicológica", "Análise do Comportamento Aplicada (ABA)", "Terapia Cognitivo-Comportamental", "Fonoaudiologia", "Terapia ocupacional", "Psicomotricidade", "Psicopedagogia", "Musicoterapia"],
        "availableService": [{"@type": "MedicalTherapy", "name": s["nome"], "url": f'{BASE}/servicos/{s["slug"]}/'} for s in SERVICOS],
    }

def person_schema():
    return {"@type": "Person", "@id": PERSON_ID, "name": "Angélica Vany Ribeiro Lopes", "alternateName": "Angélica Lopes",
            "jobTitle": "Neuropsicóloga e fundadora", "worksFor": {"@id": CLINIC_ID}, "image": BASE + "/assets/angelica.jpg",
            "identifier": {"@type": "PropertyValue", "propertyID": "CRP", "value": "04/37600"},
            "url": BASE + "/sobre/"}

def crumbs_schema(crumbs):
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + u} for i, (n, u) in enumerate(crumbs)]}

def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def ld(graph):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False) + '</script>'

def header(path):
    links = "".join(f'<a href="{u}"{" aria-current=page" if path.startswith(u) else ""}>{n}</a>' for u, n in NAV)
    return f'''<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="top"><div class="wrap">
<a href="/" class="logo" aria-label="Clínica Bambolê – página inicial"><img src="/assets/logo.png" alt="Bambolê – Centro de Desenvolvimento Humano" width="360" height="108"></a>
<nav class="nav" aria-label="Principal">{links}</nav>
<a class="btn btn-wa btn-sm" href="{WA}" target="_blank" rel="noopener">{wa_icon()}<span>WhatsApp</span></a>
<details class="menu"><summary aria-label="Abrir menu"><span></span><span></span><span></span></summary><nav aria-label="Menu">{links}<a href="{WA}" target="_blank" rel="noopener">Agende pelo WhatsApp</a></nav></details>
</div><div class="arco"></div></header>'''

IG_POSTS = [("https://www.instagram.com/p/DfTGrRSTdvt/", "/assets/ig-birra.jpg", "Post: o que parece birra x o que pode ser dificuldade emocional"),
            ("https://www.instagram.com/p/DfqPA6xTvbB/", "/assets/ig-transtornos.jpg", "Post: características principais de cada transtorno"),
            ("https://www.instagram.com/p/DRc_0BRErFr/", "/assets/ig-bambole.jpg", "Post: o que está por trás da Clínica Bambolê"),
            ("https://www.instagram.com/p/DfKPciSoLvh/", "/assets/ig-medo-escuro.jpg", "Post: se seu filho tem medo do escuro")]
IG_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2.2c3.2 0 3.6 0 4.8.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.8c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2Zm0 4.9a4.9 4.9 0 1 0 0 9.8 4.9 4.9 0 0 0 0-9.8Zm0 8.1a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4Zm5.1-9.4a1.1 1.1 0 1 0 0 2.3 1.1 1.1 0 0 0 0-2.3Z"/></svg>'

def ig_band():
    tiles = "".join(f'<a class="ig-tile" href="{u}" target="_blank" rel="noopener" aria-label="{E(alt)} (abre o Instagram)" data-reveal data-delay="{i*80}"><img src="{src}" alt="{E(alt)}" width="480" height="600" loading="lazy"><span>{IG_SVG}</span></a>' for i, (u, src, alt) in enumerate(IG_POSTS))
    return f'''<section class="ig"><div class="wrap"><div class="ig-head" data-reveal><div><span class="over">Instagram</span><h2>Acompanhe a Bambolê no Instagram</h2><p class="muted">Dicas sobre desenvolvimento, comportamento e bastidores da clínica.</p></div><a class="btn btn-ig" href="{NAP["instagram"]}" target="_blank" rel="noopener">{IG_SVG}Seguir @clinicabambole</a></div><div class="ig-grid">{tiles}</div></div></section>'''

def footer():
    svc = "".join(f'<li><a href="/servicos/{s["slug"]}/">{s["nome"]}</a></li>' for s in SERVICOS)
    hrs = "<br>".join(f"{d}: {h}" for d, h in HORARIO)
    return ig_band() + f'''<footer class="foot"><div class="wrap grid4">
<div><img src="/assets/logo.png" alt="Bambolê – Centro de Desenvolvimento Humano" width="180" height="54" loading="lazy"><p class="muted">Cuidar do desenvolvimento, juntos.</p><p><a href="{NAP["instagram"]}" target="_blank" rel="noopener">@clinicabambole</a></p></div>
<div><h2 class="over">Serviços</h2><ul class="links">{svc}</ul></div>
<div><h2 class="over">Endereço</h2><address>{NAP["rua"]}<br>{NAP["bairro"]} (Pampulha)<br>{NAP["cidade"]} – {NAP["uf"]}, {NAP["cep"]}</address><p><a href="{NAP["maps"]}" target="_blank" rel="noopener">Ver no Google Maps →</a></p></div>
<div><h2 class="over">Contato</h2><p>WhatsApp: <a href="{WA}" target="_blank" rel="noopener">{NAP["whats"]}</a><br>E-mail: <a href="mailto:{NAP["email"]}">{NAP["email"]}</a></p><p class="muted">{hrs}</p></div>
</div><div class="wrap legal"><span>CLÍNICA BAMBOLÊ</span><span>Responsável técnica: Angélica Lopes · Neuropsicóloga · CRP 04/37600</span></div><div class="arco"></div></footer>
<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Agende pelo WhatsApp">{wa_icon()}</a>
<div class="stickybar" role="region" aria-label="Agendamento rápido"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{wa_icon()}WhatsApp</a><a class="btn btn-line" href="#agendar">Quero agendar</a></div>'''

def page(path, title, desc, body, graph, og_img="/assets/sala-atendimento.jpg", noindex=False, crumbs=None):
    url = BASE + path
    g = [{"@type": "WebSite", "@id": BASE + "/#site", "url": BASE + "/", "name": "Clínica Bambolê", "inLanguage": "pt-BR", "publisher": {"@id": CLINIC_ID}},
         {"@type": "WebPage", "@id": url + "#pagina", "url": url, "name": title, "description": desc, "inLanguage": "pt-BR", "isPartOf": {"@id": BASE + "/#site"}, "about": {"@id": CLINIC_ID}, "dateModified": TODAY, **({"reviewedBy": {"@id": PERSON_ID}} if url.count("/artigos/") and url.rstrip("/") != BASE + "/artigos" else {})}]
    if crumbs:
        g.append(crumbs_schema(crumbs))
    g += graph
    bc = ""
    if crumbs and len(crumbs) > 1:
        bc = '<nav class="crumbs wrap" aria-label="Você está em"><ol>' + "".join(
            (f'<li><a href="{u}">{n}</a></li>' if i < len(crumbs) - 1 else f'<li aria-current="page">{n}</li>') for i, (n, u) in enumerate(crumbs)) + '</ol></nav>'
    robots = '<meta name="robots" content="noindex, follow">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{TRACK["ga4"]}');gtag('config','{TRACK["ads"]}');window.ADS_CONV='{TRACK["ads_conv"]}';</script>
<script async src="https://www.googletagmanager.com/gtag/js?id={TRACK["ga4"]}"></script>
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{TRACK["gtm"]}');</script>
<script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','{TRACK["meta"]}');fbq('track','PageView');</script>
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
{robots}
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#003E66">
<link rel="icon" type="image/png" href="/assets/favicon.png">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR"><meta property="og:site_name" content="Clínica Bambolê">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}{og_img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="BR-MG"><meta name="geo.placename" content="Belo Horizonte">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@700&family=Figtree:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<script src="/assets/site.js" defer></script>
<link rel="alternate" type="text/plain" href="/llms.txt" title="Resumo para IA">
{ld(g)}
</head>
<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={TRACK["gtm"]}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
{SVG_DEFS}
{header(path)}
{bc}
<main id="conteudo">
{body}
</main>
{footer()}
</body>
</html>
'''

def tldr(text):
    return f'<aside class="tldr wrap-narrow"><p class="over">Em resumo</p><p>{text}</p></aside>'

M_FAQ = '<img class="parrot" src="/assets/angelica-duvidas.webp" alt="Personagem ilustrada da Angélica Lopes explicando" width="201" height="347" loading="lazy">'

def faq_html(faqs, title="Perguntas frequentes", mascot=True):
    items = "".join(f'<details class="qa" data-reveal><summary><h3>{E(q)}</h3></summary><p>{E(a)}</p></details>' for q, a in faqs)
    return f'<section class="sec"><div class="wrap wrap-narrow faq-wrap">{M_FAQ if mascot else ""}<span class="over">Dúvidas</span><h2>{title}</h2><div class="faq">{items}</div></div></section>'

def cta_m(t):
    if t.startswith("Vamos conversar"):
        return '<img class="cta-m" src="/assets/angelica-calma.webp" alt="Personagem ilustrada da Angélica Lopes, sorrindo" width="215" height="415" loading="lazy">'
    return '<img class="cta-m" src="/assets/angelica-pensativa.webp" alt="Personagem ilustrada da Angélica Lopes, pensativa" width="178" height="342" loading="lazy">'

def cta_band(t="Ficou com alguma dúvida?", s="Fale com a gente e agende uma conversa.", svc=None):
    return f'''<section class="sec"><div class="wrap"><div class="block cta has-m" data-reveal="zoom"><img class="wm" src="/assets/bo.png" alt="" aria-hidden="true" width="160" height="136" loading="lazy">{cta_m(t)}<div><h2>{t}</h2><p>{s}</p></div><a class="wa" href="{wa(svc)}" target="_blank" rel="noopener"><span>{wa_icon()}</span>Agende pelo WhatsApp</a></div></div></section>'''

def reviews_html(items=None):
    return f'''<section class="sec" id="avaliacoes"><div class="wrap"><div class="block rev-head" data-reveal><div><span class="over">Google</span><h2>Avaliações da clínica</h2><p>As avaliações das famílias ficam no nosso perfil do Google.</p></div><div class="score"><strong>5,0</strong><div><span class="stars" aria-label="5 de 5 estrelas">★★★★★</span><small>nota no Google</small></div></div><a class="btn btn-line" href="{{NAP["maps"]}}" target="_blank" rel="noopener">Ver no Google →</a></div></div></section>'''

def form_html(title="Vamos começar?", lead="Preencha seus dados e a equipe da Bambolê retorna pelo WhatsApp.", svc=""):
    opts = "".join(f'<option{" selected" if s["nome"]==svc else ""}>{s["nome"]}</option>' for s in SERVICOS)
    return f'''<div class="panel" id="agendar" data-reveal><span class="over">Agendamento</span><h2>{title}</h2><p class="muted">{lead}</p>
<form name="pedido" method="POST" action="/obrigado/" netlify data-netlify="true" netlify-honeypot="bot-field">
<input type="hidden" name="form-name" value="pedido"><input type="hidden" name="pagina" value="">
<p class="hp"><label>Não preencha: <input name="bot-field"></label></p>
<div><label for="nome">Nome</label><input id="nome" name="nome" type="text" autocomplete="name" required></div>
<div class="row"><div><label for="whatsapp">WhatsApp</label><input id="whatsapp" name="whatsapp" type="tel" inputmode="tel" autocomplete="tel" placeholder="(31) 9xxxx-xxxx" required></div>
<div><label for="email">E-mail</label><input id="email" name="email" type="email" autocomplete="email"></div></div>
<div class="row"><div><label for="bairro">Bairro</label><input id="bairro" name="bairro" type="text" autocomplete="address-level3" required></div>
<div><label for="servico">Serviço de interesse</label><select id="servico" name="servico"><option value=""{" selected" if not svc else ""}>Ainda não sei</option>{opts}</select></div></div>
<div><label for="pedido">O que você precisa?</label><textarea id="pedido" name="pedido" required placeholder="Conte rapidamente o que está acontecendo e a idade do paciente"></textarea></div>
<button class="btn btn-navy" type="submit">Quero ser chamado no WhatsApp</button>
<p class="note">Resposta pelo WhatsApp em horário comercial. Seus dados são usados só para responder ao seu pedido.</p></form></div>'''

def loc_card():
    hrs = "<br>".join(f"{d}: {h}" for d, h in HORARIO)
    return f'''<div class="loc" data-reveal><div class="map"><iframe src="https://www.google.com/maps?q=Cl%C3%ADnica+Bambol%C3%AA,+Rua+Alair+Marques+Rodrigues,+551,+Santa+Am%C3%A9lia,+Belo+Horizonte+-+MG&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa: Clínica Bambolê, Rua Alair Marques Rodrigues, 551, Santa Amélia, Belo Horizonte"></iframe></div>
<div class="loc-info"><div><span class="over">Onde estamos</span><p>{NAP["rua"]}<br>{NAP["bairro"]} (Pampulha), {NAP["cidade"]} – {NAP["uf"]}<br>{NAP["cep"]}</p><p><a href="{NAP["maps"]}" target="_blank" rel="noopener">Como chegar →</a></p></div>
<div><span class="over">Horário</span><p>{hrs}</p></div>
<div><span class="over">Contato</span><p><a href="{WA}" target="_blank" rel="noopener">WhatsApp {NAP["whats"]}</a><br><a href="mailto:{NAP["email"]}">{NAP["email"]}</a></p></div></div></div>'''

def svc_list(cols=2):
    cores = ["ciano", "laranja", "rosa", "amarelo"]
    return '<ul class="svc-list">' + "".join(
        f'<li><a href="/servicos/{s["slug"]}/"><i class="dot" style="background:{COR[cores[i%4]]}"></i><span><b>{s["nome"]}</b><small>{s["linha"]}</small></span><em aria-hidden="true">→</em></a></li>' for i, s in enumerate(SERVICOS)) + '</ul>'

def head_block(over, h1, lead, color="azul"):
    return f'<section class="phead"><div class="wrap"><div class="block" style="--ac:{COR[color]}"><span class="over">{over}</span><h1>{h1}</h1><p class="lead-on">{lead}</p></div></div></section>'

