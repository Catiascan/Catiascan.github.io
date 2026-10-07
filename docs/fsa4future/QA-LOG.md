# QA Log — FSA⁴Future (Implementação / Pré-lançamento)

Regra: cada achado é tratado primeiro como problema de implementação. O Design System v1.1 (congelado) só muda com evidência de que o próprio sistema é a causa. Nada aqui reabre marca, posicionamento, arquitetura, método, cores ou estratégia SEO/GEO.

**Prioridade de triagem:** Bloqueio → Conversão → Acessibilidade → SEO/GEO/Performance → Responsivo/Compatibilidade → Acabamento visual.
**Gates:** G1 Navegador/dispositivo · G2 Acessibilidade · G3 Performance + SEO/GEO técnico · G4 Conversão de ponta a ponta.

**Ambiente de teste automatizado (06/10/2026):** Chromium 141 (Playwright 1.56, headless) em Linux · viewports 1440×900, 1024×768 e 390×844 (mobile com toque) · axe-core 4.14 (WCAG 2.0/2.1/2.2 A e AA + boas práticas) · servidor estático local. **Não substitui** o teste em aparelhos reais (Safari iOS, Chrome Android, Edge): esses itens seguem abertos no G1.

## Modelo de achado
```
### QA-### — <título curto>
- Severidade: Bloqueio | Conversão | Acessibilidade | SEO/GEO/Performance | Responsivo/Compat | Visual
- Gate: G1 | G2 | G3 | G4
- Página / componente:
- Ambiente: dispositivo · SO · navegador + versão · viewport · zoom
- Esperado:
- Observado:
- Evidência:
- Diagnóstico: implementação | design system (exige evidência)
- Correção recomendada:
- Correção aplicada: — (data, arquivo)
- Status: Aberto | Em andamento | Corrigido – aguardando reteste | Fechado
```

## Achados

### QA-001 — Ícones capturados como quadrados brancos
- Severidade: Responsivo/Compat · Gate: G1
- Página / componente: Icon (todas as páginas)
- Ambiente: captura automatizada (html-to-image) · ~907px (achado original de 29/09)
- Esperado: ícones Lucide na cor do texto.
- Observado: quadrados brancos na captura; máscara CSS correta e unpkg 200 + ACAO:*.
- Diagnóstico: implementação (dependência de máscara CSS servida por CDN de terceiros).
- Correção aplicada: 06/10/2026 — ícones passam a ser um sprite SVG local (`fsa4future/assets/icons/sprite.svg`, 28 ícones Lucide 0.460.0, licença ISC) usado com `<svg><use>`, same-origin, herdando `currentColor`. Sem chamada ao unpkg. (`assets/css/site.css`, `tools/build_fsa4future.py`)
- Evidência pós-correção: Chromium 1440/1024/390 sem 404 e ícones visíveis nas capturas.
- Status: Corrigido – aguardando reteste em Chrome/Edge desktop e Safari/Chrome mobile reais.

### QA-002 — Ajuste óptico do logo v0 (Fernando)
- Severidade: Visual · Gate: — (não bloqueia)
- Página / componente: Logo v0 (`assets/logo/`)
- Esperado: equilíbrio óptico do ⁴, espessura das órbitas legível a 48 px, espaçamento símbolo/nome/descritor; AI e PDF editáveis.
- Observado: vetor provisório v0 liberado pela CEO em 06/10/2026 para uso imediato.
- Diagnóstico: refinamento de arte-final.
- Correção recomendada: Fernando revisa, gera AI e PDF editáveis e substitui os arquivos **mantendo os mesmos nomes**.
- Status: Aberto (não bloqueante).

