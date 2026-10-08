# Prompt — FSA⁴Future · concluir pendências no Claude Code (terminal)

Cole o texto abaixo no `claude`, **dentro da pasta onde você descompactou o pacote do design system** (a que tem `SKILL.md`, `assets/logo/` e `guidelines/Plataforma_e_Parecer_Logo.md`), com o repositório `Catiascan/Catiascan.github.io` clonado ao lado (branch `claude/epic-wright-n7cptm`).

---

Você é o responsável técnico pelo pré-lançamento da **FSA⁴Future · Technology & Business Hub**. O Design System v1.1 está **congelado**: não reabra marca, posicionamento, arquitetura, método, cores nem estratégia SEO/GEO. Todo achado é primeiro um problema de implementação e vai para o `QA-LOG.md` no formato QA-###.

Antes de agir, leia: `SKILL.md`, `readme.md`, `QA-LOG.md`, `guidelines/Plataforma_e_Parecer_Logo.md` (no pacote) e, no repositório, `docs/fsa4future/readme.md`, `docs/fsa4future/QA-LOG.md` e `tools/build_fsa4future.py`.

## O que já foi feito (até 08/10/2026)
- Drive: Doc **v1.3** (Plataforma de Marca e Logo) em Design System v1, com o nó amarelo #F9DC6B como herança; v1.2 em _DELETAR. README e QA-LOG atualizados no Design System v1. **Logo v0 completo** (SVG + `export/`) em Design System v1 / Logo v0. LEIA-ME antigo da pasta "Logo F4F para finalizar" marcado como substituído (QA-014).
- Repositório: site V1 estático em `fsa4future/` gerado por `tools/build_fsa4future.py` (23 páginas, FSiA, fluxo Conversar → Calendly → "Conversa agendada.", consentimento, schema, sitemap, OG, favicons). **Logo v0 oficial aplicado** (QA-003 fechado). **Domínio fsa4future.com.br** (QA-017). Gerador compatível com Windows (QA-018). **Contatos provisórios da FSA** no site: (12) 3351-9958 e catia@fsasolucoes.com.br (QA-019). **Visão publicada** na página Sobre (QA-016).
- Calendly: evento "Conversa de Entendimento FSA — 30 min", gratuito, Google Meet, pergunta 1 recebendo o resumo e redirect de homologação conferido. No go-live, trocar o redirect para `https://fsa4future.com.br/conversar/confirmado/`.
- QA automatizado em Chromium (1440/1024/390) e axe-core sem violações, revalidado em 07/10 após as mudanças do terminal. Achados QA-001 a QA-019 no `docs/fsa4future/QA-LOG.md`.
- Políticas: leitura jurídica preliminar feita (doc no Drive, 07/10), à espera do advogado.

## Tarefas (nesta ordem)

### 1. Logo v0 — feito
Aplicado no site e subido ao Drive em 06/10 (QA-003). A revisão óptica segue com o Fernando (QA-002): ⁴, espessura das órbitas a 48 px, espaçamento, AI e PDF editáveis, substituindo os arquivos com os mesmos nomes. Quando chegar, copie para `fsa4future/assets/logo/` e rode o build.

### 2. G1 · navegador e dispositivo (aparelhos reais)
Publique a homologação (GitHub Pages do repositório: `https://catiascan.github.io/fsa4future/`) e teste em Chrome e Edge desktop, Safari iOS e Chrome Android: ícones (QA-001), menu, abas do Hub, trilhas, botão "Fale com a FSiA", painel da FSiA com o teclado aberto (QA-008), ausência de overflow horizontal, menu mobile no Safari (QA-009). Registre cada resultado com aparelho, SO, navegador e versão.

### 3. G2 · acessibilidade
Leitor de tela (NVDA no Windows, VoiceOver no iOS/macOS) nas páginas Home, Hub/frente, etapa do método, Conversar (inclusive erros de validação) e FSiA. Zoom de 200% real. Revisão visual dos tons derivados 700/100 das frentes junto com a FSA (contraste já aprovado em QA-005).

