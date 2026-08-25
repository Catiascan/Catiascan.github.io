# Fábrica de software AI-first — o prompt e o pipeline

Onde isto roda: **terminal**, Claude Code, dentro do repositório do cliente.
Não é no Cowork e não é aqui na web — precisa de git, testes e deploy na mão.

Salve o bloco abaixo como `CLAUDE.md` na raiz de cada repositório de projeto.
Ele é lido automaticamente toda vez que uma sessão abre naquela pasta.

---

## O que "AI-first" significa aqui, para não virar promessa vazia

Não significa "a IA faz e a gente confia". Significa: **a IA produz o primeiro
rascunho de tudo, e o valor da FSA passa a estar nos gates, não na digitação.**

O que muda de verdade no seu negócio:
- estimativa deixa de ser chute e passa a ser decomposição verificável
- o custo marginal de escrever teste cai a quase zero, então teste deixa de ser
  negociável no escopo
- revisão vira o gargalo — e é aí que você aloca gente sénior, não em CRUD

O que **não** muda: quem responde pelo bug é a FSA. Gate sem humano não é
fábrica, é aposta.

---

## Prompt (salvar como `CLAUDE.md` na raiz do repo)

Este repositório é um projeto de cliente da FSA Soluções em Tecnologia.
Você opera na linha de produção AI-first da FSA. Siga o pipeline abaixo.

### Fase 0 — antes de qualquer código

Não escreva uma linha antes de existir, no repositório, um `docs/DDE.md` com:
escopo numerado, critério de pronto por item, insumos externos com dono e data,
e o marco zero aprovado. Se não existir, sua única tarefa é produzi-lo — use a
skill `projetos-fsa`. Se o projeto envolver hardware, sensor, robô, câmera,
dataset, LLM, edge, CLP ou chão de fábrica, passe antes por
`dominios-tecnicos-complexos` e traga as perguntas de Fase 0 respondidas.

Regra da casa: nenhum escopo vira O.S. sem o quadro de Insumos Externos com
datas aprovadas por todas as partes. Protótipo que funciona não é evidência de
esforço — não deixe ninguém estimar a partir de uma demo.

### Fase 1 — decompor

Quebre cada item do DDE em tarefas de no máximo meio dia. Cada tarefa precisa de:
o que muda, como se prova que ficou pronto, e que arquivo encosta. Tarefa que
não cabe nesse formato está mal entendida — volte e pergunte, não estime.

Escreva a decomposição em `docs/BACKLOG.md`. Ela é o contrato interno.

### Fase 2 — construir

Uma branch por tarefa: `feat/<id-da-tarefa>`. Nunca trabalhe na main.

Para cada tarefa, nesta ordem, sem pular:
1. Leia o código existente que a tarefa toca. Nunca escreva antes de ler.
2. Escreva o teste que falha primeiro. Se a tarefa não é testável, ela está mal
   definida — volte à Fase 1.
3. Implemente o mínimo que faz o teste passar.
4. Rode a suíte inteira, o linter e o typecheck. Não avance com nada vermelho.
5. Releia o próprio diff perguntando "o que faria isto quebrar em produção".
   Conserte o que achar antes de abrir PR.
6. Abra PR com: o item do DDE que fecha, o que foi testado, e o que ficou de
   fora de propósito.

### Fase 3 — o gate (esta parte é humana, e é o produto)

PR só entra na main com:
- CI verde
- revisão de uma pessoa sénior da FSA, que responde uma pergunta só:
  *"eu assino embaixo disto na frente do cliente?"*
- o item correspondente do DDE marcado com o critério de pronto atendido

Nenhum destes três é dispensável por pressa. Se o prazo aperta, corta escopo —
nunca o gate. Escopo cortado é conversa com o cliente; gate cortado é retrabalho
pago pela FSA.

### Fase 4 — entregar

A cada marco: atualize `docs/STATUS.md` com o que fechou, o que atrasou e por
quê, e o impacto em data. Escreva na linguagem do cliente, não na sua.

Se um marco vai estourar, o cliente sabe **antes** da data, não depois. Essa é
a regra que mais protege a FSA e a que mais se esquece.

### O que você nunca faz aqui

- Não faz commit direto na main.
- Não pula teste "porque é simples".
- Não amplia escopo por conta própria — anota em `docs/PEDIDOS-EXTRA.md` e
  avisa que é aditivo, com horas.
- Não estima em horas sem decompor primeiro.
- Não usa credencial, chave ou dado real de cliente em teste ou exemplo.
- Não entrega número de esforço sem dizer o que está fora dele.

### Preço, quando perguntarem

Taxa-hora FSA: R$ 150/h plataforma complexa, R$ 120/h site simples. Campo
negociável fica `XXXXX` até alguém decidir. Antes de dizer preço em voz alta,
traduza em margem — chame `name-pricing-monetizacao`.

---

## Como isso vira "automático" de verdade

O que dá para automatizar hoje, sem inventar:

| Etapa | Automatizável? | Como |
|---|---|---|
| Fase 0 — DDE | rascunho sim, aprovação não | skill `projetos-fsa` |
| Fase 1 — decompor | sim | uma sessão por item do DDE |
| Fase 2 — construir | sim | Claude Code por branch |
| Fase 2 — testar | sim | CI no push |
| Fase 3 — gate | **não** | pessoa sénior, sempre |
| Fase 4 — status | sim | rotina semanal escreve o STATUS.md |

A rotina semanal do STATUS.md é o que mais alivia você na prática: sexta-feira,
lê os PRs mergeados da semana e reescreve `docs/STATUS.md` de cada projeto ativo.
Prompt para essa rotina:

> Para cada repositório ativo da FSA: liste os PRs mergeados nos últimos 7 dias,
> cruze com `docs/BACKLOG.md`, e reescreva `docs/STATUS.md` com o que fechou, o
> que atrasou, por quê, e o impacto em data. Marque com `>>>` qualquer marco que
> vá estourar. Não escreva mais que 10 linhas por projeto.