### QA-003 — Pacote `assets/logo/` v0 ausente no ambiente de implementação; símbolo provisório de implementação
- Severidade: Bloqueio (para o lançamento definitivo) · Gate: G3
- Página / componente: header, rodapé, favicon, OG, schema `Organization`
- Ambiente: sessão Claude Code em nuvem, 06/10/2026
- Esperado: SVG/PNG/ICO/OG do logo v0 de `assets/logo/` e `assets/logo/export/` disponíveis para aplicar no site e subir ao Drive (Design System v1 / Logo v0).
- Observado: o pacote descompactado do design system (com `SKILL.md`, `assets/logo/`, `guidelines/Plataforma_e_Parecer_Logo.md`) não estava no repositório nem no Drive. O artifact do Design System (01/10) e o Drive só têm a versão sem logo; o Drive tem `F4F_simbolo_positivo/negativo.svg` (29/09, em Mineral/Champagne).
- Diagnóstico: implementação (insumo faltando).
- Correção aplicada: 06/10/2026 — para não travar favicon, OG e schema, o site usa um **símbolo provisório de implementação** gerado da geometria do F4F (núcleo r23, órbitas r45/r72) recolorido conforme a decisão de 06/10: núcleo e órbitas Deep Petrol #073B4C e nó do cliente amarelo #F9DC6B com anel petróleo. O nome é tipografia Montserrat em HTML (sem vetor convertido). Arquivos: `fsa4future/assets/logo/fsa4future-simbolo.svg`, `-negativo.svg`, `-favicon.svg`, PNGs e `favicon.ico`.
- Correção recomendada: copiar o v0 oficial para `fsa4future/assets/logo/` com estes nomes (ou ajustar os nomes no gerador) e rodar o build; subir o v0 oficial ao Drive. **Não subir o símbolo provisório ao Drive como logo.**
- Correção aplicada (2): 06/10/2026, terminal — pacote encontrado em `Downloads\FSA 4 Future Design System (1).zip` (18h26). Símbolo provisório removido; o site usa os arquivos do v0 com os nomes do v0 (referências ajustadas em `tools/build_fsa4future.py`): `fsa4future-logo-light.svg` (header, 187×40 px), `fsa4future-logo-descriptor-dark.svg` (rodapé, 260 px, acima dos 240 px exigidos para o descritor), `fsa4future-symbol-light.svg` (Sobre), `favicon.svg` (núcleo + uma órbita), `favicon-32/180/192/512.png`, `favicon.ico` (ICO do v0), `fsa4future-symbol-light-512.png` (schema) e `assets/img/og-1200x630.png`. O nome deixou de ser texto HTML: agora é o lockup com nome em contornos, `alt=""` e o `aria-label` mantido no link. Verificado em Chrome desktop (1272 px) e em moldura de 390 px nas páginas Home, Sobre, Conversar, Hub/Flow e Ouvir: imagens carregam, sem overflow horizontal, logo do header não encosta no botão de menu. Logo v0 completo (50 arquivos: SVG + `export/`) enviado ao Drive em Design System v1 / Logo v0. Conferido: nó do cliente #F9DC6B com anel petróleo #073B4C nas versões coloridas de fundo claro; nas versões de fundo escuro o nó é amarelo sem anel (petróleo sobre petróleo não apareceria), e as monocromáticas não têm amarelo, como previsto no sistema de versões. Registrado, sem alterar o v0.
- Status: Fechado (A1 feita). Revisão óptica do v0 segue no QA-002, com o Fernando.

### QA-004 — Texto do CTA final e do Conversar falava "problema" com o cliente
- Severidade: Conversão · Gate: G4
- Página / componente: Home (CTA final), Conversar (H1) — kit `ui_kits/website/HomeScreen.jsx` e `ContactScreen.jsx`; Handoff v1.3 §11
- Esperado: regra de voz de 06/10 — "desafio" quando a FSA fala com o cliente: "Qual desafio precisamos resolver juntos?".
- Observado: kit e handoff usam "Qual problema precisamos resolver juntos?".
- Diagnóstico: implementação (texto anterior à regra de voz).
- Correção aplicada: 06/10/2026 — todas as ocorrências voltadas ao cliente usam "desafio" (`tools/build_fsa4future.py`). "Problema" segue nas falas institucionais e de método.
- Status: Corrigido – aguardando reteste de conteúdo.

