#!/usr/bin/env python3
"""Gera o site estático FSA⁴Future V1 em ./fsa4future/.

Uso:
  python3 tools/build_fsa4future.py            # homologação (noindex em todas as páginas)
  python3 tools/build_fsa4future.py --prod     # produção em https://fsa4future.com.br (indexável)

Fonte do conteúdo: Handoff v1.3, FSiA_Base_de_Conhecimento_v1, Design System v1.1
(ui_kits/website). Links internos são relativos, então a mesma saída funciona em
subpasta (homologação) e na raiz do domínio (produção).
"""
import datetime
import html
import json
import os
import sys

PROD = '--prod' in sys.argv
BASE = 'https://fsa4future.com.br/'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fsa4future')
YEAR = datetime.date.today().year
UPDATED = datetime.date.today().isoformat()
E = html.escape

NAME = 'FSA⁴Future'
NAME_HTML = 'FSA<sup>4</sup>Future'
DESC = 'Technology &amp; Business Hub'
SIGN = 'Technology 4 what’s next.'
CAMPAIGN = 'Ideias em movimento. Impacto no futuro.'
LEGAL = 'FSA IT4FUTURE HUB TECNOLOGIA LTDA'
CNPJ = '69.447.199/0001-05'
EMAIL = 'atendimento@fsa4future.com.br'
CTA = 'Quero conversar sobre meu desafio'

FRONTS = [
    dict(key='flow', slug='fsa-4-flow', name='FSA⁴Flow', icon='workflow',
         tag='Entender antes de transformar.',
         desc='Diagnóstico, processos, eficiência, automação, integrações, produtividade e transformação.',
         intent='Automação e otimização de processos',
         specs=['Automação de processos', 'Análise e otimização de processos', 'Integração entre sistemas', 'Redução de trabalho manual'],
         when=['Processos lentos, com retrabalho ou dependentes de planilhas.', 'Equipes redigitando os mesmos dados em sistemas que não conversam.', 'Você sente o problema, mas ainda não sabe exatamente onde ele está.']),
    dict(key='partners', slug='fsa-4-partners', name='FSA⁴Partners', icon='handshake',
         tag='A solução certa nem sempre precisa vir de dentro.',
         desc='Ecossistema de parceiros e competências complementares.',
         intent='Ecossistema de parceiros de tecnologia',
         specs=['Parceiros de tecnologia', 'Competências complementares', 'Soluções de mercado integradas'],
         when=['A melhor resposta já existe no mercado e precisa ser escolhida e integrada.', 'O desafio pede uma competência complementar à da FSA.', 'Sua empresa atende outras empresas e quer indicar quem precisa de tecnologia.']),
    dict(key='solutions', slug='fsa-4-solutions', name='FSA⁴Solutions', icon='blocks',
         tag='Do problema à tecnologia funcionando.',
         desc='APIs, bots, IA, integrações, dados, automação, desenvolvimento, modernização e soluções sob medida.',
         intent='Desenvolvimento de software sob medida, IA aplicada e modernização',
         specs=['Desenvolvimento de software sob medida', 'Modernização de sistemas legados', 'IA aplicada a processos e negócios', 'APIs e integrações'],
         when=['O negócio precisa de um sistema, app, API ou integração que não existe pronto.', 'Um sistema legado segura a operação e a decisão é modernizar, integrar ou substituir.', 'Você quer avaliar se IA é a resposta certa para um problema real.']),
    dict(key='products', slug='fsa-4-products', name='FSA⁴Products', icon='lightbulb',
         tag='Ideias que podem se transformar em novos produtos.',
         desc='Produtos próprios, experimentação, propriedade intelectual e novas soluções desenvolvidas pelo hub.',
         intent='Produtos digitais e experimentação',
         specs=['Produtos próprios', 'Experimentação', 'Novas soluções do hub'],
         when=['Existe uma ideia de produto digital que precisa ser testada antes de crescer.', 'Um problema recorrente do mercado pode virar solução própria.', 'Você quer experimentar com segurança antes de investir em escala.']),
]
FRONT = {f['key']: f for f in FRONTS}

STEPS = [
    dict(slug='ouvir', name='Ouvir', title='Antes de propor, a gente ouve.',
         lead='Todo desafio chega com uma história: pessoas, processos, sistemas, restrições, objetivos e questões que nem sempre aparecem no briefing.',
         body='Ouvir quem conhece o negócio, vive o processo e utilizará a solução é o início de uma resposta que faça sentido.',
         who='Quem decide, quem opera e quem vai usar a solução.', out='Contexto registrado e validado com você.'),
    dict(slug='entender', name='Entender', title='O problema que chega nem sempre é o problema que precisa ser resolvido.',
         lead='Transformar contexto em entendimento.',
         body='Investigar processos, dados, sistemas, dependências, impactos e oportunidades para chegar ao que realmente precisa ser resolvido.',
         who='O time da FSA e as pessoas que conhecem o processo por dentro.', out='Um entendimento comum do problema, das dependências e das oportunidades.'),
    dict(slug='conectar', name='Conectar', title='Nem sempre precisamos construir tudo do zero.',
         lead='Conectar tecnologias, sistemas, dados, pessoas, competências e parceiros.',
         body='Se a melhor resposta já existe, encontrar. Se precisa ser integrada, conectar. Se não existe, construir.',
         who='O time da FSA, parceiros do hub quando fizer sentido, e você nas decisões.', out='O caminho escolhido junto: encontrar, conectar ou construir.'),
    dict(slug='construir', name='Construir', title='Do entendimento à solução funcionando.',
         lead='Transformar entendimento e decisões em solução funcional.',
         body='Você acompanha, participa e decide junto durante a construção.',
         who='O time de construção da FSA, com você acompanhando.', out='Solução funcional, construída com quem vai usá-la.'),
    dict(slug='validar', name='Validar', title='Testar em contexto real.',
         lead='Testar, medir e ajustar em contexto real.',
         body='A validação acontece junto com quem opera e utiliza a solução, no dia a dia do negócio.',
         who='Quem opera e utiliza a solução, com o time da FSA.', out='Ajustes feitos a partir do uso real.'),
    dict(slug='evoluir', name='Evoluir', title='A tecnologia muda. A solução acompanha.',
         lead='Acompanhar, melhorar, ampliar e identificar novas possibilidades.',
         body='O negócio e a tecnologia mudam. A solução acompanha essas mudanças, e novas possibilidades aparecem pelo caminho.',
         who='Você e o time da FSA, ao longo do tempo.', out='Melhorias e novas possibilidades conforme o negócio muda.'),
]

CHALLENGES = [
    ('Sistemas que não conversam entre si.', 'Quando a equipe redigita os mesmos dados em lugares diferentes, o problema raramente é a pessoa. É a conexão que falta.', 'flow', 'Integração de sistemas'),
    ('Trabalho manual que ninguém aguenta mais.', 'Planilhas, conferências e repasses que consomem o dia e geram retrabalho. Nem sempre a resposta é um sistema novo.', 'flow', 'Automação de processos'),
    ('Um sistema legado que segura o negócio.', 'Modernizar, integrar ou substituir? A decisão depende do que o sistema sustenta hoje e do que o negócio precisa amanhã.', 'solutions', 'Modernização de sistemas legados'),
    ('IA: usar ou não usar?', 'Nem todo problema se resolve com IA. Antes da ferramenta vem a pergunta certa: qual problema precisa ser resolvido?', 'solutions', 'IA aplicada a processos e negócios'),
    ('Um processo que ninguém consegue explicar.', 'Quando o problema ainda não está claro, o primeiro passo é ouvir e entender, não escolher tecnologia.', 'flow', 'Análise e otimização de processos'),
    ('Dados espalhados, decisões no escuro.', 'Informação existe, mas está em lugares diferentes e não ajuda a decidir. Organizar e conectar dados é parte do caminho.', 'solutions', 'Dados e integrações'),
    ('Uma ideia que pode virar produto.', 'Testar antes de escalar: experimentar com segurança e transformar um problema recorrente em solução.', 'products', 'Produtos digitais'),
    ('A solução certa já existe no mercado.', 'Às vezes o melhor caminho é escolher bem, integrar e fazer funcionar, com parceiros do hub.', 'partners', 'Soluções de mercado integradas'),
]

CAPS = ['IA', 'Automação', 'Dados', 'Cloud', 'Desenvolvimento', 'APIs', 'Integrações', 'Modernização', 'Segurança', 'Produtos', 'Estratégia']

QUESTIONS = [
    'IA ou automação tradicional: como decidir?',
    'Quando não usar inteligência artificial em um projeto?',
    'Como identificar processos que deveriam ser automatizados?',
    'Quando integrar é melhor do que substituir um sistema legado?',
    'Como reduzir trabalho manual entre sistemas que não conversam?',
    'Como avaliar se um processo está pronto para automação?',
    'Modernizar ou substituir um sistema legado?',
    'Como começar um projeto de IA sem começar pela ferramenta?',
]

NAV = [('desafios/', 'Desafios'), ('como-fazemos/', 'Como fazemos'), ('hub/', 'Hub'), ('cases/', 'Cases'), ('sobre/', 'Sobre'), ('conteudos/', 'Conteúdos')]


def ic(name, size=None, cls=''):
    s = f' f4-icon--{size}' if size else ''
    return f'<svg class="f4-icon{s}{(" " + cls) if cls else ""}" aria-hidden="true"><use href="{{R}}assets/icons/sprite.svg#i-{name}"></use></svg>'


def btn(label, href, variant='accent', size='', arrow=True, track=None, extra=''):
    cls = f'f4-btn f4-btn--{variant}' + (f' f4-btn--{size}' if size else '')
    t = f' data-track="{track}"' if track else ''
    a = ' <svg class="f4-icon f4-btn__arrow" aria-hidden="true"><use href="{R}assets/icons/sprite.svg#i-arrow-right"></use></svg>' if arrow else ''
    return f'<a class="{cls}" href="{href}"{t}{extra}>{label}{a}</a>'


