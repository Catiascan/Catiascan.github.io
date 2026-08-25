# ESTADO — o painel que o JARVIS lê

Este é o arquivo que faz o EVO responder em segundos em vez de minutos.

**A regra:** o modo PULSO lê só este arquivo. Nunca o Drive, nunca os agentes.
Os agentes escrevem aqui quando rodam; o PULSO só lê.

Onde guardar: um Google Doc chamado `FSA — ESTADO` na raiz do Drive, ou este
arquivo no repositório se for usar pelo terminal. Um lugar só. Se existirem
dois, o painel morre.

Formato de cada linha: `indicador | valor | data | fonte | estado`
Estado é uma de: `OK` `ATENCAO` `ALARME` `SEM DADO`

---

## CAIXA

```
Saldo em conta          | R$ ______ | __/__/____ | extrato Nubank PJ    | SEM DADO
Fôlego (dias)           | ___ dias  | __/__/____ | calculado            | SEM DADO
A receber 30d           | R$ ______ | __/__/____ | planilha faturamento | SEM DADO
A pagar 30d             | R$ ______ | __/__/____ | planilha contas      | SEM DADO
Maior cliente (% receita)| ___%     | __/__/____ | planilha faturamento | SEM DADO
```
Alarme: fôlego < 30 dias · maior cliente > 40% · a pagar > a receber + saldo

## COMERCIAL

```
Pipeline ponderado      | R$ ______ | __/__/____ | CRM / planilha       | SEM DADO
Propostas em aberto     | ___       | __/__/____ | CRM                  | SEM DADO
Proposta parada há +14d | ___       | __/__/____ | CRM                  | SEM DADO
POCs em curso           | ___       | __/__/____ | lista de POC         | SEM DADO
POC sem data de fim     | ___       | __/__/____ | lista de POC         | SEM DADO
```
Alarme: qualquer POC sem data de fim, critério de sucesso ou preço de
continuidade · proposta parada há mais de 21 dias

## ENTREGA

```
Projetos ativos         | ___       | __/__/____ | Notion               | SEM DADO
Marco a vencer em 7d    | ___       | __/__/____ | Notion               | SEM DADO
Marco já estourado      | ___       | __/__/____ | Notion               | SEM DADO
Horas alocadas vs capac.| ___%      | __/__/____ | calculado            | SEM DADO
```
Alarme: alocação > 100% · marco estourado sem cliente avisado

## CONTRATO E PRAZO

```
Contrato a renovar 30d  | ___       | __/__/____ | pasta Contratos      | SEM DADO
Trabalho sem escopo escr| ___       | __/__/____ | conferência manual   | SEM DADO
Obrigação fiscal 7d     | ___       | __/__/____ | calendário fiscal    | SEM DADO
```
Alarme: qualquer trabalho em curso sem escopo escrito · obrigação a < 3 dias ·
renovação automática a < 7 dias

## PENDENTE COM TERCEIROS

```
| Com quem | O quê | Desde | Dias parado |
|---|---|---|---|
|  |  |  |  |
```

---

## Como este arquivo se mantém vivo

- **Todo dia, pela Rotina:** o prompt de `02-ROTINA-DIARIA.md` reescreve as
  linhas que consegue ler das fontes automáticas (Drive, Notion, Gmail, agenda).
- **Sempre que um agente de área roda um ESTUDO:** ele atualiza a linha que
  tocou, com data de hoje.
- **Uma vez por semana:** a Cátia preenche à mão o que nenhuma automação lê —
  tipicamente saldo em conta e o quadro de pendências.

Linha com `SEM DADO` há mais de 7 dias vira `ALARME` automaticamente. Painel que
mente por omissão é pior que painel que não existe.