### QA-005 — Pares de cor abaixo do AA na implementação dos componentes
- Severidade: Acessibilidade · Gate: G2
- Página / componente: Input/Textarea/Select, placeholder, MethodSteps inverso, texto muted sobre sand-300, botão sobre copper-500
- Ambiente: cálculo WCAG 2.x de luminância relativa
- Esperado: texto ≥ 4,5:1; borda de controle e ícones ≥ 3:1.
- Observado: borda sand-500 sobre branco 1,75:1; placeholder graphite-400 3,39:1; etapa inativa petrol-400 sobre petrol-900 4,17:1; graphite-500 sobre sand-300 4,48:1; branco sobre copper-500 3,75:1.
- Diagnóstico: implementação (escolha de token no componente; paleta intacta).
- Correção aplicada: 06/10/2026 (`assets/css/site.css`, bloco "IMPL QA-005"): borda de controle graphite-400 (3,39:1); placeholder graphite-500 (5,9:1); etapa inativa petrol-200 (7,47:1); muted sobre sand-300 → graphite-700 (9,56:1); botão sempre copper-600 #A85C34 (4,95:1), nunca copper-500 com texto.
- **Tons derivados das frentes (700 e 100) — aprovados no teste:** flow-700 7,82/6,57 · partners-700 6,86/5,64 · solutions-700 8,32/6,96 · products-700 10,69/8,70 (sobre branco / sobre o próprio 100). Barras e ícones 500 sobre branco ≥ 4,11:1. Ainda falta a revisão visual para oficializá-los.
- Status: Corrigido – aguardando reteste manual (e revisão visual dos derivados).

### QA-006 — Overflow horizontal em 390 px
- Severidade: Responsivo/Compat · Gate: G1
- Página / componente: Home, Hub (frentes), Programa de Parceiros, Privacidade, Cookies
- Ambiente: Chromium · 390×844
- Esperado: sem rolagem horizontal.
- Observado: scrollWidth 422–590 px. Itens de grid com `min-width:auto` + eyebrow, trilha e abas com `nowrap`.
- Diagnóstico: implementação.
- Correção aplicada: 06/10/2026 — `min-width:0` nos filhos de grid/stack; eyebrow e trilha podem quebrar linha abaixo de 560 px (`site.css`, "IMPL QA-006").
- Evidência: reteste automatizado em 19 páginas × 3 viewports sem overflow.
- Status: Corrigido – aguardando reteste em aparelho.

### QA-007 — Painéis do método todos visíveis na Home
- Severidade: Visual · Gate: G1
- Página / componente: Home · interação OUVIR → EVOLUIR
- Esperado: só o painel da etapa ativa.
- Observado: os 6 painéis visíveis; `display:grid` da classe vencia o atributo `hidden`.
- Correção aplicada: 06/10/2026 — `[hidden]{display:none!important}` (`site.css`).
- Status: Corrigido.

### QA-008 — Botão "Fale com a FSiA" cobre conteúdo no celular
- Severidade: Conversão · Gate: G1
- Página / componente: botão flutuante da FSiA · 390 px
- Observado: o botão cobre parte do CTA do hero e o fim da página.
- Correção aplicada: 06/10/2026 — `padding-bottom` de 84 px no `body` abaixo de 560 px; o painel aberto ocupa a tela toda e acompanha a altura do `visualViewport` (teclado virtual).
- Pendente: validar em iPhone (Safari) e Android (Chrome) com o teclado aberto; se o botão ainda atrapalhar o CTA do hero, avaliar com a FSA uma versão compacta.
- Status: Corrigido – aguardando reteste em aparelho.

### QA-009 — Menu mobile cortado
- Severidade: Bloqueio (navegação mobile) · Gate: G1
- Página / componente: header · ≤ 1100 px
- Observado: o menu aberto (position:fixed) aparecia cortado dentro dos 80 px do header.
- Diagnóstico: implementação — `backdrop-filter` no header cria bloco de contenção para filhos `fixed`.
- Correção aplicada: 06/10/2026 — blur movido para `.site-header:before` (`site.css`, "IMPL QA-009").
- Status: Corrigido – aguardando reteste em Safari iOS.