def cta_main(size='lg'):
    return btn(CTA, '{R}conversar/', 'accent', size, track='cta_principal')


def eyebrow(text, inverse=False):
    return f'<span class="f4-eyebrow{" f4-eyebrow--inverse" if inverse else ""}"><span class="f4-eyebrow__rule" aria-hidden="true"></span>{text}</span>'


def photo(label, tall=False):
    return f'<div class="photo{" photo--tall" if tall else ""}" role="img" aria-label="Espaço reservado para foto: {E(label)}"><span>{ic("image", 16)}Foto temporária: {E(label)}</span></div>'


def crumbs(items, inverse=False):
    li = []
    for i, (label, href) in enumerate(items):
        if i == len(items) - 1:
            li.append(f'<li aria-current="page">{label}</li>')
        else:
            li.append(f'<li><a href="{href}">{label}</a></li><li aria-hidden="true">/</li>')
    return f'<nav aria-label="Trilha de navegação"><ol class="f4-crumbs{" f4-crumbs--inverse" if inverse else ""}">{"".join(li)}</ol></nav>'


def hub_card(f, level='h3'):
    return f'''<a class="f4-card f4-card--link f4-hub front-{f["key"]}" href="{{R}}hub/{f["slug"]}/" data-track="clique_hub" data-track-label="{f["name"]}">
<span class="f4-card__accent" aria-hidden="true"></span>
<span class="f4-hub__icon">{ic(f["icon"], 24)}</span>
<{level} class="f4-hub__name">{f["name"]}</{level}>
<p class="f4-hub__tag">{f["tag"]}</p>
<span class="f4-hub__more">Conhecer a frente {ic("arrow-right", 16)}</span>
</a>'''


def cta_final(title='Qual desafio precisamos resolver juntos?'):
    return f'''<section class="section--md" aria-labelledby="cta-final">
<div class="container grid-split" style="align-items:end">
<div class="stack-sm"><h2 class="h2" id="cta-final">{title}</h2><p class="lead">Conte um pouco sobre o seu desafio. <strong class="strong">Não precisa saber qual tecnologia usar. Essa parte a gente descobre junto.</strong></p></div>
<div>{cta_main()}</div>
</div></section>'''


# ---------------------------------------------------------------- páginas
PAGES = []


def page(path, title, description, h1, body, *, crumb=None, schema_extra=None, noindex=False, data=None, intent=None, priority='0.7', og_type='website'):
    PAGES.append(dict(path=path, title=title, description=description, h1=h1, body=body, crumb=crumb or [],
                      schema_extra=schema_extra or [], noindex=noindex, data=data or {}, intent=intent or {}, priority=priority, og_type=og_type))


# Home --------------------------------------------------------------
method_btns = ''.join(
    f'<button type="button" role="tab" class="f4-step{" f4-step--active" if i == 0 else ""}" id="mt-{s["slug"]}" aria-controls="mp-{s["slug"]}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}"><span class="f4-step__num">0{i+1}</span><span class="f4-step__label">{s["name"]}</span></button>'
    for i, s in enumerate(STEPS))
method_panels = ''.join(
    f'<div class="grid-2 mt-48" role="tabpanel" id="mp-{s["slug"]}" aria-labelledby="mt-{s["slug"]}" data-step-panel{"" if i == 0 else " hidden"}><h3 class="h3">{s["title"]}</h3><div class="stack" style="justify-items:start"><p class="lead">{s["lead"]}</p>{btn("Ver a etapa completa", "{R}como-fazemos/" + s["slug"] + "/", "secondary")}</div></div>'
    for i, s in enumerate(STEPS))

home = f'''
<section class="section" style="padding-top:112px" aria-labelledby="h1">
<div class="container grid-hero">
<div class="stack" style="gap:28px">
{eyebrow(NAME + ' · ' + DESC)}
<h1 class="h1" id="h1">Seu desafio não precisa caber em uma solução pronta.</h1>
<p class="lead strong brand">Você traz o desafio. A gente encontra, conecta ou constrói a tecnologia para resolvê-lo.</p>
<p>IA, automação, dados, cloud, integrações, desenvolvimento e um ecossistema de tecnologia para construir o que faz sentido para o seu negócio, hoje e para o que vem depois.</p>
<div class="row">{cta_main()}{btn("Explorar possibilidades", "{R}hub/", "ghost", track="cta_exploratorio")}</div>
<p class="proof"><span>+20 anos de experiência</span><span aria-hidden="true">·</span><span>NPS 70</span><span aria-hidden="true">·</span><span>Tecnologia construída junto</span></p>
</div>
{photo("cliente e time FSA em workshop", tall=True)}
</div></section>

<section class="section bg-petrol" style="padding:120px 0" aria-labelledby="h-ia">
<div class="container grid-split" style="align-items:end">
<h2 class="h2" id="h-ia">Nem todo problema se resolve com IA. <span class="inv-accent">Mas todo problema precisa ser resolvido.</span></h2>
<div class="stack-sm"><p class="lead strong inv">Não começamos pela tecnologia da vez. Começamos pelo que o seu negócio precisa.</p><p class="inv-muted">Às vezes a resposta é IA. Às vezes é automação, integração, dados, cloud ou desenvolvimento full-code. Muitas vezes, é uma combinação de diferentes capacidades.</p></div>
</div></section>

<section class="section" aria-labelledby="h-metodo">
<div class="container" id="method-home">
<div class="stack-sm mb-48">{eyebrow("Como fazemos")}<h2 class="h2" id="h-metodo">Tecnologia construída junto.</h2></div>
<div class="f4-steps" role="tablist" aria-label="Etapas do método">{method_btns}</div>
{method_panels}
</div></section>

<section class="section bg-sand100" aria-labelledby="h-hub">
<div class="container">
<div class="stack-sm mb-48">{eyebrow("Hub")}<h2 class="h2" id="h-hub">Um hub. Diferentes caminhos para resolver.</h2></div>
<div class="grid-4">{"".join(hub_card(f) for f in FRONTS)}</div>
</div></section>

<section class="section" aria-labelledby="h-cap">
<div class="container grid-2 cols-1-12">
<h2 class="h2" id="h-cap">A tecnologia muda. Nossa capacidade de construir também.</h2>
<div class="stack"><ul class="chips" role="list" style="list-style:none;margin:0;padding:0">{"".join(f'<li class="f4-chip f4-chip--static">{c}</li>' for c in CAPS)}</ul><p class="lead strong brand">Não precisamos escolher uma dessas caixas. Podemos conectá-las.</p></div>
</div></section>

<section class="section bg-sand300" style="padding:112px 0" aria-labelledby="h-prova">
<div class="container grid-3 cols-proof">
<h2 class="h3" id="h-prova" style="font-size:40px;line-height:48px">Mais de duas décadas resolvendo problemas que não vêm com manual.</h2>
<div class="stat"><div class="stat__n">+20</div><p class="small" style="color:var(--graphite-700)">anos de experiência em tecnologia e consultoria</p></div>
<div class="stat"><div class="stat__n">NPS 70</div><p class="small" style="color:var(--graphite-700)">Net Promoter Score · atuação em múltiplos setores</p></div>
</div></section>

<section class="section" aria-labelledby="h-prox">
<div class="container grid-2" style="align-items:center">
{photo("equipe mista validando protótipo")}
<div class="stack"><h2 class="h2" id="h-prox">Tecnologia se constrói com quem vai usá-la.</h2><p class="lead">Você conhece seu negócio. Nós trazemos experiência, tecnologia, engenharia e um ecossistema de possibilidades.</p><p class="strong">As melhores decisões acontecem quando esses conhecimentos trabalham juntos.</p><span class="label-up" style="color:var(--copper-700)">Nada sobre o cliente sem o cliente.</span></div>
</div></section>

<section class="section--md bg-sand100" aria-labelledby="h-futuro">
<div class="container grid-2" style="align-items:start">
<h2 class="h2" id="h-futuro">O futuro que queremos construir também importa.</h2>
<div class="stack"><p class="lead">Evoluir sempre, com responsabilidade: pessoas, inclusão, acessibilidade, sustentabilidade, parcerias e governança fazem parte de como a gente trabalha.</p><p class="muted">{CAMPAIGN}</p></div>
</div></section>

<section class="section bg-petrol950" aria-label="Manifesto">
<div class="container"><div class="maxw-820 stack">
{eyebrow("Manifesto", True)}
<h2 class="h2" id="h-manifesto">Seu desafio não precisa caber em uma solução pronta.</h2>
<p class="lead inv-muted">Há mais de 20 anos, a FSA escuta, entende e constrói tecnologia junto com seus clientes. Às vezes a resposta é IA. Às vezes é automação, integração, dados, cloud ou desenvolvimento full-code. E, muitas vezes, é uma combinação de tudo isso.</p>
<p class="lead inv-muted">Não estamos aqui para empurrar a tecnologia da vez. Estamos aqui para encontrar o que faz sentido para o seu negócio, inclusive quando o problema ainda não está claro.</p>
<p class="lead inv-muted">Porque acreditamos em tecnologia próxima, construída com quem conhece o negócio de verdade. Você participa, questiona, valida e evolui junto com a gente.</p>
<p class="lead strong inv">Você traz o desafio. A gente encontra, conecta ou constrói a tecnologia para resolvê-lo.</p>
<p style="font-weight:700;font-size:18px" class="inv">{NAME_HTML}. <span class="inv-accent" style="font-weight:500">{SIGN}</span></p>
</div></div></section>
{cta_final()}
'''
page('', f'{NAME} · {DESC.replace("&amp;", "&")} · Tecnologia construída junto',
     'Technology & Business Hub com mais de 20 anos em consultoria e tecnologia. IA, automação, dados, integrações e desenvolvimento escolhidos pelo seu desafio.',
     'Seu desafio não precisa caber em uma solução pronta.', home, priority='1.0',
     intent=dict(finalidade='Apresentar a nova marca e levar à conversa', persona='Decisor com um desafio de negócio e tecnologia', tema='FSA⁴Future, Technology & Business Hub', cta=CTA))

