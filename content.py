# -*- coding: utf-8 -*-
# Conteúdo do site da Clínica Bambolê.
# Fontes: ficha do Google Maps, Catálogo de Serviços / design system da marca, Instagram @clinicabambole.
# Descrições gerais das terapias são explicativas (o que é cada área), sem promessas de resultado.

BASE = "https://clinicabambole.com.br"

NAP = {
    "nome": "Clínica Bambolê",
    "nome_longo": "Clínica Bambolê – Centro de Desenvolvimento Humano",
    "rua": "Rua Alair Marques Rodrigues, 551",
    "bairro": "Santa Amélia",
    "regiao": "Pampulha",
    "cidade": "Belo Horizonte",
    "uf": "MG",
    "cep": "31560-220",
    "whats": "(31) 99622-5819",
    "whats_e164": "+5531996225819",
    "tel3": "(31) 3427-2436",
    "email": "bambolecdhumano@gmail.com",
    "instagram": "https://www.instagram.com/clinicabambole/",
    "maps": "https://share.google/4faGJPG3BIIF9m1kt",
}

WA = "https://wa.me/5531996225819?text=" + "Ol%C3%A1!%20Vim%20pelo%20site%20da%20Cl%C3%ADnica%20Bambol%C3%AA%20e%20gostaria%20de%20agendar."

HORARIO = [("Segunda a sexta", "8h às 20h"), ("Sábado", "8h às 16h"), ("Domingo", "Fechado")]

REVIEWS = [
    ("Laize Barbosa", "Meu filho é acompanhado pelas profissionais da clínica Bambolê por case 10 meses(TO e Fono), é a evolução do desenvolvimento é brilhante.Sempre com Feedback pós consulta e que nos ajuda muito a lidar em situações no dia.Os ambientes todos adaptados para cada especialidade."),
    ("Rejane Gonçalves", "Clínica excelente! Profissionais ótimos, estrutura maravilhosa! Meu filho (TEA) está desenvolvendo muito com as terapias. Só tenho a agradecer. Recomendo de mais!"),
    ("Carl Carvalho", "O diagnóstico precoce associado ao acompanhamento psicológico ampliam a autonomia e a qualidade de vida da pessoa neurodivergente. A clínica é excelente, conta com uma infraestrutura completa e profissionais altamente capacitados!"),
    ("Bruna Cólen", "Angélica é uma profissional excepcional! Uma verdadeira alma boa e possui uma competência única. Recomendo a clínica para todos!"),
]

DIFERENCIAIS = [
    ("Fundada e acompanhada por neuropsicóloga", "Angélica Lopes, com 14 anos de experiência, acompanha de perto toda a equipe."),
    ("Tudo em um só lugar", "Dez áreas integradas em um só plano: menos tempo no trânsito e mais aproveitamento do seu dia."),
    ("Experiência com neurodivergência", "Psicólogas com formação em ABA e TCC, e equipe de várias áreas que conversa entre si."),
    ("Sessões de 50 minutos", "Atendimento individual, uma pessoa por vez."),
    ("Espaço pensado para o desenvolvimento", "Salas climatizadas e silenciosas, sala de TO e psicomotricidade e acervo escolhido pela neuropsicologia."),
    ("Família e escola por perto", "Orientação, devolutivas e parceria em cada etapa."),
    ("Para todas as fases da vida", "Crianças, adolescentes e adultos, típicos e atípicos."),
]

COMO_ATENDEMOS = [
    ("Sessões de 50 minutos", "Tempo de verdade para cada atendimento."),
    ("Atendimento individual", "Uma pessoa por vez, com a atenção total do profissional, exceto nas atividades em grupo."),
    ("Equipe preparada para a neurodivergência", "Profissionais experientes, com psicólogas com formação em ABA."),
    ("Crianças, adolescentes e adultos", "Típicos e atípicos, em cada fase da vida, com orientação à família."),
    ("Presencial e online", "Na clínica, no bairro Santa Amélia (Pampulha), ou por videochamada, conforme o serviço."),
    ("Particular, com nota para reembolso", "Emitimos nota para você solicitar reembolso ao seu plano de saúde."),
]

