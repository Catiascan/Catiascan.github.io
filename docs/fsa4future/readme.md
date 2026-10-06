# FSA⁴Future — Design System v1.1 (congelado) e site V1

**FSA⁴Future · Technology & Business Hub**, o rebranding da FSA Soluções em Tecnologia (+20 anos em consultoria e tecnologia).
Assinatura: **Technology 4 what's next.** · Frase de campanha: **Ideias em movimento. Impacto no futuro.**

Atualizado em 06/10/2026. Substitui o README do Design System v1 de 29/09 (que ainda usava "FSA 4 Future · Technology Hub" e dizia que não havia logo).

## Decisões fechadas (não reabrir nesta fase)
- **Nome:** FSA⁴Future em tudo. Frentes: FSA⁴Flow, FSA⁴Partners, FSA⁴Solutions, FSA⁴Products. IA, cloud, dados, automação, integrações e segurança são capacidades transversais, não submarcas.
- **Descritor:** Technology & Business Hub.
- **Cores:** Deep Petrol #073B4C (institucional) · Graphite #111820 · Copper #C06F42 (acento humano e CTA; o botão usa #A85C34) · Sand #E8DFD3 · Off White #F8F6F1. Frentes: Flow #4F7D52, Partners #B9683D, Solutions #247A8B, Products #65439B (700 e 100 derivados e provisórios; passaram no contraste, falta revisão visual). Acentos premium: Champagne #D4C3A3 e Prata #C0C0C6. Herança: amarelo FSA #F9DC6B, exclusivo do nó do cliente no logo.
- **Tipografia:** Montserrat 400/500/600/700.
- **Logo:** vetor provisório v0 (CEO, 06/10/2026): núcleo, duas órbitas abertas, nós e o nó amarelo do cliente com anel petróleo. Revisão do Fernando em QA-002. Plataforma e parecer: Doc v1.3 no Drive (`FSA4Future_Plataforma_de_Marca_e_Logo_v1.3`).
- **Método:** 01 OUVIR → 02 ENTENDER → 03 CONECTAR → 04 CONSTRUIR → 05 VALIDAR → 06 EVOLUIR.
- **Voz:** "problema" nas falas institucionais e de método; **"desafio"** sempre que falar com o cliente. "Qual desafio precisamos resolver juntos?", nunca "Qual é o seu problema?". Sem emoji, sem métrica inventada, sem prazo nem SLA prometido, NPS 70 como "NPS 70".
- **Escopo:** nenhuma funcionalidade nova. Ideias vão para o backlog do `QA-LOG.md`, exceto acessibilidade, segurança, SEO/GEO ou conversão.

## Onde está cada coisa neste repositório
| Caminho | O quê |
|---|---|
| `fsa4future/` | Site V1 estático gerado (pronto para subir na raiz de fsa4future.com.br). Homologação: `https://catiascan.github.io/fsa4future/` |
| `tools/build_fsa4future.py` | Gerador (Python 3.12+, sem dependências). Conteúdo, metadados, schema e fichas ficam aqui. `--prod` gera a versão indexável |
| `fsa4future/assets/css/site.css` | Tokens + componentes do DS v1.1 num arquivo; blocos `IMPL QA-###` são ajustes de implementação |
| `fsa4future/assets/js/site.js` | Menu, consentimento + eventos, FSiA, fluxo Conversar, confirmação. `CONFIG` no topo concentra canais pendentes |
| `fsa4future/assets/icons/sprite.svg` | 28 ícones Lucide 0.460.0 auto-hospedados (QA-001) |
| `fsa4future/assets/fonts/` | Montserrat woff2 auto-hospedada (OFL) — sem Google Fonts, por LGPD e performance |
| `fsa4future/assets/logo/` | Logo v0 oficial (06/10/2026), com os nomes do v0: lockup do header e do rodapé, símbolo, favicons. Revisão óptica: QA-002 |
| `docs/fsa4future/QA-LOG.md` | Achados QA-###, pendências por gate e backlog |
| `docs/fsa4future/fichas-de-intencao.md` | Ficha por URL (gerada) |
| `docs/fsa4future/migracao-urls.md` | Modelo do mapa de migração 301 |
| `docs/fsa4future/operacao-atendimento.md` | Checklist do atendimento@ (D8) e DNS |
| `docs/fsa4future/PROMPT-terminal.md` | Prompt para o terminal concluir o que ficou pendente |