# Desafios ----------------------------------------------------------
ch_cards = ''.join(f'''<article class="f4-card front-{fk}"><span class="f4-card__accent" aria-hidden="true"></span>
<span class="f4-badge f4-badge--{fk}"><span class="f4-badge__dot" aria-hidden="true"></span>{FRONT[fk]["name"]}</span>
<h2 class="h4">{t}</h2><p>{d}</p>
<a class="card-link front-label" href="{{R}}hub/{FRONT[fk]["slug"]}/">{spec} em {FRONT[fk]["name"]} {ic("arrow-right", 16)}</a></article>''' for t, d, fk, spec in CHALLENGES)
desafios = f'''
<section class="section--md" aria-labelledby="h1">
<div class="container stack">
{crumbs([("Home", "{R}"), ("Desafios", "")])}
<div class="grid-split"><div class="stack">{eyebrow("Desafios")}<h1 class="h1" id="h1">Cada negócio tem um desafio. Cada desafio pede seu próprio caminho.</h1></div>
<p class="lead" style="align-self:end">Estes são alguns dos desafios que chegam até a FSA. O seu pode ser parecido, diferente ou ainda não estar claro. Em qualquer caso, a conversa começa pelo que o seu negócio precisa.</p></div>
</div></section>
<section class="section--md bg-sand100" aria-label="Desafios frequentes"><div class="container grid-2" style="gap:24px">{ch_cards}</div></section>
<section class="section--md" aria-labelledby="h-perg"><div class="container grid-2">
<h2 class="h2" id="h-perg">Perguntas que a gente ajuda a responder.</h2>
<ul class="list-check">{"".join(f'<li>{ic("check", 18)}<span>{q}</span></li>' for q in QUESTIONS)}</ul>
</div></section>
{cta_final()}
'''
page('desafios/', f'Desafios de tecnologia e negócio que a gente resolve junto · {NAME}',
     'Sistemas que não conversam, trabalho manual, legado, IA, dados e novos produtos: veja desafios comuns e como cada um encontra seu caminho no hub.',
     'Cada negócio tem um desafio. Cada desafio pede seu próprio caminho.', desafios, crumb=[('Desafios', 'desafios/')],
     intent=dict(finalidade='Identificação com o problema e roteamento para a frente', persona='Decisor que reconhece um sintoma', tema='Desafios de tecnologia e processos', cta=CTA))

# Como fazemos ------------------------------------------------------
steps_list = ''.join(f'''<a class="f4-card f4-card--link" href="{{R}}como-fazemos/{s["slug"]}/"><span class="label-up" style="color:var(--copper-700)">0{i+1} · {s["name"].upper()}</span><h2 class="h4">{s["title"]}</h2><p>{s["lead"]}</p><span class="card-link">Ver a etapa {ic("arrow-right", 16)}</span></a>''' for i, s in enumerate(STEPS))
como = f'''
<section class="section--md bg-petrol" aria-labelledby="h1"><div class="container stack" style="gap:28px">
{crumbs([("Home", "{R}"), ("Como fazemos", "")], True)}
{eyebrow("Como fazemos", True)}
<h1 class="h1 maxw-900" id="h1">Tecnologia construída junto.</h1>
<p class="lead inv-muted maxw-720">01 Ouvir → 02 Entender → 03 Conectar → 04 Construir → 05 Validar → 06 Evoluir. Essas etapas mostram como a FSA trabalha. Não são seis serviços: são um único caminho, percorrido com você.</p>
</div></section>
<section class="section--md"><div class="container grid-3">{steps_list}</div></section>
{cta_final()}
'''
page('como-fazemos/', f'Como fazemos: o método Ouvir → Evoluir · {NAME}',
     'Ouvir, Entender, Conectar, Construir, Validar e Evoluir: as seis etapas de como a FSA⁴Future constrói tecnologia junto com quem conhece o negócio.',
     'Tecnologia construída junto.', como, crumb=[('Como fazemos', 'como-fazemos/')],
     intent=dict(finalidade='Explicar o método e gerar confiança', persona='Decisor avaliando como a FSA trabalha', tema='Método de trabalho', cta=CTA))

for i, s in enumerate(STEPS):
    steps_nav = ''.join(
        f'<a class="f4-step{" f4-step--active" if j == i else (" f4-step--done" if j < i else "")}" href="{{R}}como-fazemos/{t["slug"]}/"{" aria-current=\"step\"" if j == i else ""}><span class="f4-step__num">0{j+1}</span><span class="f4-step__label">{t["name"]}</span></a>'
        for j, t in enumerate(STEPS))
    prev_l = btn(f'0{i} {STEPS[i-1]["name"]}', '{R}como-fazemos/' + STEPS[i-1]['slug'] + '/', 'ghost', arrow=False, extra=' rel="prev"').replace('">0', '"><svg class="f4-icon" aria-hidden="true"><use href="{R}assets/icons/sprite.svg#i-arrow-left"></use></svg> 0', 1) if i > 0 else '<span></span>'
    next_l = btn(f'0{i+2} {STEPS[i+1]["name"]}', '{R}como-fazemos/' + STEPS[i+1]['slug'] + '/', 'secondary', extra=' rel="next"') if i < 5 else cta_main('')
    body = f'''
<section class="section--md bg-petrol" aria-labelledby="h1"><div class="container stack" style="gap:28px">
{crumbs([("Home", "{R}"), ("Como fazemos", "{R}como-fazemos/"), (s["name"], "")], True)}
{eyebrow(f"Etapa 0{i+1} de 06 · {s['name']}", True)}
<h1 class="h1 maxw-900" id="h1">{s["title"]}</h1>
<p class="lead inv-muted maxw-720">{s["lead"]}</p>
<nav aria-label="Etapas do método" class="mt-24"><div class="f4-steps f4-steps--inverse">{steps_nav}</div></nav>
</div></section>
<section class="section--md" aria-labelledby="h-etapa"><div class="container grid-2 cols-1-14">
{photo(s["name"].lower() + " em contexto real")}
<div class="stack"><h2 class="h3" id="h-etapa">O que acontece nesta etapa.</h2><p class="lead">{s["body"]}</p>
<div class="cards-2"><div class="f4-card f4-card--compact"><h3 class="h4" style="font-size:17px;line-height:24px">Quem participa</h3><p class="small">{s["who"]}</p></div><div class="f4-card f4-card--compact"><h3 class="h4" style="font-size:17px;line-height:24px">O que sai daqui</h3><p class="small">{s["out"]}</p></div></div>
</div></div></section>
<section class="section--sm bg-sand100" aria-label="Navegação entre etapas"><div class="container step-nav">{prev_l}{next_l}</div></section>
{cta_final()}
'''
    page(f'como-fazemos/{s["slug"]}/', f'{s["name"]}: etapa 0{i+1} do método · {NAME}',
         f'Etapa 0{i+1} de 06 do método FSA⁴Future. {s["title"]} {s["lead"]}'[:158],
         s['title'], body, crumb=[('Como fazemos', 'como-fazemos/'), (s['name'], f'como-fazemos/{s["slug"]}/')], priority='0.6',
         intent=dict(finalidade=f'Detalhar a etapa {s["name"]}', persona='Decisor avaliando o método', tema=f'Etapa {s["name"]}', cta='Próxima etapa / ' + CTA))

# Hub ---------------------------------------------------------------
def hub_tabs(active):
    return '<nav aria-label="Frentes do hub"><div class="f4-tabs">' + ''.join(
        f'<a class="f4-tab{" f4-tab--active" if f["key"] == active else ""}" href="{{R}}hub/{f["slug"]}/"{" aria-current=\"page\"" if f["key"] == active else ""}>{f["name"]}</a>' for f in FRONTS) + '</div></nav>'


hub = f'''
<section class="section--md" aria-labelledby="h1"><div class="container stack">
{crumbs([("Home", "{R}"), ("Hub", "")])}
<div class="grid-split"><div class="stack">{eyebrow("Hub")}<h1 class="h1" id="h1">Um hub. Diferentes caminhos para resolver.</h1></div>
<p class="lead" style="align-self:end">Quatro frentes, um mesmo ponto de partida: o seu desafio. IA, cloud, dados, desenvolvimento, automação, integrações e segurança são capacidades que atravessam todas elas.</p></div>
</div></section>
<section class="section--md bg-sand100" aria-label="Frentes do hub"><div class="container grid-4">{"".join(hub_card(f, "h2") for f in FRONTS)}</div></section>
<section class="section--md" aria-labelledby="h-conn"><div class="container grid-2" style="align-items:center">
<h2 class="h3" id="h-conn">Nem sempre precisamos construir tudo do zero.</h2>
<p class="lead">Se a melhor resposta já existe, encontramos. Se precisa ser integrada, conectamos. Se não existe, construímos.</p>
</div></section>
{cta_final()}
'''
page('hub/', f'Hub: Flow, Partners, Solutions e Products · {NAME}',
     'As quatro frentes do hub FSA⁴Future: processos e automação, parceiros, desenvolvimento e IA, e produtos. Um mesmo ponto de partida: o seu desafio.',
     'Um hub. Diferentes caminhos para resolver.', hub, crumb=[('Hub', 'hub/')], priority='0.8',
     intent=dict(finalidade='Apresentar a arquitetura de marca e rotear para as frentes', persona='Decisor explorando possibilidades', tema='Frentes do hub', cta=CTA))