# Serviços: slug, nome, nome curto p/ título, linha do catálogo, cor, intro, para quem, como, faqs
SERVICOS = [
 {
  "slug": "avaliacao-neuropsicologica", "nome": "Avaliação neuropsicológica", "titulo": "Avaliação neuropsicológica em BH",
  "linha": "Perfil cognitivo e emocional", "cor": "azul",
  "resumo": "A avaliação neuropsicológica da Clínica Bambolê, na Pampulha, em Belo Horizonte, mapeia atenção, memória, funções executivas e aspectos emocionais de crianças, adolescentes e adultos. São em média 10 a 15 sessões, com mais de 40 testes e escalas padronizados, laudo completo e devolutiva para paciente, família, escola e médicos.",
  "intro": ["Avaliação neuropsicológica completa: mapeia atenção, memória, funções executivas e aspectos emocionais para orientar médicos, escola e família, construindo um plano terapêutico para o desenvolvimento do paciente no dia a dia.",
            "Na Bambolê, a avaliação é conduzida a partir da neuropsicologia, área de formação da fundadora, a neuropsicóloga Angélica Lopes."],
  "para_quem": ["Crianças, adolescentes e adultos", "Suspeita de TEA ou TDAH", "Suspeita de TOD", "Deficiência intelectual", "Altas habilidades", "Alzheimer e/ou demência", "Atenção, memória e aprendizagem", "Ansiedade, depressão ou TOC"],
  "passos": [("Anamnese", "Entrevista inicial com paciente e/ou família para entender o caso e definir o que será aplicado."),
             ("Testes e escuta", "Aplicação dos testes e escuta do paciente, da família e da escola."),
             ("Laudo e devolutiva", "Laudo completo, relatório e reunião de devolutiva explicando as áreas e os resultados ao paciente, à família, à escola e aos médicos."),
             ("Próximos passos", "Plano terapêutico e encaminhamento para as áreas de reabilitação.")],
  "destaque": ("Em média, de 10 a 15 sessões.", "Mais de 40 testes e escalas padronizados, para crianças, adolescentes e adultos."),
  "faq": [("Quantas sessões tem a avaliação neuropsicológica na Bambolê?", "Em média, de 10 a 15 sessões. O número exato depende da idade e da demanda de cada paciente."),
          ("A avaliação neuropsicológica serve para investigar autismo e TDAH?", "Sim. Suspeita de TEA ou TDAH está entre as principais razões para a avaliação. Ela mapeia atenção, memória, funções executivas e aspectos emocionais e ajuda médicos, família e escola na tomada de decisão."),
          ("Adultos também podem fazer a avaliação?", "Sim. A Bambolê avalia crianças, adolescentes e adultos, com mais de 40 testes e escalas padronizados."),
          ("O que recebo ao final da avaliação?", "Laudo completo, relatório e uma reunião de devolutiva que explica os resultados ao paciente, à família, à escola e aos médicos, além do plano terapêutico e dos encaminhamentos.")],
 },
 {
  "slug": "terapia-aba", "nome": "Psicoterapia (ABA e TCC)", "titulo": "Terapia ABA e psicoterapia em BH",
  "linha": "ABA, TCC, PECS e técnicas lúdicas", "cor": "laranja",
  "resumo": "Na Clínica Bambolê, em Belo Horizonte, a psicoterapia é feita por psicólogas com formação em ABA (Análise do Comportamento Aplicada), também com TCC, PECS e técnicas lúdicas. As sessões são individuais, de 50 minutos, para crianças, adolescentes e adultos, típicos e atípicos.",
  "intro": ["A ABA (Análise do Comportamento Aplicada) é uma abordagem da psicologia que planeja intervenções a partir da observação do comportamento e do registro dos avanços. No autismo, costuma ser usada para ensinar habilidades de comunicação, sociais e de autonomia no dia a dia.",
            "Na Bambolê, a psicoterapia combina ABA, TCC (Terapia Cognitivo-Comportamental), PECS (comunicação por troca de figuras) e técnicas lúdicas, de acordo com a idade e a necessidade de cada paciente."],
  "para_quem": ["Crianças, adolescentes e adultos com TEA", "Pessoas com TDAH ou TOD", "Dificuldades de comunicação e interação", "Comportamentos desafiadores e regulação emocional", "Ansiedade e outras demandas emocionais"],
  "passos": [("Avaliação inicial", "Conversa com a família e o paciente para entender a rotina, as dificuldades e os objetivos."),
             ("Plano individual", "Metas definidas para cada paciente, com a abordagem mais adequada: ABA, TCC, PECS ou técnicas lúdicas."),
             ("Sessões de 50 minutos", "Atendimento individual, com acompanhamento do progresso ao longo do tempo."),
             ("Família e escola por perto", "Orientação e devolutivas para que o que é trabalhado na sessão chegue ao dia a dia.")],
  "faq": [("O que é terapia ABA?", "ABA significa Análise do Comportamento Aplicada. É uma abordagem da psicologia que planeja a intervenção com base na observação do comportamento e no registro dos avanços, muito usada no acompanhamento de pessoas com autismo."),
          ("A Bambolê tem psicólogas com formação em ABA?", "Sim. A equipe de psicologia da Bambolê inclui psicólogas com formação em ABA."),
          ("A terapia ABA é só para crianças?", "Não. Na Bambolê a psicoterapia atende crianças, adolescentes e adultos, típicos e atípicos."),
          ("Quanto dura cada sessão?", "As sessões têm 50 minutos e o atendimento é individual.")],
 },
 {
  "slug": "fonoaudiologia", "nome": "Fonoaudiologia", "titulo": "Fonoaudiologia e reabilitação do PAC em BH",
  "linha": "Fala, linguagem, voz e processamento auditivo", "cor": "rosa",
  "resumo": "A fonoaudiologia da Clínica Bambolê, na Pampulha, em Belo Horizonte, trabalha fala, linguagem e voz e oferece Reabilitação do Processamento Auditivo Central (PAC), para crianças, adolescentes e adultos, típicos e atípicos, integrada às demais áreas da clínica.",
  "intro": ["A fonoaudiologia cuida da comunicação: fala, linguagem e voz. No desenvolvimento infantil, acompanha crianças com atraso de fala, dificuldades de linguagem e de comunicação, muito comuns em quadros como TEA e TDL (Transtorno do Desenvolvimento da Linguagem).",
            "A Bambolê também oferece Reabilitação do Processamento Auditivo Central (PAC). O processamento auditivo é a forma como o cérebro interpreta o que ouvimos. Quando há alteração (TPAC), a pessoa ouve bem, mas pode ter dificuldade para entender a fala em ambientes com barulho, seguir instruções, manter a atenção ao que escuta e aprender a ler e escrever. A reabilitação treina essas habilidades auditivas.",
            "Na Bambolê, a fonoaudiologia faz parte do plano integrado: a equipe conversa entre si e com a família para que os objetivos sejam os mesmos em todas as áreas."],
  "para_quem": ["Atraso na fala e na linguagem", "Dificuldades de comunicação no TEA", "Transtorno do Desenvolvimento da Linguagem (TDL)", "Transtorno do Processamento Auditivo Central (TPAC)", "Dificuldade para entender a fala em ambientes com barulho", "Trocas de sons e inteligibilidade da fala", "Questões de voz"],
  "passos": [("Avaliação fonoaudiológica", "Entendimento da comunicação do paciente e da queixa da família."),
             ("Plano terapêutico", "Objetivos claros, alinhados às outras terapias da clínica."),
             ("Sessões individuais", "Atendimentos de 50 minutos."),
             ("Orientação à família", "Estratégias para estimular a comunicação em casa e na escola.")],
  "faq": [("A Bambolê atende fonoaudiologia infantil?", "Sim. A fonoaudiologia atende crianças, adolescentes e adultos, típicos e atípicos."),
          ("Fonoaudiologia ajuda criança autista que não fala?", "A fonoaudiologia trabalha comunicação, fala e linguagem e é uma das áreas frequentemente indicadas no acompanhamento do autismo. A indicação e os objetivos são definidos após avaliação."),
          ("A Bambolê faz reabilitação do processamento auditivo central (PAC)?", "Sim. A fonoaudiologia da Bambolê oferece Reabilitação do Processamento Auditivo Central, que treina as habilidades auditivas de quem tem alteração no processamento auditivo (TPAC)."),
          ("Quais sinais podem indicar alteração do processamento auditivo?", "Dificuldade para entender a fala com barulho de fundo, pedir para repetir com frequência, dificuldade em seguir instruções, distração ao ouvir e dificuldades de leitura e escrita, mesmo com audição normal. A confirmação depende de avaliação específica."),
          ("A fonoaudiologia é integrada às outras terapias?", "Sim. Na Bambolê as dez áreas trabalham em um plano integrado, com a família e a escola por perto.")],
 },
 {
  "slug": "terapia-ocupacional", "nome": "Terapia ocupacional", "titulo": "Terapia ocupacional em BH",
  "linha": "Autonomia no dia a dia", "cor": "amarelo",
  "resumo": "A terapia ocupacional da Clínica Bambolê, em Belo Horizonte, trabalha a autonomia no dia a dia de crianças, adolescentes e adultos, em uma sala de TO própria, com sessões individuais de 50 minutos e orientação à família.",
  "intro": ["A terapia ocupacional (TO) ajuda a pessoa a participar das atividades do dia a dia com mais autonomia: autocuidado, alimentação, brincar, rotina escolar e organização. No desenvolvimento infantil, também olha para coordenação motora e para a forma como a criança reage a sons, texturas e movimentos.",
            "A Bambolê tem sala de TO e psicomotricidade preparada para esses atendimentos."],
  "para_quem": ["Dificuldades de autonomia e autocuidado", "Questões sensoriais (sons, texturas, movimento)", "Coordenação motora", "Organização da rotina", "Crianças com TEA, TDAH e outros quadros do neurodesenvolvimento"],
  "passos": [("Avaliação", "Observação da criança ou do adulto e conversa com a família."),
             ("Plano com objetivos do dia a dia", "Metas ligadas à rotina real do paciente."),
             ("Sessões na sala de TO", "Atendimentos individuais de 50 minutos."),
             ("Orientação à família e à escola", "Adaptações e estratégias para casa e sala de aula.")],
  "faq": [("O que a terapia ocupacional trabalha?", "Autonomia no dia a dia: autocuidado, alimentação, brincar, rotina, coordenação motora e respostas sensoriais."),
          ("A Bambolê tem sala própria de terapia ocupacional?", "Sim. A clínica tem sala de TO e psicomotricidade."),
          ("Terapia ocupacional é indicada para autismo?", "A TO é uma das áreas frequentemente indicadas no acompanhamento do autismo, principalmente para autonomia e questões sensoriais. A indicação é feita após avaliação.")],
 },
 {
  "slug": "psicomotricidade", "nome": "Psicomotricidade", "titulo": "Psicomotricidade em BH",
  "linha": "Corpo, movimento e coordenação", "cor": "ciano",
  "resumo": "A psicomotricidade da Clínica Bambolê, na Pampulha, em Belo Horizonte, trabalha corpo, movimento e coordenação, em sala de TO e psicomotricidade, com sessões individuais de 50 minutos.",
  "intro": ["A psicomotricidade trabalha a relação entre corpo, movimento, emoção e aprendizagem. Por meio do brincar e do movimento, estimula coordenação, equilíbrio, noção de espaço e organização do corpo.",
            "Na Bambolê, os atendimentos acontecem em sala preparada para movimento, integrados às demais terapias."],
  "para_quem": ["Coordenação motora e equilíbrio", "Noção de corpo e de espaço", "Agitação ou dificuldade de organização do movimento", "Crianças com TEA, TDAH e atrasos do desenvolvimento"],
  "passos": [("Avaliação psicomotora", "Observação do movimento e do brincar."),
             ("Plano individual", "Objetivos alinhados ao plano integrado."),
             ("Sessões de 50 minutos", "Em sala preparada para o movimento."),
             ("Devolutivas", "Orientação à família sobre como estimular em casa.")],
  "faq": [("O que é psicomotricidade?", "É uma área que trabalha a relação entre corpo, movimento, emoção e aprendizagem, usando o brincar e o movimento para estimular coordenação, equilíbrio e organização do corpo."),
          ("Qual a diferença entre psicomotricidade e terapia ocupacional?", "As duas se complementam. A psicomotricidade foca em corpo, movimento e coordenação; a terapia ocupacional foca na autonomia nas atividades do dia a dia.")],
 },
 {
  "slug": "psicopedagogia", "nome": "Psicopedagogia", "titulo": "Psicopedagogia em BH",
  "linha": "Aprender com confiança", "cor": "laranja",
  "resumo": "A psicopedagogia da Clínica Bambolê, em Belo Horizonte, acompanha crianças e adolescentes com dificuldades de aprendizagem para que aprendam com confiança, em parceria com a família e a escola.",
  "intro": ["A psicopedagogia investiga como a pessoa aprende e o que está dificultando esse processo: leitura, escrita, matemática, atenção e organização dos estudos.",
            "Na Bambolê, o trabalho é feito em parceria com a família e a escola, e conversa com a avaliação neuropsicológica quando ela foi realizada."],
  "para_quem": ["Dificuldades de leitura, escrita ou matemática", "Desatenção e desorganização nos estudos", "Estudantes com TDAH, TEA ou outros quadros", "Baixa autoestima ligada à escola"],
  "passos": [("Avaliação psicopedagógica", "Entendimento de como o estudante aprende."),
             ("Plano de intervenção", "Estratégias para as dificuldades encontradas."),
             ("Sessões individuais", "Atendimentos de 50 minutos."),
             ("Parceria com a escola", "Orientação e troca com professores.")],
  "faq": [("Quando procurar psicopedagogia?", "Quando a criança ou o adolescente tem dificuldades persistentes de aprendizagem, de leitura, escrita, matemática ou organização dos estudos."),
          ("A psicopedagogia conversa com a escola?", "Sim. Quando a família autoriza, a psicopedagoga conversa com professores e coordenação.")],
 },
 {
  "slug": "fisioterapia", "nome": "Fisioterapia", "titulo": "Fisioterapia neonatal e neurofuncional em BH",
  "linha": "Neonatal e neurofuncional", "cor": "rosa",
  "resumo": "A Clínica Bambolê, na Pampulha, em Belo Horizonte, oferece fisioterapia neonatal e neurofuncional, integrada às demais áreas do desenvolvimento.",
  "intro": ["A fisioterapia neurofuncional acompanha o desenvolvimento motor e as funções ligadas ao sistema nervoso. A fisioterapia neonatal acompanha bebês desde os primeiros meses.",
            "Na Bambolê, a fisioterapia faz parte do plano integrado com as outras nove áreas da clínica."],
  "para_quem": ["Bebês com atraso nos marcos motores", "Desenvolvimento motor de crianças atípicas", "Quadros neurológicos que afetam o movimento"],
  "passos": [("Avaliação fisioterapêutica", "Observação do desenvolvimento motor."),
             ("Plano individual", "Objetivos claros e alinhados à família."),
             ("Sessões de 50 minutos", "Atendimentos individuais."),
             ("Orientação à família", "Como estimular em casa.")],
  "faq": [("A Bambolê atende bebês?", "A clínica oferece fisioterapia neonatal e neurofuncional. Para saber se o caso do seu bebê se encaixa, fale com a equipe pelo WhatsApp."),
          ("O que é fisioterapia neurofuncional?", "É a área da fisioterapia que acompanha o desenvolvimento motor e as funções ligadas ao sistema nervoso.")],
 },
 {
  "slug": "oficinas-sociais", "nome": "Oficinas sociais", "titulo": "Oficinas de habilidades sociais em BH",
  "linha": "Habilidades sociais em grupo", "cor": "amarelo",
  "resumo": "As oficinas sociais da Clínica Bambolê, em Belo Horizonte, são atividades em grupo para treinar habilidades sociais: convivência, comunicação, espera, regras e cooperação.",
  "intro": ["As oficinas sociais são o único atendimento em grupo da Bambolê. Nelas, crianças e adolescentes praticam com colegas o que trabalham nas terapias individuais: conversar, esperar a vez, seguir regras, lidar com frustração e cooperar.",
            "O grupo é um espaço seguro para experimentar a convivência com mediação profissional."],
  "para_quem": ["Dificuldades de interação social", "Crianças e adolescentes com TEA, TDAH ou TOD", "Quem precisa praticar convivência em grupo"],
  "passos": [("Indicação", "A equipe avalia se a oficina faz sentido para o momento do paciente."),
             ("Grupo mediado", "Atividades em grupo com profissional."),
             ("Integração", "O que aparece no grupo volta para as terapias individuais."),
             ("Família por perto", "Devolutivas sobre a participação.")],
  "faq": [("As oficinas sociais são em grupo?", "Sim. É a única atividade em grupo da Bambolê; os demais atendimentos são individuais."),
          ("Para quem são as oficinas sociais?", "Para crianças e adolescentes que precisam praticar habilidades sociais em grupo, como conversar, esperar a vez e cooperar.")],
 },
 {
  "slug": "musicoterapia", "nome": "Musicoterapia", "titulo": "Musicoterapia em BH",
  "linha": "A música como terapia", "cor": "ciano",
  "resumo": "A Clínica Bambolê, na Pampulha, em Belo Horizonte, oferece musicoterapia: a música como recurso terapêutico para comunicação, interação, atenção e expressão emocional.",
  "intro": ["Na musicoterapia, a música é usada como recurso terapêutico. Cantar, tocar e ouvir ajudam a trabalhar comunicação, interação, atenção, expressão de emoções e regulação.",
            "Na Bambolê, a musicoterapia é integrada ao plano de cada paciente."],
  "para_quem": ["Crianças com TEA e dificuldades de comunicação", "Interação e atenção compartilhada", "Expressão e regulação emocional"],
  "passos": [("Avaliação", "Observação da relação do paciente com o som e a música."),
             ("Plano individual", "Objetivos terapêuticos claros."),
             ("Sessões de 50 minutos", "Atendimentos individuais."),
             ("Devolutivas", "Família informada sobre a evolução.")],
  "faq": [("O que é musicoterapia?", "É uma terapia que usa a música como recurso para trabalhar comunicação, interação, atenção e expressão emocional."),
          ("Precisa saber música para fazer musicoterapia?", "Não. A musicoterapia não é aula de música; a música é o meio da terapia.")],
 },
 {
  "slug": "orientacao-parental", "nome": "Orientação parental", "titulo": "Orientação e treinamento de pais em BH",
  "linha": "Treinamento de pais", "cor": "laranja",
  "resumo": "A orientação parental da Clínica Bambolê, em Belo Horizonte, é um treinamento de pais: a família aprende estratégias para lidar com comportamentos, rotina e emoções da criança em casa.",
  "intro": ["Na orientação parental, o foco são os pais e cuidadores. A equipe ensina estratégias práticas para lidar com birras, crises, rotina, limites e comunicação, e ajuda a família a entender o que está por trás de cada comportamento.",
            "Na Bambolê, a família participa do tratamento e, quando faz sentido, a escola também."],
  "para_quem": ["Pais de crianças com TEA, TDAH ou TOD", "Famílias que enfrentam birras e crises frequentes", "Quem quer alinhar a rotina de casa com as terapias"],
  "passos": [("Escuta da família", "Entendimento da rotina e das dificuldades."),
             ("Estratégias práticas", "Orientações para aplicar em casa."),
             ("Acompanhamento", "Revisão do que funcionou e ajustes."),
             ("Integração", "Alinhamento com as terapias da criança.")],
  "faq": [("O que é treinamento de pais?", "É um acompanhamento voltado aos pais e cuidadores, com estratégias práticas para lidar com comportamentos, rotina, limites e emoções da criança."),
          ("Birra e dificuldade emocional são a mesma coisa?", "Nem sempre. Nem todo comportamento difícil é falta de limite; às vezes há dificuldade de regulação emocional, sensorial ou de comunicação. A orientação parental ajuda a família a diferenciar e a agir.")],
 },
]

