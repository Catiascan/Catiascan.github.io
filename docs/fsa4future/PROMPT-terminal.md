# Prompt — FSA⁴Future · concluir pendências no Claude Code (terminal)

Cole o texto abaixo no `claude`, **dentro da pasta onde você descompactou o pacote do design system** (a que tem `SKILL.md`, `assets/logo/` e `guidelines/Plataforma_e_Parecer_Logo.md`), com o repositório `Catiascan/Catiascan.github.io` clonado ao lado (branch `claude/epic-wright-n7cptm`).

---

Você é o responsável técnico pelo pré-lançamento da **FSA⁴Future · Technology & Business Hub**. O Design System v1.1 está **congelado**: não reabra marca, posicionamento, arquitetura, método, cores nem estratégia SEO/GEO. Todo achado é primeiro um problema de implementação e vai para o `QA-LOG.md` no formato QA-###.

Antes de agir, leia: `SKILL.md`, `readme.md`, `QA-LOG.md`, `guidelines/Plataforma_e_Parecer_Logo.md` (no pacote) e, no repositório, `docs/fsa4future/readme.md`, `docs/fsa4future/QA-LOG.md` e `tools/build_fsa4future.py`.

## O que já foi feito (06/10/2026, sessão em nuvem)
- Drive: Doc **v1.3** criado em Design System v1 (`FSA4Future_Plataforma_de_Marca_e_Logo_v1.3`, id `1KDXYd-VoJnb0gQ5CiDm39D5DQIgfp8DbP6fHEH_yXhc`) com o nó amarelo #F9DC6B como herança; v1.2 movido para _DELETAR. `readme.md` e `QA-LOG.md` atualizados subidos ao Design System v1 (versões de 29/09 movidas para _DELETAR).
- Repositório: site V1 estático em `fsa4future/` gerado por `tools/build_fsa4future.py` (23 páginas, FSiA, fluxo Conversar → Calendly → "Conversa agendada.", consentimento, schema, sitemap, OG, favicons). QA automatizado em Chromium (1440/1024/390) e axe-core sem violações. Achados QA-001 e QA-003 a QA-016 no `docs/fsa4future/QA-LOG.md`.
- **O pacote `assets/logo/` não estava disponível na nuvem.** O site usa um símbolo provisório de implementação (QA-003), que **não** deve ir ao Drive como logo.

## Tarefas (nesta ordem)

### 1. Logo v0 oficial (fecha A1 e QA-003)
1. Suba `assets/logo/` (SVG) e `assets/logo/export/` (PNG, favicon, ICO, OG, avatar) para o Drive em **Design System v1 / Logo v0** (crie a subpasta `Logo v0` dentro de `13En303ltTwlsrWowHDHqC0xnFDmim8uR`). Confira antes que o nó do cliente é amarelo #F9DC6B com anel petróleo.
2. No repositório, substitua em `fsa4future/assets/logo/`: `fsa4future-simbolo.svg` (positivo), `fsa4future-simbolo-negativo.svg`, `fsa4future-favicon.svg` (núcleo + uma órbita), `favicon-32.png`, `apple-touch-icon.png` (180), `icon-192.png`, `icon-512.png`, `fsa4future-simbolo-512.png`, `fsa4future/favicon.ico` (16/32/48) e `fsa4future/assets/img/og-fsa4future.png` (1200×630). Use os arquivos do v0; se os nomes forem outros, ajuste as referências em `tools/build_fsa4future.py` em vez de renomear o v0.
3. Se o v0 tiver o logo horizontal com nome em contornos, troque o bloco `.logo` do header e do rodapé (em `render()` no gerador) por `<img>` do SVG horizontal positivo/negativo, mantendo `aria-label` e o mínimo de 120 px.
4. Rode `python3 tools/build_fsa4future.py` e registre o fechamento de QA-003 no QA-LOG. No Drive, marque como substituído o LEIA-ME de 06/10 da pasta "Logo F4F para finalizar" (QA-014).

### 2. G1 · navegador e dispositivo (aparelhos reais)
Publique a homologação (GitHub Pages do repositório: `https://catiascan.github.io/fsa4future/`) e teste em Chrome e Edge desktop, Safari iOS e Chrome Android: ícones (QA-001), menu, abas do Hub, trilhas, botão "Fale com a FSiA", painel da FSiA com o teclado aberto (QA-008), ausência de overflow horizontal, menu mobile no Safari (QA-009). Registre cada resultado com aparelho, SO, navegador e versão.

