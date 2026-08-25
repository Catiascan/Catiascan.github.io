# Agentes no menu do Cowork

## O que dá e o que não dá

O menu da esquerda do Cowork Desktop tem seções fixas — Artefatos, Rotinas,
Personalizar, Projetos. Essas seções são do aplicativo: não dá para criar uma
nova ao lado delas, nem eu nem você.

O que dá, e resolve o mesmo problema: **Projetos**. Cada projeto aparece nomeado
no menu, com instruções, contexto e memória próprios. Então a pasta de agentes é
um projeto chamado `Agentes` — e as instruções dele fazem o papel do
orquestrador: você escreve em português normal, ele escolhe o agente e diz qual
escolheu, para você ir aprendendo os nomes sem decorar.

Onde cada coisa do seu pedido cai:

| Você pediu | Onde vive de verdade |
|---|---|
| pasta dos agentes no menu | projeto `Agentes` (seção Projetos) |
| orquestrador | campo Instruções desse projeto |
| ver a lista de agentes | Personalizar → Skills |
| EVO da manhã automático | Rotinas |

## Passo a passo — caminho curto (recomendado)

1. Abra o Cowork no Desktop. No painel esquerdo, seção **Projetos**, clique em
   novo projeto.
2. Escolha **começar do zero** (as outras opções são importar do claude.ai ou
   apontar para uma pasta do computador — nenhuma é necessária aqui).
3. Nome: `Agentes`
4. Abra o campo **Instruções** e cole tudo o que está abaixo do traço em
   [`00-agentes-orquestrador/INSTRUCOES.md`](00-agentes-orquestrador/INSTRUCOES.md).
5. Salve.

**Teste:** clique em `Agentes` e escreva só `fechamento`. Se ele responder
dizendo que está usando `evo-diario` e abrir o status com os alarmes primeiro,
sem perguntar nada, a instrução pegou.

Pronto — uma pasta no menu, todos os agentes atrás dela.

## Caminho longo — oito pastas separadas

Se um dia quiser as frentes separadas no menu (útil quando cada uma tiver
memória e ficheiros próprios), as oito estão prontas aqui, cada uma com seu
bloco de instruções para colar:

| Pasta | Nome do projeto | Agentes |
|---|---|---|
| `01-fsa-evo-painel` | `FSA · Evo / Painel` | evo-diario, painel-fsa, presidencia-fsa |
| `02-fsa-financeiro` | `FSA · Financeiro` | financeiro-fsa, contabil-fsa, name-pricing-monetizacao |
| `03-fsa-juridico` | `FSA · Jurídico` | juridico-fsa, advogado-pi |
| `04-fsa-comercial` | `FSA · Comercial` | comercial-fsa, poc-para-contrato, pitch-deck-investidor, fsa-starmeta-dde-proposta |
| `05-fsa-projetos-pmo` | `FSA · Projetos / PMO` | projetos-fsa, pmo-portfolio-agil, dominios-tecnicos-complexos |
| `06-fsa-marketing` | `FSA · Marketing` | marketing-fsa, marketing-sea |
| `07-sea` | `S.E.A.` | sea-analise-de-produto, sea-template-interativo |
| `08-rotina` | `Rotina` | morning, evo-diario |

Mesmo processo: novo projeto → começar do zero → nome exato da coluna do meio →
colar o bloco de instruções do `INSTRUCOES.md` da pasta.

Os dois caminhos convivem. Dá para ter o `Agentes` como porta de entrada e
abrir uma pasta separada só para a frente que ficar pesada.

## O que você precisa saber antes de mexer

- Projetos do Cowork são **só do Desktop**, salvos localmente, sem sincronizar.
  Não organizam o histórico do claude.ai web.
- A skill precisa existir no Desktop. `pmo-portfolio-agil` hoje está só na web —
  copie antes, senão a camada de carteira fica capenga.
- Enquanto não montar nada: chamar pelo nome já funciona em qualquer lugar.
  "usa a skill juridico-fsa" no meio da conversa resolve, sem pasta nenhuma.
- Se o Cowork abrir em tela branca (bug conhecido na sua máquina): mate o
  processo no Gerenciador de Tarefas e limpe o cache em `%APPDATA%\Claude`.

Se algum passo não bater com o que aparece na sua tela — principalmente o passo
1 ou o 4 — me descreva o que você vê que eu oriento dali.