### QA-010 — Proporções de coluna inline quebravam o layout mobile
- Severidade: Responsivo/Compat · Gate: G1
- Página / componente: Conversar, Home (capacidades e prova), etapas do método
- Observado: no celular o formulário do Conversar ficava em duas colunas estreitas.
- Correção aplicada: 06/10/2026 — classes `.cols-*` aplicadas só acima de 860 px.
- Status: Corrigido.

### QA-011 — Resumo da FSiA repetia a linha "Desafio"
- Severidade: Conversão · Gate: G4
- Correção aplicada: 06/10/2026 (`assets/js/site.js`).
- Status: Corrigido.

### QA-012 — Horário da confirmação em UTC
- Severidade: Conversão · Gate: G4
- Página / componente: `/conversar/confirmado/`
- Observado: 14:00 (Brasília) exibido como 17:00 em navegador com fuso UTC.
- Correção aplicada: 06/10/2026 — formatação com `America/Sao_Paulo` e "(horário de Brasília)".
- Status: Corrigido.

### QA-013 — Acessibilidade: landmark duplicado, tabelas roláveis sem foco, ordem do aviso de cookies
- Severidade: Acessibilidade · Gate: G2
- Observado (axe): `landmark-unique` na Home (hero e manifesto com o mesmo nome); `scrollable-region-focusable` nas tabelas das políticas no celular. Aviso de cookies no fim do DOM (último na tabulação).
- Correção aplicada: 06/10/2026 — manifesto com `aria-label="Manifesto"`; tabelas com `tabindex="0"`; aviso de cookies logo após o link "Pular para o conteúdo".
- Evidência: axe-core sem violações em 19 páginas (1440 e 390 px); foco visível (contorno cobre 2 px) em toda a sequência de tabulação; `prefers-reduced-motion` zera transições; 720 px (≈ 200% de zoom em 1440) sem overflow.
- Status: Corrigido – falta teste com leitor de tela (NVDA/VoiceOver).

### QA-014 — Conflito de fontes sobre a cor do logo
- Severidade: Bloqueio (decisão de marca já tomada; registro) · Gate: —
- Observado: o LEIA-ME de 06/10 da pasta "Logo F4F para finalizar" diz que o símbolo é Mineral #0B0B0F + Champagne e que é a "única referência válida"; a decisão da CEO de 06/10 (prompt de continuação e Doc v1.3) define núcleo Deep Petrol e nó amarelo #F9DC6B com anel petróleo.
- Diagnóstico: documentação desatualizada no Drive.
- Correção recomendada: marcar o LEIA-ME de 06/10 como substituído pelo Doc v1.3 (ou mover para _DELETAR) quando o v0 oficial for subido. Implementação segue a decisão da CEO.
- Correção aplicada: 06/10/2026, terminal — LEIA-ME renomeado para "[SUBSTITUÍDO pelo Logo v0 em Design System v1] 00_LEIA-ME — Logo F4F e site (06-10-2026)" na pasta "Logo F4F para finalizar".
- Status: Fechado.

### QA-015 — Prazo de resposta (SLA) nos documentos de origem
- Severidade: Conversão · Gate: G4
- Observado: Handoff v1.3 §12/§24 e a base da FSiA (§10) citam "primeira resposta em até 4 horas úteis" e "retorno até as 13h do próximo dia útil".
- Esperado: decisão de 06/10 — não prometer SLA.
- Correção aplicada: 06/10/2026 — site e FSiA não citam prazo de resposta. O SLA fica só como regra interna de atendimento.
- Status: Fechado no site; documentos de origem continuam com o texto (atualizar na próxima versão do handoff).

### QA-016 — Visão ainda é proposta
- Severidade: Conteúdo · Gate: —
- Correção aplicada: a página Sobre publica Propósito, Promessa, Crença e Pilares; a Visão fica de fora até a validação.
- Validação 07/10/2026 (Cátia): a proposta original repetia a Crença ("não cabe em uma solução pronta"). Aprovada a versão: "Ser o hub de tecnologia e negócios que as empresas procuram primeiro quando precisam resolver um desafio de verdade."
- Correção aplicada (2): 07/10/2026 — Visão publicada na página Sobre, antes da Promessa e da Crença (`tools/build_fsa4future.py`).
- Status: Fechado.