## Site V1 — páginas
Home · Desafios · Como fazemos (+ 6 etapas com anterior/próxima) · Hub (+ 4 frentes, com abas entre elas) · Programa de Parceiros (página pública) · Cases · Sobre · Conteúdos · Conversar (+ confirmação) · Política de Privacidade · Política de Cookies · 404.
Cases e Conteúdos estão `noindex` até ter o primeiro case autorizado e o primeiro artigo. As políticas estão `noindex` e marcadas como rascunho até a leitura jurídica.

## FSiA
Roteiro fechado a partir da `FSiA_Base_de_Conhecimento_v1` (sem modelo de linguagem nesta fase, o que garante os limites): abertura e 4 opções; até 5 perguntas do OUVIR, uma por vez; sugestão de frente sempre como "sugestão, não diagnóstico"; respostas fixas para preço, prazo, viabilidade, dados sensíveis, vagas, privacidade e tentativa de mudar as regras; handoff humano a qualquer momento por agenda, WhatsApp, e-mail ou telefone. O resumo da conversa só vai junto se a pessoa disser "sim" — no link do WhatsApp, no corpo do e-mail ou como resposta 1 no Calendly. Não cita prazo de resposta.

## Conversa → agenda → confirmação
Desafio → dados (com autorização LGPD, nenhuma caixa pré-marcada) → canal → Calendly embutido ("Conversa de Entendimento FSA — 30 min", gratuita) → "Conversa agendada." com **Adicionar à agenda** (.ics e Google Agenda). Para mostrar data e hora na confirmação, o evento do Calendly precisa redirecionar para `/conversar/confirmado/` repassando os detalhes do evento. Sem isso, a confirmação aparece sem horário e orienta usar o convite enviado por e-mail.

## Consentimento e analytics
Aviso com Aceitar, Recusar e Escolher com o mesmo destaque; escolha registrada com data e versão; link "Preferências de cookies" no rodapé. Eventos do funil do handoff §19 já disparam para `window.dataLayer` **só com consentimento de análise**; a ferramenta de analytics ainda não foi escolhida (`loadAnalytics()` em `site.js`).

## SEO/GEO técnico
Um H1 por página, títulos e descrições exclusivos, canonical absoluto em https://fsa4future.com.br, Open Graph/Twitter com OG 1200×630, trilhas com `BreadcrumbList`, `Organization` (legalName, taxID, logo, e-mail), `WebSite`, `Service` nas frentes, `AboutPage` e `ContactPage`. Sitemap só com URLs canônicas indexáveis; robots com `Disallow: /parceiros/` em produção. Em homologação todas as páginas são `noindex, nofollow`.

## Auditoria de dependências e arquivos (tarefa 9)
- Zero dependências de execução de terceiros na carga das páginas (fontes, ícones, CSS e JS locais). Calendly só carrega quando a pessoa escolhe agendar.
- Sem framework, sem build de JS, sem `node_modules` no repositório. O gerador usa só a biblioteca padrão do Python.
- Licenças incluídas: `assets/fonts/LICENSE-Montserrat-OFL.txt`, `assets/icons/LICENSE-lucide.txt`.
- Repetir antes do go-live: remover o que o v0 oficial tornar obsoleto em `assets/logo/` e conferir referências quebradas (o QA automatizado já falha em qualquer 404).

## Build e publicação
```bash
python3 tools/build_fsa4future.py          # homologação (noindex)
python3 tools/build_fsa4future.py --prod   # produção: indexável, robots/sitemap para a raiz
```
Em produção, publicar o conteúdo de `fsa4future/` na raiz de fsa4future.com.br numa hospedagem que aceite redirects 301 por URL (Cloudflare Pages, Netlify ou Vercel; GitHub Pages não faz 301). O `404.html` de produção usa caminhos a partir de `/`.