for f in FRONTS:
    extra = ''
    if f['key'] == 'partners':
        extra = f'''<section class="section--md front-partners" aria-labelledby="h-prog"><div class="container"><div class="f4-card front-bar" style="padding:40px"><div class="grid-split" style="align-items:center">
<div class="stack-sm"><span class="label-up front-label">Programa de Parceiros</span><h2 class="h3" id="h-prog">Indique quem precisa de tecnologia. A gente constrói, você participa do resultado.</h2><p>Para empresas com CNPJ ativo que atendem outras empresas: agências, contabilidades, consultorias, integradores, mentores e assessorias.</p></div>
<div>{btn("Conhecer o Programa de Parceiros", "{R}hub/fsa-4-partners/programa/", "secondary")}</div></div></div></div></section>'''
    body = f'''
<section class="section--sm" style="border-bottom:1px solid var(--border-subtle)"><div class="container stack">
{crumbs([("Home", "{R}"), ("Hub", "{R}hub/"), (f["name"], "")])}
{hub_tabs(f["key"])}
</div></section>
<section class="section--md front-{f["key"]} front-bar" aria-labelledby="h1"><div class="container grid-split">
<div class="stack">
<span class="f4-badge f4-badge--{f["key"]}"><span class="f4-badge__dot" aria-hidden="true"></span>{f["name"]}</span>
<h1 class="h1" id="h1">{f["tag"]}</h1>
<p class="lead">{f["desc"]}</p>
<div>{cta_main("")}</div>
</div>
<div class="stack-sm"><h2 class="label-up front-label">Especialidades</h2>
<ul class="stack-sm" style="list-style:none;margin:0;padding:0">{"".join(f'<li class="f4-card f4-card--compact" style="flex-direction:row;align-items:center;justify-content:space-between"><span class="strong" style="font-size:17px">{sp}</span>{ic("check", 18, "front-label")}</li>' for sp in f["specs"])}</ul>
</div></div></section>
<section class="section--md bg-sand100" aria-labelledby="h-quando"><div class="container grid-2">
<h2 class="h3" id="h-quando">Quando {f["name"]} costuma fazer sentido.</h2>
<ul class="list-check">{"".join(f'<li>{ic("check", 18)}<span>{w}</span></li>' for w in f["when"])}</ul>
</div></section>
{extra}
<section class="section--md" aria-labelledby="h-conn"><div class="container grid-2" style="align-items:center">
<h2 class="h3" id="h-conn">Nem sempre precisamos construir tudo do zero.</h2>
<p class="lead">Se a melhor resposta já existe, encontramos. Se precisa ser integrada, conectamos. Se não existe, construímos. A escolha da tecnologia depende do problema.</p>
</div></section>
{cta_final()}
'''
    page(f'hub/{f["slug"]}/', f'{f["name"]}: {f["intent"]} · {NAME}',
         f'{f["name"]}. {f["tag"]} {f["desc"]}'[:158], f['tag'], body,
         crumb=[('Hub', 'hub/'), (f['name'], f'hub/{f["slug"]}/')], data={'hub': f['key']}, priority='0.8',
         schema_extra=[{'@type': 'Service', 'name': f['name'], 'serviceType': f['intent'], 'description': f['desc'], 'provider': {'@id': BASE + '#organization'}, 'areaServed': 'BR', 'url': BASE + f'hub/{f["slug"]}/'}],
         intent=dict(finalidade=f'Converter interesse em {f["intent"].lower()}', persona='Decisor com desafio relacionado à frente', tema=f['intent'], cta=CTA))

prog = f'''
<section class="section--sm" style="border-bottom:1px solid var(--border-subtle)"><div class="container stack">
{crumbs([("Home", "{R}"), ("Hub", "{R}hub/"), ("FSA⁴Partners", "{R}hub/fsa-4-partners/"), ("Programa de Parceiros", "")])}
</div></section>
<section class="section--md front-partners front-bar" aria-labelledby="h1"><div class="container grid-split">
<div class="stack">{eyebrow("FSA⁴Partners · Programa de Parceiros")}<h1 class="h1" id="h1">Indique quem precisa de tecnologia. A gente constrói, você participa do resultado.</h1>
<p class="lead">Um programa para empresas que atendem outras empresas e conhecem de perto os desafios dos seus clientes.</p>
<div class="row">{btn("Quero ser parceiro", "mailto:" + EMAIL + "?subject=" + "Programa%20de%20Parceiros", "accent", "", track="cta_parceiro")}</div></div>
<div class="f4-card f4-card--sand stack-sm"><h2 class="h4">Quem pode ser parceiro</h2><p>Empresas com CNPJ ativo que atendem outras empresas: agências, contabilidades, consultorias, integradores, mentores e assessorias.</p></div>
</div></section>
<section class="section--md bg-sand100" aria-labelledby="h-como"><div class="container stack-lg">
<h2 class="h2" id="h-como">Como funciona.</h2>
<ol class="grid-3" style="list-style:none;margin:0;padding:0">
<li class="f4-card stack-sm"><span class="label-up front-label front-partners">01</span><p class="strong">Você indica uma empresa com um desafio real.</p></li>
<li class="f4-card stack-sm"><span class="label-up front-label front-partners">02</span><p class="strong">A FSA conduz a conversa, o escopo e a proposta.</p></li>
<li class="f4-card stack-sm"><span class="label-up front-label front-partners">03</span><p class="strong">Com o contrato fechado e pago, você recebe comissão sobre o valor líquido recebido.</p></li>
</ol></div></section>
<section class="section--md" aria-labelledby="h-regras"><div class="container grid-2">
<h2 class="h3" id="h-regras">Regras em resumo.</h2>
<ul class="list-check">
<li>{ic("check", 18)}<span>A indicação fica protegida por um prazo definido.</span></li>
<li>{ic("check", 18)}<span>Se outro parceiro já indicou o mesmo cliente, a indicação vai para uma lista de espera.</span></li>
<li>{ic("check", 18)}<span>O percentual é definido na contratação de cada cliente e aparece no contrato de adesão.</span></li>
<li>{ic("check", 18)}<span>Sem vínculo, sem exclusividade, sem meta.</span></li>
<li>{ic("check", 18)}<span>O parceiro não negocia preço. Escopo, prazo e proposta são da FSA.</span></li>
</ul></div></section>
<section class="section--sm bg-sand100"><div class="container row" style="justify-content:space-between"><p class="small muted">Já é parceiro? A área do parceiro está em preparação.</p>{btn("Quero ser parceiro", "mailto:" + EMAIL + "?subject=" + "Programa%20de%20Parceiros", "secondary", "sm", track="cta_parceiro")}</div></section>
'''
page('hub/fsa-4-partners/programa/', f'Programa de Parceiros FSA⁴Partners: indique e participe do resultado · {NAME}',
     'Empresas com CNPJ que atendem outras empresas podem indicar quem precisa de tecnologia. A FSA conduz a conversa, o escopo e a proposta.',
     'Indique quem precisa de tecnologia. A gente constrói, você participa do resultado.', prog,
     crumb=[('Hub', 'hub/'), ('FSA⁴Partners', 'hub/fsa-4-partners/'), ('Programa de Parceiros', 'hub/fsa-4-partners/programa/')], data={'hub': 'partners-programa'}, priority='0.6',
     intent=dict(finalidade='Atrair parceiros indicadores', persona='Agências, contabilidades, consultorias, integradores', tema='Programa de parceiros de tecnologia', cta='Quero ser parceiro'))

# Cases --------------------------------------------------------------
cases = f'''
<section class="section--md" aria-labelledby="h1"><div class="container stack">
{crumbs([("Home", "{R}"), ("Cases", "")])}
<div class="grid-split"><div class="stack">{eyebrow("Cases")}<h1 class="h1" id="h1">Mais de duas décadas resolvendo problemas que não vêm com manual.</h1></div>
<p class="lead" style="align-self:end">Os cases da FSA estão em autorização com os clientes. Cada um será publicado com a história completa e com resultados comprováveis, sem números inventados.</p></div>
</div></section>
<section class="section--md bg-sand100" aria-labelledby="h-formato"><div class="container stack-lg">
<h2 class="h3" id="h-formato">Como cada case será contado.</h2>
<ol class="grid-4" style="list-style:none;margin:0;padding:0">
<li class="f4-card stack-sm"><span class="label-up" style="color:var(--copper-700)">01</span><p class="strong">Desafio</p><p class="small">O contexto e o que precisava ser resolvido.</p></li>
<li class="f4-card stack-sm"><span class="label-up" style="color:var(--copper-700)">02</span><p class="strong">O que encontramos</p><p class="small">O diagnóstico feito junto com o cliente.</p></li>
<li class="f4-card stack-sm"><span class="label-up" style="color:var(--copper-700)">03</span><p class="strong">O que construímos</p><p class="small">As decisões, as tecnologias e a participação do cliente.</p></li>
<li class="f4-card stack-sm"><span class="label-up" style="color:var(--copper-700)">04</span><p class="strong">Impacto</p><p class="small">Resultado comprovável e aprendizados.</p></li>
</ol></div></section>
{cta_final()}
'''
page('cases/', f'Cases · {NAME}', 'Cases da FSA⁴Future contados do desafio ao impacto: o que encontramos, o que construímos junto com o cliente e o resultado comprovável.',
     'Mais de duas décadas resolvendo problemas que não vêm com manual.', cases, crumb=[('Cases', 'cases/')], noindex=True, data={'page': 'cases'}, priority='0.5',
     intent=dict(finalidade='Prova social (aguardando cases autorizados)', persona='Decisor buscando evidência', tema='Cases', cta=CTA))

# Sobre ---------------------------------------------------------------
pillars = [('Proximidade', 'O cliente participa, questiona, acompanha, valida e decide junto com a FSA.'),
           ('Tecnologia sem dogma', 'IA, automação, dados, cloud, integrações, full-code e outras tecnologias são meios. A escolha depende do problema.'),
           ('Capacidade de construir', 'A FSA não para no diagnóstico. Conecta, integra, automatiza, desenvolve e coloca tecnologia para funcionar.'),
           ('Experiência para enxergar além do pedido', 'Mais de duas décadas de atuação ajudam a identificar riscos, oportunidades e problemas que nem sempre estão evidentes no briefing inicial.')]