COR = {"azul": "var(--azul)", "laranja": "var(--laranja)", "rosa": "var(--rosa)", "amarelo": "var(--amarelo)", "ciano": "var(--ciano)"}
# texto sobre bloco de cor (contraste do design system)
COR_TXT = {"azul": "var(--off)", "rosa": "var(--off)", "laranja": "var(--marinho)", "amarelo": "var(--marinho)", "ciano": "var(--marinho)"}

FAQ_GERAL = [
    ("Onde fica a Clínica Bambolê?", "Na Rua Alair Marques Rodrigues, 551, bairro Santa Amélia, região da Pampulha, em Belo Horizonte (MG), CEP 31560-220."),
    ("Qual o horário de funcionamento?", "De segunda a sexta, das 8h às 20h, e aos sábados, das 8h às 16h. Aos domingos a clínica fica fechada."),
    ("Como agendar uma consulta?", "Pelo WhatsApp (31) 99622-5819, que é o canal mais rápido, ou pelo telefone (31) 3427-2436."),
    ("A Bambolê atende plano de saúde?", "O atendimento é particular, e a clínica emite nota para você solicitar reembolso ao seu plano de saúde."),
    ("A clínica atende adultos?", "Sim. A Bambolê atende crianças, adolescentes e adultos, típicos e atípicos."),
    ("Tem atendimento online?", "Sim. O atendimento é presencial, na clínica, ou online, por videochamada, conforme o serviço."),
    ("Quanto tempo dura cada sessão?", "As sessões têm 50 minutos e o atendimento é individual, exceto nas oficinas sociais, que são em grupo."),
    ("Quais serviços a Bambolê oferece?", "Dez áreas integradas: avaliação neuropsicológica, psicoterapia (ABA, TCC, PECS e técnicas lúdicas), fonoaudiologia (incluindo reabilitação do processamento auditivo central), terapia ocupacional, psicomotricidade, psicopedagogia, fisioterapia, oficinas sociais, musicoterapia e orientação parental."),
    ("Quem é a responsável pela clínica?", "A Bambolê foi fundada pela neuropsicóloga Angélica Lopes (CRP 04/37600), com 14 anos de experiência, que acompanha de perto toda a equipe."),
    ("A Bambolê atende autismo e TDAH?", "Sim. A clínica atende crianças, adolescentes e adultos neurodivergentes, com psicólogas com formação em ABA e TCC e uma equipe de dez áreas."),
]