### QA-017 — Domínio do site e do atendimento@ apontava para fsa4f.com.br, que não está registrado
- Severidade: Bloqueio · Gate: G3/G4
- Página / componente: canonical, sitemap, OG, schema, `EMAIL` do gerador, `CONFIG.email` e UID do .ics em `site.js`, documentos em `docs/fsa4future/`
- Ambiente: verificação no RDAP do Registro.br, 06/10/2026
- Esperado: domínio registrado no CNPJ 69.447.199/0001-05.
- Observado: `fsa4f.com.br` não está registrado. O domínio comprado pela Cátia em 05/10/2026, no CNPJ da FSA IT4FUTURE (Locaweb), é `fsa4future.com.br`.
- Diagnóstico: implementação (handoff v1.3 §25 com domínio não adquirido).
- Correção aplicada: 06/10/2026 — por decisão da Cátia, todas as ocorrências trocadas por `fsa4future.com.br`: `BASE`, `EMAIL`, `site.js` e documentos. O e-mail passa a ser atendimento@fsa4future.com.br. O redirect do Calendly passa a ser `https://fsa4future.com.br/conversar/confirmado/`. O `fsaforfuture.com.br` (mesmo titular) deve redirecionar para ele.
- Status: Fechado no código. O handoff de origem continua com o domínio antigo (atualizar na próxima versão).

### QA-018 — Gerador quebrava no Windows ao gravar sitemap, robots e manifest
- Severidade: Compatibilidade · Gate: —
- Ambiente: Windows 11 · Python 3.12 · terminal
- Observado: `UnicodeEncodeError` (cp1252) ao gravar `site.webmanifest`, por causa do ⁴; quatro `open(..., 'w')` sem `encoding`.
- Correção aplicada: 06/10/2026 — `encoding='utf-8'` nas quatro gravações de `tools/build_fsa4future.py`. A saída fica igual à do Linux.
- Status: Fechado.

### QA-019 — Contatos provisórios até a FSA⁴Future ter canais próprios
- Severidade: Conversão · Gate: G4
- Página / componente: `CONFIG` em `fsa4future/assets/js/site.js`, `EMAIL` em `tools/build_fsa4future.py` (rodapé, Parceiros, políticas, schema)
- Esperado (handoff): WhatsApp Business próprio da FSA⁴Future e atendimento@fsa4future.com.br.
- Observado: nenhum dos dois existe ainda.
- Decisão da Cátia, 06/10/2026: usar por enquanto os contatos da FSA — WhatsApp e telefone (12) 3351-9958 e e-mail catia@fsasolucoes.com.br — até tudo estar resolvido; ela pede a troca depois.
- Correção aplicada: 06/10/2026 — `CONFIG.whatsapp = '551233519958'`, `telefone = '+551233519958'`, `telefoneLabel = '(12) 3351-9958'`, `CONFIG.email` e `EMAIL = 'catia@fsasolucoes.com.br'`, marcados como PROVISÓRIO no código.
- Pendente: trocar pelos canais da FSA⁴Future (chip novo + WhatsApp Business e atendimento@) antes do go-live definitivo; o e-mail nominal só sai depois de todos os pontos migrarem (D8).
- Status: Provisório.

## Pendências abertas por gate