sobre = f'''
<section class="section--md" aria-labelledby="h1"><div class="container stack">
{crumbs([("Home", "{R}"), ("Sobre", "")])}
<div class="grid-split"><div class="stack">{eyebrow("Sobre")}<h1 class="h1" id="h1">Tecnologia construída junto, para resolver o que importa agora e preparar o que vem depois.</h1></div>
<div class="stack" style="align-self:end"><p class="lead">A {NAME_HTML} é um Technology &amp; Business Hub que combina experiência, proximidade e diferentes capacidades tecnológicas para entender, desenhar e construir soluções para desafios reais de negócio.</p><p>Com mais de 20 anos de experiência em consultoria e tecnologia como FSA Soluções em Tecnologia, atua da descoberta à execução, conectando competências próprias, parceiros e diferentes tecnologias conforme cada necessidade.</p></div></div>
</div></section>
<section class="section--md bg-petrol" aria-labelledby="h-prop"><div class="container grid-2">
<div class="stack-sm">{eyebrow("Propósito", True)}<h2 class="h3" id="h-prop">Transformar desafios de negócio em possibilidades por meio da tecnologia, construindo o futuro junto com as pessoas.</h2></div>
<div class="stack"><div class="stack-sm"><span class="label-up inv-muted">Promessa</span><p class="lead inv">Você traz o desafio. A gente encontra, conecta ou constrói a tecnologia para resolvê-lo.</p></div>
<div class="stack-sm"><span class="label-up inv-muted">Crença</span><p class="lead inv">Seu desafio não precisa caber em uma solução pronta.</p></div></div>
</div></section>
<section class="section--md" aria-labelledby="h-pil"><div class="container stack-lg">
<h2 class="h2" id="h-pil">O que guia a gente.</h2>
<div class="grid-4">{"".join(f'<div class="f4-card stack-sm"><h3 class="h4">{t}</h3><p class="small">{d}</p></div>' for t, d in pillars)}</div>
</div></section>
<section class="section--md bg-sand100" aria-labelledby="h-her"><div class="container grid-2" style="align-items:center">
<div class="stack"><h2 class="h3" id="h-her">Uma nova marca, a mesma escuta.</h2><p class="lead">A FSA Soluções em Tecnologia agora é {NAME_HTML}. O amarelo que acompanhou a empresa por mais de 20 anos continua no logo, no nó que representa o cliente: quem sempre esteve no centro do trabalho.</p><p class="label-up" style="color:var(--copper-700)">{CAMPAIGN}</p></div>
<div class="f4-card stack-sm" style="align-items:center;text-align:center;padding:48px"><img src="{{R}}assets/logo/fsa4future-symbol-light.svg" alt="Símbolo FSA⁴Future: núcleo, órbitas abertas e o nó amarelo do cliente" width="160" height="160" loading="lazy"><p class="small muted">Nada sobre o cliente sem o cliente.</p></div>
</div></section>
{cta_final()}
'''
page('sobre/', f'Sobre a FSA⁴Future, antes FSA Soluções em Tecnologia · {NAME}',
     'A FSA Soluções em Tecnologia agora é FSA⁴Future: um Technology & Business Hub com mais de 20 anos em consultoria e tecnologia, da descoberta à execução.',
     'Tecnologia construída junto, para resolver o que importa agora e preparar o que vem depois.', sobre, crumb=[('Sobre', 'sobre/')], priority='0.7',
     schema_extra=[{'@type': 'AboutPage', 'name': 'Sobre a FSA⁴Future', 'url': BASE + 'sobre/', 'about': {'@id': BASE + '#organization'}}],
     intent=dict(finalidade='Explicar o rebranding e a entidade (GEO)', persona='Decisor e mecanismos de busca/IA', tema='Quem é a FSA⁴Future', cta=CTA))

# Conteúdos -------------------------------------------------------------
cont = f'''
<section class="section--md" aria-labelledby="h1"><div class="container stack">
{crumbs([("Home", "{R}"), ("Conteúdos", "")])}
<div class="grid-split"><div class="stack">{eyebrow("Conteúdos")}<h1 class="h1" id="h1">A FSA não fala de tecnologia para parecer tecnológica.</h1></div>
<p class="lead" style="align-self:end">Fala de tecnologia para ajudar alguém a enxergar melhor um problema, uma possibilidade ou o que vem depois. Os primeiros conteúdos estão em produção, com autoria e data.</p></div>
</div></section>
<section class="section--md bg-sand100" aria-labelledby="h-temas"><div class="container stack-lg">
<h2 class="h3" id="h-temas">Perguntas que vamos responder.</h2>
<ul class="grid-2" style="list-style:none;margin:0;padding:0;gap:16px">{"".join(f'<li class="f4-card f4-card--compact"><p class="strong">{q}</p><span class="f4-badge f4-badge--neutral" style="justify-self:start;align-self:flex-start">Em produção</span></li>' for q in QUESTIONS)}</ul>
</div></section>
{cta_final()}
'''
page('conteudos/', f'Conteúdos sobre IA, automação, integração e sistemas legados · {NAME}',
     'Respostas diretas para decisões reais: IA ou automação, quando integrar ou substituir um legado, como reduzir trabalho manual. Com autoria e data.',
     'A FSA não fala de tecnologia para parecer tecnológica.', cont, crumb=[('Conteúdos', 'conteudos/')], noindex=True, priority='0.5',
     intent=dict(finalidade='Hub editorial (aguardando primeiros artigos)', persona='Decisor pesquisando uma decisão', tema='Conteúdo decisório', cta=CTA))

# Conversar ---------------------------------------------------------------
conv = f'''
<section class="section--md" aria-labelledby="h1"><div class="container grid-2 cols-contact">
<div class="stack">
{crumbs([("Home", "{R}"), ("Conversar", "")])}
{eyebrow("Vamos conversar")}
<h1 class="h1" id="h1" style="font-size:clamp(36px,5vw,52px);line-height:1.1">Qual desafio precisamos resolver juntos?</h1>
<p class="lead">Conte um pouco sobre o seu desafio. Não precisa saber qual tecnologia usar. Essa parte a gente descobre junto.</p>
<div class="f4-card f4-card--sand f4-card--compact"><span class="f4-badge f4-badge--petrol" style="align-self:flex-start">30 min · gratuita</span><h2 class="h4" style="font-size:18px;line-height:26px">Conversa de Entendimento FSA</h2><p class="small" style="color:var(--graphite-700)">Um primeiro encontro para ouvir seu contexto, entender o desafio e identificar juntos qual pode ser o próximo passo. Não precisa chegar com a solução definida. É justamente para isso que vamos conversar.</p></div>
<p class="small muted">Prefere conversar antes com a assistente digital? <button type="button" class="linklike brand" style="font-weight:600;text-decoration:underline" data-fsia-open>Fale com a FSiA</button>.</p>
</div>
<form class="f4-card form-card" id="conversar-form" novalidate aria-labelledby="form-title">
<h2 class="visually-hidden" id="form-title">Formulário de conversa</h2>
<ol class="flow-steps" aria-label="Etapas do formulário"><li aria-current="step">01 Seu desafio</li><li>02 Seus dados</li><li>03 Como continuar</li></ol>
<fieldset data-stage="1" class="stack" style="border:0;padding:0;margin:0">
<legend class="visually-hidden">Seu desafio</legend>
<h3 class="h4 stage-title">Conte o desafio.</h3>
<div class="f4-field"><label class="f4-label" for="desafio">O que está acontecendo hoje? <span class="req" aria-hidden="true">*</span></label>
<textarea class="f4-textarea" id="desafio" name="desafio" rows="6" required aria-required="true" aria-describedby="desafio-hint" placeholder="Ex.: temos três sistemas que não conversam e a equipe redigita os mesmos dados todos os dias."></textarea>
<span class="f4-hint" id="desafio-hint">Não precisa usar termos técnicos.</span></div>
<div class="f4-field"><label class="f4-label" for="porte">Tamanho da empresa <span class="f4-label__opt">(opcional)</span></label>
<div class="f4-select-wrap"><select class="f4-select" id="porte" name="porte"><option value="">Selecione</option><option>Até 50 pessoas</option><option>51 a 200 pessoas</option><option>201 a 1000 pessoas</option><option>Mais de 1000 pessoas</option></select>{ic("chevron-down", 18)}</div></div>
<p class="form-error" role="alert"></p>
<div><button type="button" class="f4-btn f4-btn--primary" id="to-2">Continuar {ic("arrow-right", None, "f4-btn__arrow")}</button></div>
</fieldset>
<fieldset data-stage="2" class="stack" style="border:0;padding:0;margin:0" hidden>
<legend class="visually-hidden">Seus dados</legend>
<h3 class="h4 stage-title">Seus dados.</h3>
<div class="fields-2">
<div class="f4-field"><label class="f4-label" for="nome">Nome <span class="req" aria-hidden="true">*</span></label><input class="f4-input" id="nome" name="nome" autocomplete="name" required aria-required="true"></div>
<div class="f4-field"><label class="f4-label" for="empresa">Empresa <span class="req" aria-hidden="true">*</span></label><input class="f4-input" id="empresa" name="empresa" autocomplete="organization" required aria-required="true"></div>
<div class="f4-field"><label class="f4-label" for="email">E-mail corporativo <span class="req" aria-hidden="true">*</span></label><input class="f4-input" id="email" name="email" type="email" autocomplete="email" inputmode="email" required aria-required="true"></div>
<div class="f4-field"><label class="f4-label" for="telefone">Telefone ou WhatsApp <span class="f4-label__opt">(opcional)</span></label><input class="f4-input" id="telefone" name="telefone" type="tel" autocomplete="tel" inputmode="tel"></div>
</div>
<label class="f4-check"><input type="checkbox" id="lgpd" name="lgpd" required aria-required="true"><span class="f4-check__box" aria-hidden="true">{ic("check", 16)}</span><span>Autorizo o uso destes dados para a FSA⁴Future retornar sobre o meu desafio, conforme a <a href="{{R}}privacidade/">Política de Privacidade</a>.</span></label>
<p class="form-error" role="alert"></p>
<div class="row"><button type="button" class="f4-btn f4-btn--ghost" id="back-1">{ic("arrow-left")} Voltar</button><button type="button" class="f4-btn f4-btn--primary" id="to-3">Continuar {ic("arrow-right", None, "f4-btn__arrow")}</button></div>
</fieldset>
<fieldset data-stage="3" class="stack" style="border:0;padding:0;margin:0" hidden>
<legend class="visually-hidden">Como continuar</legend>
<h3 class="h4 stage-title">Como você prefere continuar?</h3>
<p class="small muted">O resumo do que você contou vai junto, para você não precisar repetir tudo.</p>
<div class="channel-grid" id="channels"></div>
<p class="form-error" role="alert"></p>
<div><button type="button" class="f4-btn f4-btn--ghost" id="back-2">{ic("arrow-left")} Voltar</button></div>
</fieldset>
</form>
</div></section>
<section class="section--sm" id="calendly-wrap" hidden aria-labelledby="calendly-title"><div class="container stack">
<h2 class="h3" id="calendly-title" tabindex="-1">Conversa de Entendimento FSA — 30 min</h2>
<p class="muted">Escolha o melhor horário. O convite com o link do Google Meet chega no seu e-mail.</p>
<div class="calendly-box" id="calendly-box"></div>
</div></section>
'''
CONFIRM_DIALOG = f'''<dialog class="f4-dialog" id="confirm-dialog" aria-labelledby="confirm-title">
<h2 class="f4-dialog__title" id="confirm-title">Conversa agendada.</h2>
<p>Seu desafio já chegou até nós. No encontro, vamos ouvir o contexto, entender o que precisa ser resolvido e avaliar juntos o melhor próximo passo.</p>
<p class="strong brand mt-24" id="confirm-when" hidden></p>
<p class="small muted mt-24" id="confirm-note">O convite com data, horário e link do Google Meet foi enviado para o seu e-mail. Use o convite para adicionar a conversa à sua agenda.</p>
<div class="f4-dialog__actions">
<a class="f4-btn f4-btn--primary" id="confirm-add" href="#" hidden data-track="adicionar_agenda">{ic("calendar-plus")} Adicionar à agenda</a>
<a class="f4-btn f4-btn--secondary" id="confirm-gcal" href="#" target="_blank" rel="noopener" hidden data-track="adicionar_agenda_google">Google Agenda</a>
<a class="f4-btn f4-btn--ghost" href="{{R}}">Voltar ao início</a>
</div>
<button type="button" class="f4-iconbtn f4-dialog__close" data-dialog-close aria-label="Fechar">{ic("x")}</button>
</dialog>'''
page('conversar/', f'Vamos conversar: Conversa de Entendimento gratuita · {NAME}',
     'Conte o seu desafio, escolha como continuar e agende a Conversa de Entendimento FSA: 30 minutos, gratuita, para ouvir seu contexto e definir o próximo passo.',
     'Qual desafio precisamos resolver juntos?', conv + CONFIRM_DIALOG, crumb=[('Conversar', 'conversar/')], priority='0.9', data={'page': 'conversar'},
     schema_extra=[{'@type': 'ContactPage', 'name': 'Conversar com a FSA⁴Future', 'url': BASE + 'conversar/'}],
     intent=dict(finalidade='Conversão: desafio → dados → canal → agenda', persona='Decisor pronto para conversar', tema='Contato e agendamento', cta='Agendar a Conversa de Entendimento'))