# ---- Atualização com o Catálogo de Serviços oficial (artefato "Catálogo de Serviços Bambolê") ----
_CAT = {
 "avaliacao-neuropsicologica": dict(
    foto=("sala-atendimento.jpg", "Angélica Lopes em uma sala de atendimento da Clínica Bambolê"),
    equipe=["Conduzida a partir da neuropsicologia, com a supervisão da neuropsicóloga Angélica Lopes (CRP 04/37600)", "Mais de 40 testes e escalas padronizados", "Acervo escolhido pela neuropsicologia"]),
 "terapia-aba": dict(
    intro0="Acompanhamento psicológico para crianças, adolescentes e adultos, típicos e atípicos: de ansiedade e questões emocionais ao autismo, com ABA, TCC, PECS e técnicas lúdicas.",
    para_quem=["Crianças, adolescentes e adultos", "Autismo (TEA), TDAH e outras condições", "Ansiedade, depressão e TOC", "Quem quer lidar melhor com as emoções", "Intervenção precoce"],
    passos=[("Avaliação das necessidades", "Cada paciente é avaliado para entender as necessidades e os objetivos."), ("Plano personalizado", "Plano individual e lúdico para crianças, com ABA, TCC, PECS ou técnicas lúdicas."), ("Família e escola juntas", "Para crianças, família e escola participam do processo."), ("Sessões de 50 minutos", "Atendimento individual, com psicólogas com formação em ABA e TCC.")],
    foto=("espaco-sala-puff.jpg", "Sala de atendimento da Clínica Bambolê, com tatame e puff"),
    equipe=["Psicólogas com formação em ABA e TCC", "Formação em autismo baseada em evidências", "Protocolo VB-MAPP e orientação a pais e aplicadores"]),
 "fonoaudiologia": dict(
    intro0="Atendimento para crianças, adolescentes e adultos, com planos personalizados para melhorar a comunicação e a qualidade de vida.",
    para_quem=["Comunicação, fala, voz e linguagem escrita", "Atraso de fala, trocas fonológicas, gagueira e ceceio", "Reabilitação do Processamento Auditivo Central (PAC)", "Comunicação no TEA e Comunicação Aumentativa e Alternativa (CAA)", "Adultos que querem se comunicar de forma mais clara"],
    passos=[("Avaliação", "Avaliação de fala, linguagem, voz e processamento auditivo."), ("Terapia individual", "Exercícios e, para crianças, atividades lúdicas."), ("Orientação à família e à escola", "Estratégias para o dia a dia."), ("Sessões de 50 minutos", "Atendimento individual.")],
    foto=("espaco-painel-sensorial.jpg", "Painel de atividades e estímulos da Clínica Bambolê"),
    equipe=["Comunicação Aumentativa e Alternativa (CAA) e comunicação no TEA", "Reabilitação do Processamento Auditivo Central e reabilitação do TDAH"]),
 "terapia-ocupacional": dict(
    intro0="Promove habilidades diárias, sociais e cognitivas para a autonomia e o desenvolvimento integral de crianças, adolescentes e adultos, típicos ou neurodivergentes.",
    para_quem=["Crianças, adolescentes e adultos", "Autonomia no dia a dia", "Habilidades sociais e cognitivas", "Independência e confiança", "Questões sensoriais (sons, texturas, movimento)"],
    passos=[("Plano adaptado", "Plano adaptado a cada paciente."), ("Atividades práticas", "Atividades práticas e divertidas, na sala de TO."), ("Ambiente seguro", "Ambiente seguro e acolhedor, com estrutura de escalada, balanços e piscina de bolinhas."), ("Sessões de 50 minutos", "Atendimento individual.")],
    foto=("espaco-sala-ampla.jpg", "Sala de Terapia Ocupacional e Psicomotricidade da Clínica Bambolê"),
    equipe=["Formação em Integração Sensorial de Ayres", "Foco em autonomia e habilidades do dia a dia"]),
 "psicomotricidade": dict(
    intro0="Trabalha a relação entre corpo, movimento, emoção e cognição, desenvolvendo coordenação, equilíbrio e organização por meio do brincar.",
    para_quem=["Atraso no desenvolvimento motor", "TEA, TDAH e outras condições", "Coordenação e equilíbrio", "Atenção e organização"],
    passos=[("Avaliação psicomotora", "Observação do movimento e do brincar."), ("Movimento e brincadeira", "Atividades com movimento e brincadeira, na sala de psicomotricidade."), ("Orientação à família e à escola", "Como estimular no dia a dia."), ("Sessões de 50 minutos", "Atendimento individual.")],
    foto=("espaco-estrutura.jpg", "Estrutura de movimento com balanços da sala de psicomotricidade da Clínica Bambolê"),
    equipe=["Psicomotricista com formação internacional", "Formação em Psicomotricidade Relacional", "Experiência com crianças, grupos e adultos"]),
 "psicopedagogia": dict(
    intro0="Avaliação e intervenção nos processos de aprendizagem: entende como a pessoa aprende e o que dificulta esse caminho, em parceria com a família e a escola.",
    para_quem=["Alfabetização", "Transtornos e dificuldades de aprendizagem", "Leitura, escrita e matemática", "Rendimento, organização e motivação nos estudos"],
    passos=[("Avaliação psicopedagógica", "Entendimento de como o estudante aprende."), ("Estratégias individualizadas", "Intervenção para as dificuldades encontradas."), ("Parceria com família e escola", "Troca com professores e orientação à família."), ("Sessões de 50 minutos", "Atendimento individual.")],
    foto=("espaco-mesinha.jpg", "Espaço de atividades com mesinha e materiais na Clínica Bambolê"),
    equipe=["Avaliação e intervenção nos processos de aprendizagem", "Leitura, escrita, matemática e organização dos estudos", "Parceria com a família e a escola"]),
 "fisioterapia": dict(
    intro0="Fisioterapia neonatal e neurofuncional da criança e do adolescente, associada à psicomotricidade, para estimular o desenvolvimento motor com mais força, equilíbrio e autonomia.",
    para_quem=["Recém-nascidos e bebês", "Crianças e adolescentes", "Atraso no desenvolvimento motor", "Condições neurológicas e do desenvolvimento"],
    passos=[("Avaliação neurofuncional", "Observação do desenvolvimento motor."), ("Exercícios integrados", "Exercícios integrados à psicomotricidade."), ("Orientação à família e à escola", "Como estimular em casa."), ("Sessões de 50 minutos", "Atendimento individual.")],
    foto=("espaco-psicomotricidade.jpg", "Bancos coloridos, túnel e parede de escalada na Clínica Bambolê"),
    equipe=["Atendimento neonatal", "Neurofuncional da criança e do adolescente", "Associada à psicomotricidade"]),
 "oficinas-sociais": dict(
    intro0="Oficinas em grupo, interativas, que desenvolvem habilidades sociais em um ambiente colaborativo e divertido.",
    para_quem=["Habilidades sociais", "Comunicação e cooperação", "Trabalho em equipe", "Empatia e responsabilidade", "Criatividade"],
    passos=[("Atividades lúdicas em grupo", "Com mediação profissional."), ("Jogos, arte, música e dança", "Formas variadas de praticar a convivência."), ("Participação ativa dos pais", "A família participa do processo."), ("Sessões de 50 minutos", "Atendimento individual.")],
    foto=("espaco-mesa.jpg", "Mesa infantil e cavalete de pintura na Clínica Bambolê"),
    equipe=["Atividades lúdicas em grupo", "Jogos, arte, música e dança", "Participação ativa dos pais"]),
 "musicoterapia": dict(
    intro0="A música como ferramenta terapêutica para crianças, adolescentes e adultos, promovendo comunicação, interação, aprendizagem e expressão emocional.",
    para_quem=["Comunicação e interação", "Aprendizagem", "Expressão emocional", "Desenvolvimento social"],
    passos=[("Percussão", "Tambor, pandeiro e caxixi."), ("Sopro e teclas", "Flauta e xilofone."), ("Individual ou em grupo", "Atividades individuais ou em grupo."), ("Sessões de 50 minutos", "Atendimento individual.")],
    foto=("espaco-sala-to.jpg", "Sala da Clínica Bambolê com balanços e puffs"),
    equipe=["A música como ferramenta terapêutica", "Comunicação, interação e expressão emocional", "Atendimentos individuais e em grupo"]),
 "orientacao-parental": dict(
    intro0="Treinamento para pais e responsáveis que fortalece o vínculo familiar e apoia o desenvolvimento emocional e social da criança.",
    para_quem=["Entender os comportamentos da criança", "Criar um ambiente favorável em casa", "Ensinar habilidades sociais", "Participar da terapia do filho"],
    passos=[("Treinamento colaborativo", "Treinamento colaborativo com os pais."), ("Habilidades sociais", "Educação em habilidades sociais."), ("Suporte emocional", "Suporte emocional à família."), ("Sessões de 50 minutos", "Atendimento individual.")],
    foto=("espaco-recepcao.jpg", "Sala de conversa com poltronas na Clínica Bambolê"),
    equipe=["Psicólogas com orientação a pais e aplicadores", "Estratégias práticas para casa", "Integração com as terapias da criança"]),
}
for _s in SERVICOS:
    _c = _CAT.get(_s["slug"], {})
    if "intro0" in _c: _s["intro"][0] = _c["intro0"]
    for _k in ("para_quem", "passos", "foto", "equipe"):
        if _k in _c: _s[_k] = _c[_k]

ESPACO = [("Salas climatizadas e silenciosas", "Pensadas para quem tem sensibilidade sensorial."),
          ("Uma sala para cada tipo de atendimento", "Ambientes neutros, organizados e acolhedores."),
          ("Acervo escolhido pela neuropsicologia", "Nenhum brinquedo está na prateleira por acaso."),
          ("Banheiro acessível", "Pensado para estimular a independência."),
          ("Sala de TO e Psicomotricidade", "Espaço amplo, com estrutura de escalada, balanços e piscina de bolinhas.")]
CURRICULO = ["Neuropsicóloga", "Formação em ABA", "Especialista em Autismo (TEA)", "Terapia Cognitivo-Comportamental (TCC)", "Reabilitação do TDAH", "Comunicação Aumentativa e Alternativa (CAA)", "Psicoterapia Humanista"]

# Marcações de anúncios e análise (as mesmas do site antigo)
TRACK = {"gtm": "GTM-W7TLFHJ5", "ga4": "G-DZL95R1LLP", "ads": "AW-16869774533",
         "ads_conv": "AW-16869774533/w7o4COLf-JwaEMWpkew-", "meta": "3393514717496749"}