| Gate | Item | Dono | Situação |
|---|---|---|---|
| G1 | Teste real em Chrome/Edge desktop, Safari iOS e Chrome Android (ícones, menu, abas do Hub, trilhas, FSiA com teclado aberto, overflow) | Implementação | Aberto |
| G2 | Leitor de tela (NVDA + VoiceOver) e revisão visual dos tons derivados | Implementação + FSA | Aberto |
| G3 | Core Web Vitals em produção (PageSpeed/CrUX). Peso local da Home: HTML 6 KB, CSS 9 KB, JS 10 KB (gzip) + 4 fontes woff2 de ~19 KB, sem JS de terceiros na carga | Implementação | Aberto |
| G3 | Inventário do site atual e mapa de redirects 301 individuais (`docs/fsa4future/migracao-urls.md`) | Fernando (acesso) + Implementação | Bloqueado: acesso ao Search Console/analytics e inventário provavelmente só com o Fernando |
| G3 | Hospedagem com suporte a 301 (GitHub Pages não faz 301 por URL) | Implementação | Aberto |
| G3 | Build `--prod`, robots/sitemap na raiz, Search Console, Bing Webmaster Tools, IndexNow, validação do schema (Rich Results Test) | Implementação | Aberto |
| G3 | Fichas de intenção: completar links internos, evidência, responsável e status (`docs/fsa4future/fichas-de-intencao.md`) | FSA | Aberto |
| G4 | Criar atendimento@fsa4future.com.br (D8); até lá, o site usa catia@fsasolucoes.com.br (QA-019). 06/10: tentativa no Zoho Mail gratuito parou na verificação da conta; adiado. DNS do domínio na Locaweb sem MX/TXT (nada a limpar) 07/10: a aguardar resposta do Fernando | Cátia + Fernando | Provisório — à espera do Fernando |
| G4 | WhatsApp Business e telefone próprios da FSA⁴Future (hoje provisórios da FSA, QA-019) | FSA | Provisório |
| G4 | Calendly (conta catiascan@gmail.com): 06/10 — evento renomeado para "Conversa de Entendimento FSA — 30 min" (link igual), gratuito, Google Meet; a pergunta 1 já existe (texto, recebe o resumo via `a1`). 07/10: a Cátia confirma que o redirect de homologação já está configurado e conferido, e o evento tem 30 min. Fica só trocar para `https://fsa4future.com.br/conversar/confirmado/` no go-live | Cátia | Feito (homologação); trocar no go-live |
| G4 | Ferramenta de analytics (carregar só após consentimento em `loadAnalytics()`) e teste dos eventos | FSA + Implementação | Aberto |
| G4 | Endpoint de formulário opcional (`CONFIG.formEndpoint`) com cópia para atendimento@ | Implementação | Aberto |
| — | Políticas de Privacidade e Cookies: leitura jurídica antes de tirar o aviso de rascunho e o noindex. 07/10: leitura da skill jurídica feita (4 pontos críticos, 5 perguntas ao advogado), doc "Leitura jurídica — Políticas de Privacidade e Cookies do site FSA⁴Future (07-10-2026)" na pasta FSA4FUTURE do Drive | Cátia → advogado | À espera do advogado |
| — | Fotos reais (hoje: espaços reservados listrados) e cases autorizados. 07/10: ainda sem autorização dos clientes; site segue com espaços reservados | FSA | À espera de autorização |
| — | Portal do Parceiro (handoff §27.3–27.11): sistema com login, contrato e comissões — fora do escopo desta fase | — | Backlog pós-lançamento |
| — | Auditoria final de dependências/arquivos não usados (tarefa 9) | Implementação | 06/10 (terminal): único arquivo sem uso era `assets/logo/fsa4future-symbol-dark.svg` (removido; o original está no Drive, Logo v0). Licenças, robots.txt e sitemap.xml ficam (não são referenciados por página, mas são necessários). Nenhum recurso de terceiros na abertura: Calendly só ao escolher agendar; WhatsApp e Google Agenda só em links. Repetir antes do go-live |

## Backlog pós-lançamento
Ideias que não bloqueiam acessibilidade, SEO/GEO, segurança ou conversão.

| # | Ideia | Origem | Data |
|---|---|---|---|
| 1 | Portal do Parceiro com cadastro, contrato de adesão e apuração de comissões (handoff §27) | Handoff v1.2/v1.3 | 06/10/2026 |
| 2 | FSiA com modelo de linguagem (hoje é roteiro fechado da base de conhecimento, o que garante os limites) | Implementação | 06/10/2026 |
| 3 | Registro de perguntas sem resposta da FSiA como insumo editorial (precisa de backend + consentimento) | Base da FSiA §13 | 06/10/2026 |