confirm = f'''
<section class="section" id="confirm-page" aria-labelledby="h1"><div class="container stack maxw-720">
{eyebrow("Conversa de Entendimento FSA")}
<h1 class="h1" id="h1">Conversa agendada.</h1>
<p class="lead">Seu desafio já chegou até nós. No encontro, vamos ouvir o contexto, entender o que precisa ser resolvido e avaliar juntos o melhor próximo passo.</p>
<div class="row">{btn("Voltar ao início", "{R}", "secondary", arrow=False)}{btn("Conhecer o método", "{R}como-fazemos/", "ghost")}</div>
</div></section>
''' + CONFIRM_DIALOG
page('conversar/confirmado/', f'Conversa agendada · {NAME}', 'Sua Conversa de Entendimento FSA está agendada.', 'Conversa agendada.', confirm,
     crumb=[('Conversar', 'conversar/'), ('Conversa agendada', 'conversar/confirmado/')], noindex=True, priority='0.1',
     intent=dict(finalidade='Confirmação pós-agendamento (redirect do Calendly)', persona='Quem acabou de agendar', tema='Confirmação', cta='Adicionar à agenda'))

# Políticas (rascunho v1, aguardando revisão jurídica) -------------------
DRAFT = f'<div class="notice" role="note">{ic("info", 18)}<span>Rascunho v1.0 em revisão jurídica. A versão vigente será publicada com a data de atualização.</span></div>'
priv = f'''
<section class="section--md"><div class="container stack">
{crumbs([("Home", "{R}"), ("Política de Privacidade", "")])}
<h1 class="h2" id="h1">Política de Privacidade.</h1>{DRAFT}
<div class="prose">
<h2>1. Quem somos</h2><p>A FSA⁴Future é a marca da <strong>{LEGAL}</strong>, CNPJ {CNPJ}, controladora dos dados pessoais tratados neste site, na assistente digital FSiA e no Programa de Parceiros FSA⁴Partners. Contato para assuntos de privacidade: <a href="mailto:{EMAIL}?subject=Privacidade">{EMAIL}</a>, com o assunto "Privacidade".</p>
<h2>2. A quem esta política se aplica</h2><ul><li>visitantes do site;</li><li>quem conversa com a FSiA;</li><li>quem preenche formulários ou agenda uma conversa;</li><li>parceiros do Programa FSA⁴Partners e seus representantes;</li><li>contatos indicados por parceiros.</li></ul>
<h2>3. Quais dados tratamos, para quê e com qual base legal</h2>
<table><thead><tr><th>Situação</th><th>Dados</th><th>Para quê</th><th>Base legal (LGPD, art. 7º)</th></tr></thead><tbody>
<tr><td>Formulário e agendamento</td><td>nome, empresa, cargo, e-mail, telefone/WhatsApp, descrição do desafio</td><td>responder e preparar a conversa</td><td>procedimentos preliminares a contrato, a pedido do titular (V)</td></tr>
<tr><td>Conversa com a FSiA</td><td>mensagens e resumo da conversa</td><td>orientar e, com sua autorização, enviar o resumo ao time</td><td>procedimentos preliminares (V); consentimento para o envio do resumo (I)</td></tr>
<tr><td>Navegação</td><td>dados técnicos (IP, navegador, páginas visitadas) e cookies</td><td>funcionamento, segurança e, com consentimento, estatísticas de uso</td><td>legítimo interesse (IX) para os necessários; consentimento (I) para os de análise</td></tr>
<tr><td>Registros de acesso</td><td>IP, data e hora de acesso</td><td>obrigação legal de guarda (Marco Civil da Internet, art. 15)</td><td>cumprimento de obrigação legal (II)</td></tr>
<tr><td>Cadastro de parceiro</td><td>dados da empresa e do representante</td><td>adesão, contrato, apuração e pagamento de comissões</td><td>execução de contrato (V); obrigação legal e fiscal (II)</td></tr>
<tr><td>Indicação de cliente por parceiro</td><td>dados de contato do indicado, CNPJ e desafio da empresa</td><td>avaliar a oportunidade e entrar em contato</td><td>legítimo interesse (IX), com declaração do parceiro de que o contato autorizou</td></tr>
<tr><td>Clientes</td><td>dados de contato e de faturamento</td><td>execução do contrato e emissão de notas</td><td>execução de contrato (V); obrigação legal (II)</td></tr>
</tbody></table>
<p>Não pedimos dados sensíveis (saúde, religião, origem racial, biometria etc.) nem documentos pessoais pelo site ou pela FSiA.</p>
<h2>4. A FSiA</h2><p>A FSiA é uma assistente digital automatizada, não uma pessoa. Ela orienta e coleta contexto, não toma decisões sobre você e não fecha preço nem contrato. A qualquer momento você pode pedir para falar com uma pessoa.</p>
<h2>5. Com quem compartilhamos</h2><p>Só o necessário, com provedores de hospedagem, e-mail, agenda, mensagens e análise de uso que tratam dados em nosso nome; com a contabilidade, para obrigações fiscais; com instituições financeiras, para pagamentos; e com autoridades, quando a lei exigir. Não vendemos dados pessoais.</p>
<h2>6. Transferência internacional</h2><p>Alguns provedores podem armazenar dados fora do Brasil. Nesses casos, adotamos os mecanismos previstos na LGPD e na regulamentação da ANPD.</p>
<h2>7. Por quanto tempo guardamos</h2><table><thead><tr><th>Dado</th><th>Prazo</th></tr></thead><tbody><tr><td>Contatos que não viraram cliente</td><td>até 24 meses após o último contato</td></tr><tr><td>Conversas da FSiA</td><td>até 12 meses</td></tr><tr><td>Registros de acesso ao site</td><td>6 meses (Marco Civil da Internet)</td></tr><tr><td>Dados de parceiros e de clientes</td><td>durante o contrato e por 5 anos após o fim</td></tr></tbody></table>
<h2>8. Seus direitos</h2><p>Você pode pedir confirmação de tratamento, acesso, correção, anonimização, bloqueio ou eliminação, portabilidade, informação sobre compartilhamentos, revogação do consentimento e revisão de decisões automatizadas. Escreva para <a href="mailto:{EMAIL}?subject=Privacidade">{EMAIL}</a> com o assunto "Privacidade". Você também pode reclamar à ANPD.</p>
<h2>9. Segurança</h2><p>Usamos medidas técnicas e administrativas compatíveis com o porte da empresa, como acesso restrito, verificação em duas etapas e cópias de segurança.</p>
<h2>10. Crianças e adolescentes</h2><p>O site e a FSiA são voltados a empresas e não se destinam a menores de 18 anos.</p>
<h2>11. Cookies</h2><p>Veja a <a href="{{R}}cookies/">Política de Cookies</a>.</p>
<h2>12. Alterações</h2><p>A versão vigente fica sempre nesta página, com a data de atualização.</p>
</div></div></section>'''
priv = priv.replace('<table>', '<table tabindex="0">')
page('privacidade/', f'Política de Privacidade · {NAME}', 'Como a FSA⁴Future trata dados pessoais no site, na FSiA e no Programa de Parceiros, conforme a LGPD.', 'Política de Privacidade.', priv,
     crumb=[('Política de Privacidade', 'privacidade/')], noindex=True, priority='0.2',
     intent=dict(finalidade='Transparência LGPD (rascunho)', persona='Titular de dados', tema='Privacidade', cta='—'))

