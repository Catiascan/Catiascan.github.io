# JARVIS — acompanhamento de CEO que roda sozinho

## O diagnóstico, primeiro

Você tentou resolver com prompt duas coisas que prompt não resolve.

**Por que o EVO demora uma vida.** A skill manda ler a fonte no Drive e chamar
os departamentos. Cada execução vira uma busca no Drive, depois 3 a 5 agentes, e
cada um busca de novo. São dezenas de leituras para responder "como estamos".
A correção não é escrever melhor: é ele ler **um arquivo só, já calculado**.
Isso é o `FSA — ESTADO`, e é a peça central de tudo aqui.

**Por que nada é automático.** Automático precisa de três peças e você tinha só
a do meio:

```
gatilho  →  instrução  →  destino
(Rotina)    (o prompt)    (onde a resposta aparece)
```

Prompt não acorda sozinho. Sem Rotina configurada, ele espera para sempre.

## Os arquivos

| Arquivo | O que é | Onde vai |
|---|---|---|
| `00-JARVIS.md` | o orquestrador — três modos, roteamento, regras | Instruções do projeto `JARVIS` |
| `01-ESTADO.md` | o painel que faz o boletim ser instantâneo | doc `FSA — ESTADO` no Drive |
| `02-ROTINA-DIARIA.md` | o prompt que roda às 7h sem você abrir nada | Rotinas |
| `03-FABRICA-SOFTWARE.md` | pipeline AI-first + prompt de repo | `CLAUDE.md` de cada projeto |
| `04-CICLO-COMPLETO.md` | os três anéis e a ordem de execução | ler uma vez |
| `bin/instalar-fabrica.sh` | cria docs/ e CLAUDE.md num repo | terminal |

## O truque dos três modos

É o que conserta a lentidão. Todo pedido cai num dos três, e o JARVIS decide
sozinho qual é:

- **PULSO** — "como estamos", "boletim". Lê só o `FSA — ESTADO`. Segundos.
- **ESTUDO** — "por que", "analisa", "monta". Aí sim chama o agente da área. E
  ao terminar, escreve o número novo de volta no painel.
- **DECISÃO** — as áreas se contradizem. Chama `presidencia-fsa`, devolve uma
  recomendação assumida.

O painel se mantém vivo porque todo ESTUDO o alimenta. Ninguém preenche à mão
além das cinco linhas iniciais.

## Comece por aqui

```
1. Criar o doc FSA — ESTADO no Drive, preencher 5 linhas    (15 min, uma vez)
2. Criar o projeto JARVIS no Cowork com 00-JARVIS.md        (5 min)
3. Testar: "roda o boletim agora"                           (tem que ser rápido)
4. Ligar a Rotina diária 07:00                              (5 min)
```

Esses quatro dão o acompanhamento de CEO funcionando. A fábrica de software
(`03`) e o fecho semanal podem esperar uma semana — o painel precisa de alguns
dias de dado real antes de valer alguma coisa.

## O que continua não sendo automático, e nem deve ser

- O **gate** da fábrica de software. PR só entra na main com uma pessoa sénior
  respondendo "eu assino embaixo disto na frente do cliente?". Gate sem humano
  não é fábrica, é aposta.
- As cinco linhas do painel que nenhuma ferramenta lê — saldo em conta e o
  quadro de pendências com terceiros. Uma vez por semana, na mão.
- Aprovar o DDE. Rascunho a IA faz; assinatura é sua.