### 3. G2 · acessibilidade
Leitor de tela (NVDA no Windows, VoiceOver no iOS/macOS) nas páginas Home, Hub/frente, etapa do método, Conversar (inclusive erros de validação) e FSiA. Zoom de 200% real. Revisão visual dos tons derivados 700/100 das frentes junto com a FSA (contraste já aprovado em QA-005).

### 4. Canais e conversão (G4) — quando a FSA fornecer
- Preencha `CONFIG` no topo de `fsa4future/assets/js/site.js`: `whatsapp` (WhatsApp Business da FSA⁴Future, nunca número pessoal), `telefone` e `telefoneLabel`. Canal vazio não aparece.
- Calendly: confirme o evento "Conversa de Entendimento FSA — 30 min" (gratuita, Google Meet); crie a **pergunta personalizada 1** (recebe o resumo via `a1`); configure **redirecionar para** `https://fsa4f.com.br/conversar/confirmado/` com **"Pass event details"** ligado (traz `event_start_time`/`event_end_time` para o "Adicionar à agenda").
- Analytics: escolha a ferramenta com a FSA e implemente em `loadAnalytics()` (só após consentimento). Teste os eventos do handoff §19 (já disparados no `dataLayer`): `cta_principal`, `cta_exploratorio`, `fsia_abertura`, `fsia_inicio_conversa`, `fsia_pedido_humano`, `clique_whatsapp`, `clique_email`, `solicitacao_telefone`, `agenda_abertura`, `agendamento_concluido`, `envio_formulario`, `visualizacao_case`, `interacao_metodo`, `visita_hub`.
- Opcional: `CONFIG.formEndpoint` (ex.: Apps Script) para gravar o formulário e mandar cópia a atendimento@.
- Teste ponta a ponta: FSiA → atendimento@ → WhatsApp / e-mail / telefone / agenda → confirmação, com consentimento aceito e recusado.

### 5. Operação (D8)
Siga `docs/fsa4future/operacao-atendimento.md`: domínio no CNPJ da FSA IT4FUTURE, atendimento@ com dois responsáveis + contingência, MFA, SPF/DKIM/DMARC, integração com site, FSiA e Calendly. O e-mail nominal da Cátia só é desligado depois que todos os pontos de contato migrarem.

### 6. G3 · SEO/GEO técnico e go-live
1. Com o acesso ao Search Console/analytics e o inventário do site atual, preencha `docs/fsa4future/migracao-urls.md` e gere os 301 individuais na hospedagem escolhida (Cloudflare Pages, Netlify ou Vercel; GitHub Pages não faz 301).
2. Complete as fichas em `docs/fsa4future/fichas-de-intencao.md` (links de entrada/saída, evidência, responsável, status) editando os dados no gerador.
3. `python3 tools/build_fsa4future.py --prod` e publique `fsa4future/` na raiz de fsa4f.com.br. Valide schema (Rich Results Test), canonical, robots e sitemap; envie o sitemap no Search Console e no Bing Webmaster Tools; configure IndexNow. Meça Core Web Vitals (PageSpeed Insights) nas 5 páginas principais.
4. Só tire o `noindex` de Cases e Conteúdos quando houver o primeiro case autorizado e o primeiro artigo; só tire o aviso de rascunho das políticas depois da leitura jurídica.

### 7. Auditoria final (tarefa 9)
Procure arquivos não referenciados em `fsa4future/` e dependências não usadas; o site não deve carregar nada de terceiros na abertura (Calendly só ao agendar).

## Pendências que dependem da FSA (não invente)
Fotos reais em colaboração e cases autorizados · telefones, WhatsApp Business e ferramenta de agenda · leitura jurídica das políticas · validação da Visão (hoje fora do site) · acesso ao analytics e Search Console e inventário do site atual · nomes do 2º responsável e da contingência do atendimento@.

## Regra de entrega
Ao terminar cada bloco, atualize `docs/fsa4future/QA-LOG.md` (achados QA-###, com ambiente, esperado × observado, evidência e correção), faça commit e push na branch `claude/epic-wright-n7cptm` e informe em uma linha o que foi feito, o que falta e o próximo bloco.