cook = f'''
<section class="section--md"><div class="container stack">
{crumbs([("Home", "{R}"), ("Política de Cookies", "")])}
<h1 class="h2" id="h1">Política de Cookies.</h1>{DRAFT}
<div class="prose">
<h2>1. O que são cookies</h2><p>São pequenos arquivos que o site guarda no seu navegador para funcionar e lembrar escolhas. Também usamos tecnologias parecidas, como armazenamento local; esta política vale para todas.</p>
<h2>2. Que cookies usamos</h2><table><thead><tr><th>Categoria</th><th>Para quê</th><th>Precisa do seu consentimento?</th></tr></thead><tbody>
<tr><td><strong>Necessários</strong></td><td>funcionamento do site, segurança e guardar sua escolha de cookies</td><td>Não. Sem eles o site não funciona.</td></tr>
<tr><td><strong>Preferências</strong></td><td>lembrar escolhas de navegação</td><td>Sim</td></tr>
<tr><td><strong>Análise</strong></td><td>entender, de forma agregada, como o site é usado, para melhorá-lo</td><td>Sim</td></tr>
<tr><td><strong>Marketing</strong></td><td>não usamos na versão atual do site</td><td>—</td></tr></tbody></table>
<table><thead><tr><th>Item</th><th>Fornecedor</th><th>Categoria</th><th>Finalidade</th><th>Duração</th></tr></thead><tbody>
<tr><td>f4_consent (armazenamento local)</td><td>FSA⁴Future</td><td>Necessário</td><td>guardar sua escolha de cookies, a data e a versão desta política</td><td>até você limpar os dados do navegador</td></tr>
<tr><td>f4_fsia_ctx (armazenamento da sessão)</td><td>FSA⁴Future</td><td>Necessário</td><td>manter o contexto da conversa com a FSiA enquanto a aba estiver aberta</td><td>até fechar a aba</td></tr>
<tr><td>Agenda incorporada</td><td>Calendly</td><td>Necessário quando você escolhe agendar</td><td>exibir horários e concluir o agendamento</td><td>definida pelo Calendly</td></tr>
<tr><td>Ferramenta de análise</td><td>a definir</td><td>Análise</td><td>estatísticas agregadas de uso, só com consentimento</td><td>a definir</td></tr>
</tbody></table>
<h2>3. Como escolher</h2><ul><li>Na primeira visita, um aviso permite aceitar todos, recusar os não necessários ou escolher por categoria.</li><li>Recusar é tão fácil quanto aceitar. Nada além dos necessários é ativado antes da sua escolha.</li><li>Você pode mudar a escolha a qualquer momento pelo link "Preferências de cookies" no rodapé.</li><li>No navegador, também dá para apagar ou bloquear cookies.</li></ul>
<h2>4. Contato</h2><p>Dúvidas: <a href="mailto:{EMAIL}?subject=Privacidade">{EMAIL}</a>, com o assunto "Privacidade".</p>
</div></div></section>'''
cook = cook.replace('<table>', '<table tabindex="0">')
page('cookies/', f'Política de Cookies · {NAME}', 'Quais cookies o site da FSA⁴Future usa, para quê, e como aceitar, recusar ou mudar sua escolha.', 'Política de Cookies.', cook,
     crumb=[('Política de Cookies', 'cookies/')], noindex=True, priority='0.2',
     intent=dict(finalidade='Transparência de cookies (rascunho)', persona='Visitante', tema='Cookies', cta='—'))

nf = f'''
<section class="section"><div class="container stack maxw-720">
{eyebrow("Página não encontrada")}
<h1 class="h1" id="h1">Esta página mudou de lugar ou não existe.</h1>
<p class="lead">O site da FSA Soluções em Tecnologia agora é {NAME_HTML}. Se você chegou por um link antigo, estes caminhos podem ajudar.</p>
<ul class="list-check"><li>{ic("arrow-right", 18)}<a href="{{R}}">Página inicial</a></li><li>{ic("arrow-right", 18)}<a href="{{R}}hub/">Hub: Flow, Partners, Solutions e Products</a></li><li>{ic("arrow-right", 18)}<a href="{{R}}como-fazemos/">Como fazemos</a></li><li>{ic("arrow-right", 18)}<a href="{{R}}conversar/">Conversar sobre um desafio</a></li></ul>
</div></section>'''
page('404.html', f'Página não encontrada · {NAME}', 'Página não encontrada.', 'Esta página mudou de lugar ou não existe.', nf, noindex=True, priority='0')


# ---------------------------------------------------------------- template
def org_schema():
    return {
        '@type': 'Organization', '@id': BASE + '#organization', 'name': NAME,
        'alternateName': ['FSA 4 Future', 'FSA4Future', 'FSA Soluções em Tecnologia'],
        'legalName': LEGAL, 'taxID': CNPJ, 'url': BASE,
        'logo': {'@type': 'ImageObject', 'url': BASE + 'assets/logo/fsa4future-symbol-light-512.png', 'width': 512, 'height': 512},
        'image': BASE + 'assets/img/og-1200x630.png',
        'email': EMAIL, 'slogan': SIGN,
        'description': 'Technology & Business Hub que combina experiência, proximidade e diferentes capacidades tecnológicas para entender, desenhar e construir soluções para desafios reais de negócio.',
        'knowsAbout': ['Automação de processos', 'Integração de sistemas', 'APIs', 'Desenvolvimento de software sob medida', 'Modernização de sistemas legados', 'Inteligência artificial aplicada a negócios', 'Dados', 'Cloud'],
        'contactPoint': [{'@type': 'ContactPoint', 'contactType': 'customer service', 'email': EMAIL, 'availableLanguage': 'pt-BR', 'areaServed': 'BR'}],
    }