### 4. Canais e conversão (G4) — quando a FSA fornecer
- Troque os contatos **provisórios** do `CONFIG` em `fsa4future/assets/js/site.js` e do `EMAIL` em `tools/build_fsa4future.py` (QA-019) pelos canais próprios da FSA⁴Future: WhatsApp Business (nunca número pessoal), telefone e atendimento@fsa4future.com.br. Canal vazio não aparece.
- Calendly: já configurado em homologação. No go-live, troque o redirect para `https://fsa4future.com.br/conversar/confirmado/` com "Pass event details" ligado.
- Analytics: escolha a ferramenta com a FSA e implemente em `loadAnalytics()` (só após consentimento). Teste os eventos do handoff §19 (já disparados no `dataLayer`): `cta_principal`, `cta_exploratorio`, `fsia_abertura`, `fsia_inicio_conversa`, `fsia_pedido_humano`, `clique_whatsapp`, `clique_email`, `solicitacao_telefone`, `agenda_abertura`, `agendamento_concluido`, `envio_formulario`, `visualizacao_case`, `interacao_metodo`, `visita_hub`.
- Opcional: `CONFIG.formEndpoint` (ex.: Apps Script) para gravar o formulário e mandar cópia a atendimento@.
- Teste ponta a ponta: FSiA → atendimento@ → WhatsApp / e-mail / telefone / agenda → confirmação, com consentimento aceito e recusado.

### 5. Operação (D8)
Siga `docs/fsa4future/operacao-atendimento.md`: domínio fsa4future.com.br (Locaweb, CNPJ da FSA IT4FUTURE; DNS ainda sem MX/TXT), atendimento@fsa4future.com.br com dois responsáveis + contingência, MFA, SPF/DKIM/DMARC, integração com site, FSiA e Calendly. O e-mail nominal da Cátia só é desligado depois que todos os pontos de contato migrarem.

### 6. G3 · SEO/GEO técnico e go-live
1. Com o acesso ao Search Console/analytics e o inventário do site atual, preencha `docs/fsa4future/migracao-urls.md` e gere os 301 individuais na hospedagem escolhida (Cloudflare Pages, Netlify ou Vercel; GitHub Pages não faz 301).
2. Complete as fichas em `docs/fsa4future/fichas-de-intencao.md` (links de entrada/saída, evidência, responsável, status) editando os dados no gerador.
3. `python3 tools/build_fsa4future.py --prod` e publique `fsa4future/` na raiz de fsa4future.com.br. Valide schema (Rich Results Test), canonical, robots e sitemap; envie o sitemap no Search Console e no Bing Webmaster Tools; configure IndexNow. Meça Core Web Vitals (PageSpeed Insights) nas 5 páginas principais.
4. Só tire o `noindex` de Cases e Conteúdos quando houver o primeiro case autorizado e o primeiro artigo; só tire o aviso de rascunho das políticas depois da leitura jurídica.

### 7. Auditoria final (tarefa 9)
Procure arquivos não referenciados em `fsa4future/` e dependências não usadas; o site não deve carregar nada de terceiros na abertura (Calendly só ao agendar).

## Pendências que dependem da FSA (não invente)
Fotos reais em colaboração e cases autorizados (ainda sem autorização) · WhatsApp Business e telefone próprios da FSA⁴Future · criação do atendimento@fsa4future.com.br (à espera do Fernando) · resposta do advogado sobre as políticas · acesso ao analytics e Search Console e inventário do site atual (provavelmente com o Fernando) · nomes do 2º responsável e da contingência do atendimento@ · revisão óptica do logo (QA-002, Fernando).

## Regra de entrega
Ao terminar cada bloco, atualize `docs/fsa4future/QA-LOG.md` (achados QA-###, com ambiente, esperado × observado, evidência e correção), faça commit e push na branch `claude/epic-wright-n7cptm` e informe em uma linha o que foi feito, o que falta e o próximo bloco.