def render(p):
    depth = 0 if p['path'] in ('', '404.html') else p['path'].strip('/').count('/') + 1
    R = '../' * depth if depth else './'
    if p['path'] == '404.html':
        R = '/' if PROD else '/fsa4future/'
    url = BASE + (p['path'] if p['path'] != '404.html' else '')
    robots = 'noindex, nofollow' if (not PROD or p['noindex']) else 'index, follow, max-image-preview:large'
    graph = []
    if p['path'] == '':
        graph.append(org_schema())
        graph.append({'@type': 'WebSite', '@id': BASE + '#website', 'name': NAME, 'url': BASE, 'inLanguage': 'pt-BR', 'publisher': {'@id': BASE + '#organization'}})
    else:
        graph.append({'@type': 'Organization', '@id': BASE + '#organization', 'name': NAME, 'url': BASE, 'logo': BASE + 'assets/logo/fsa4future-symbol-light-512.png'})
    if p['crumb']:
        items = [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': BASE}] + [
            {'@type': 'ListItem', 'position': i + 2, 'name': n, 'item': BASE + u} for i, (n, u) in enumerate(p['crumb'])]
        graph.append({'@type': 'BreadcrumbList', 'itemListElement': items})
    graph.append({'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': p['title'], 'description': p['description'], 'inLanguage': 'pt-BR', 'isPartOf': {'@id': BASE + '#website'}, 'about': {'@id': BASE + '#organization'}, 'dateModified': UPDATED})
    graph.extend(p['schema_extra'])
    ld = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    cur = p['path'].split('/')[0] + '/' if p['path'] else ''
    nav = ''.join(f'<li><a href="{R}{h}"{" aria-current=\"page\"" if cur == h else ""}>{l}</a></li>' for h, l in NAV)
    data_attrs = ''.join(f' data-{k}="{E(v)}"' for k, v in p['data'].items())
    body = p['body'].replace('{R}', R)
    og_img = BASE + 'assets/img/og-1200x630.png'
    return f'''<!doctype html>
<html lang="pt-BR" data-root="{R}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(p["title"])}</title>
<meta name="description" content="{E(p["description"])}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#073B4C">
<meta property="og:type" content="{p["og_type"]}">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{E(p["title"])}">
<meta property="og:description" content="{E(p["description"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{NAME} · Technology &amp; Business Hub · {SIGN}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{E(p["title"])}">
<meta name="twitter:description" content="{E(p["description"])}">
<meta name="twitter:image" content="{og_img}">
<link rel="icon" href="{R}favicon.ico" sizes="any">
<link rel="icon" href="{R}assets/logo/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{R}assets/logo/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{R}assets/logo/favicon-180.png">
<link rel="manifest" href="{R}site.webmanifest">
<link rel="preload" href="{R}assets/fonts/montserrat-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{R}assets/fonts/montserrat-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{R}assets/css/site.css">
<script type="application/ld+json">{ld}</script>
<script src="{R}assets/js/site.js" defer></script>
</head>
<body{data_attrs}>
<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<section class="consent" id="consent" aria-labelledby="consent-title" hidden>
<h2 class="h4" id="consent-title" style="font-size:18px;line-height:26px">Cookies e privacidade</h2>
<p class="small">Usamos o necessário para o site funcionar. Com sua permissão, também usamos cookies de análise para entender, de forma agregada, como o site é usado. Veja a <a href="{R}cookies/">Política de Cookies</a>.</p>
<div id="consent-options" class="stack-sm" hidden>
<label class="f4-check"><input type="checkbox" checked disabled><span class="f4-check__box" aria-hidden="true"><svg class="f4-icon f4-icon--16" aria-hidden="true"><use href="{R}assets/icons/sprite.svg#i-check"></use></svg></span><span>Necessários (sempre ativos)</span></label>
<label class="f4-check"><input type="checkbox" id="c-pref"><span class="f4-check__box" aria-hidden="true"><svg class="f4-icon f4-icon--16" aria-hidden="true"><use href="{R}assets/icons/sprite.svg#i-check"></use></svg></span><span>Preferências</span></label>
<label class="f4-check"><input type="checkbox" id="c-analise"><span class="f4-check__box" aria-hidden="true"><svg class="f4-icon f4-icon--16" aria-hidden="true"><use href="{R}assets/icons/sprite.svg#i-check"></use></svg></span><span>Análise</span></label>
</div>
<div class="row"><button type="button" class="f4-btn f4-btn--secondary f4-btn--sm" id="consent-reject">Recusar</button><button type="button" class="f4-btn f4-btn--secondary f4-btn--sm" id="consent-choose">Escolher</button><button type="button" class="f4-btn f4-btn--secondary f4-btn--sm" id="consent-accept">Aceitar</button><button type="button" class="f4-btn f4-btn--primary f4-btn--sm" id="consent-save" hidden>Salvar escolha</button></div>
</section>
<header class="site-header"><div class="container site-header__in">
<a class="logo" href="{R}" aria-label="{NAME}, Technology &amp; Business Hub: página inicial">
<img class="logo__img" src="{R}assets/logo/fsa4future-logo-light.svg" alt="" width="187" height="40"></a>
<nav class="nav" id="nav" aria-label="Principal"><ul>{nav}</ul></nav>
<button type="button" class="f4-iconbtn menu-btn" id="menu-btn" aria-expanded="false" aria-controls="nav" aria-label="Abrir menu"><svg class="f4-icon f4-icon--24" aria-hidden="true"><use href="{R}assets/icons/sprite.svg#i-menu"></use></svg></button>
<a class="f4-btn f4-btn--primary f4-btn--sm header-cta" href="{R}conversar/" data-track="cta_principal" data-track-label="Header · Vamos conversar">Vamos conversar</a>
</div></header>
<main id="conteudo" tabindex="-1">
{body}
</main>
<footer class="site-footer"><div class="container">
<div class="footer-grid">
<div class="footer-col"><a class="logo logo--light" href="{R}" aria-label="{NAME}, Technology &amp; Business Hub: página inicial"><img class="logo__img logo__img--desc" src="{R}assets/logo/fsa4future-logo-descriptor-dark.svg" alt="" width="260" height="58" loading="lazy"></a><p class="inv-accent" style="font-weight:500">{SIGN}</p></div>
<div class="footer-col"><h2>Como fazemos</h2><ul>{"".join(f'<li><a href="{R}como-fazemos/{s["slug"]}/">{s["name"]}</a></li>' for s in STEPS)}</ul></div>
<div class="footer-col"><h2>Hub</h2><ul>{"".join(f'<li><a href="{R}hub/{f["slug"]}/">{f["name"]}</a></li>' for f in FRONTS)}<li><a href="{R}hub/fsa-4-partners/programa/">Programa de Parceiros</a></li></ul></div>
<div class="footer-col"><h2>Contato</h2><ul><li><a href="mailto:{EMAIL}" data-track="clique_email" data-track-label="Rodapé · e-mail">{EMAIL}</a></li><li><a href="{R}conversar/">Agendar conversa</a></li><li><button type="button" class="linklike" data-fsia-open>Fale com a FSiA</button></li></ul></div>
</div>
<div class="footer-legal">
<div class="links"><a href="{R}privacidade/">Política de Privacidade</a><a href="{R}cookies/">Política de Cookies</a><button type="button" class="linklike" data-consent-open>Preferências de cookies</button><a href="{R}hub/fsa-4-partners/programa/">Programa de Parceiros</a></div>
<p>{LEGAL} · CNPJ {CNPJ}</p>
<p>© {YEAR} {NAME}. Todos os direitos reservados.</p>
</div>
</div></footer>

<div class="fsia" id="fsia">
<section class="fsia__panel" id="fsia-panel" role="dialog" aria-modal="false" aria-labelledby="fsia-title" hidden>
<div class="fsia__head"><div style="flex:1"><b id="fsia-title">FSiA</b><div class="small">Assistente digital da FSA⁴Future</div></div><button type="button" class="f4-iconbtn f4-iconbtn--inverse" id="fsia-close" aria-label="Fechar a FSiA"><svg class="f4-icon" aria-hidden="true"><use href="{R}assets/icons/sprite.svg#i-x"></use></svg></button></div>
<div class="fsia__log" id="fsia-log" role="log" aria-live="polite" aria-relevant="additions"></div>
<form class="fsia__form" id="fsia-form" autocomplete="off"><label class="visually-hidden" for="fsia-input">Escreva sua mensagem</label><input class="f4-input" id="fsia-input" placeholder="Escreva sua mensagem" maxlength="1000" enterkeyhint="send"><button type="submit" class="f4-iconbtn f4-iconbtn--primary" aria-label="Enviar"><svg class="f4-icon" aria-hidden="true"><use href="{R}assets/icons/sprite.svg#i-send"></use></svg></button></form>
<p class="fsia__note">A FSiA é uma assistente automatizada. Ela não passa preço, prazo nem escopo. Não envie CPF, senhas ou dados bancários.</p>
</section>
<button type="button" class="fsia__launcher" id="fsia-launcher" aria-expanded="false" aria-controls="fsia-panel" data-track="fsia_launcher"><svg class="f4-icon f4-icon--22" aria-hidden="true"><use href="{R}assets/icons/sprite.svg#i-message-circle"></use></svg>Fale com a FSiA</button>
</div>

</body>
</html>
'''


def main():
    for p in PAGES:
        out = os.path.join(OUT, p['path'] if p['path'].endswith('.html') else os.path.join(p['path'], 'index.html'))
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, 'w', encoding='utf-8') as fh:
            fh.write(render(p))
    # sitemap: só URLs canônicas e indexáveis
    urls = [p for p in PAGES if not p['noindex'] and p['path'] != '404.html']
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in urls:
        sm.append(f'  <url><loc>{BASE + p["path"]}</loc><lastmod>{UPDATED}</lastmod><priority>{p["priority"]}</priority></url>')
    sm.append('</urlset>')
    open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(sm) + '\n')
    rob = ('User-agent: *\nDisallow: /parceiros/\nAllow: /\n\nSitemap: ' + BASE + 'sitemap.xml\n') if PROD else \
        ('# HOMOLOGAÇÃO: este arquivo só vale na raiz do domínio. Em produção, gere com --prod.\nUser-agent: *\nDisallow: /\n')
    open(os.path.join(OUT, 'robots.txt'), 'w', encoding='utf-8').write(rob)
    manifest = {'name': 'FSA⁴Future · Technology & Business Hub', 'short_name': 'FSA⁴Future', 'lang': 'pt-BR', 'start_url': './', 'display': 'browser',
                'background_color': '#F8F6F1', 'theme_color': '#073B4C',
                'icons': [{'src': 'assets/logo/favicon-192.png', 'sizes': '192x192', 'type': 'image/png'}, {'src': 'assets/logo/favicon-512.png', 'sizes': '512x512', 'type': 'image/png'}]}
    open(os.path.join(OUT, 'site.webmanifest'), 'w', encoding='utf-8').write(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    # ficha de intenção por URL (G3)
    rows = ['| URL | Finalidade | Persona/intenção | Tema principal | Title | Meta description | H1 | CTA | Indexação | Schema |', '|---|---|---|---|---|---|---|---|---|---|']
    for p in PAGES:
        if p['path'] == '404.html':
            continue
        i = p['intent']
        sch = ', '.join(['Organization', 'WebSite'] if p['path'] == '' else ['WebPage', 'BreadcrumbList'] + [s['@type'] for s in p['schema_extra']])
        cell = lambda s: str(s).replace('|', '\\|')
        rows.append(f'| /{p["path"]} | {cell(i.get("finalidade", ""))} | {cell(i.get("persona", ""))} | {cell(i.get("tema", ""))} | {cell(p["title"])} | {cell(p["description"])} | {cell(p["h1"])} | {cell(i.get("cta", ""))} | {"noindex" if p["noindex"] else "index"} | {sch} |')
    doc = os.path.join(OUT, '..', 'docs', 'fsa4future', 'fichas-de-intencao.md')
    os.makedirs(os.path.dirname(doc), exist_ok=True)
    open(doc, 'w', encoding='utf-8').write('# FSA⁴Future · Fichas de intenção por URL (G3)\n\nGerado por `tools/build_fsa4future.py` em ' + UPDATED + '. Editar os dados no gerador, não aqui.\n\n'
                         'Campos ainda pendentes por URL (preencher com a FSA): links internos de entrada e saída validados, conteúdo/evidência necessária, responsável e status.\n\n' + '\n'.join(rows) + '\n')
    print(f'{len(PAGES)} páginas · {"PRODUÇÃO" if PROD else "HOMOLOGAÇÃO (noindex)"} · sitemap com {len(urls)} URLs')


if __name__ == '__main__':
    main()
