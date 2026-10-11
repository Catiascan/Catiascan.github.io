# Gestão FSA Hub

App de gestão financeira que substitui a planilha `Budget_FSA_Hub.xlsx`.
Vive como artifact privado no claude.ai, com base de dados própria:

- App: https://claude.ai/artifact/4demuMvq1UgX3Ych8oUjcY (só a dona da conta abre)
- Os dados **não** ficam neste repositório, que é público. `.seed/` e `*.xlsx` estão no `.gitignore`.

## Módulos

| Módulo | Substitui as abas | O que faz |
|---|---|---|
| Painel | Mes_Atual, Painel_Risco, Meta_Crescimento | Visão Mês ou Ano; saldo PJ, quanto falta entrar para fechar as contas, fluxo de caixa projetado até dezembro, ponto de equilíbrio, alertas (sempre a vermelho), próximos vencimentos com código de pagamento |
| Lançamentos | Registro_Diario | Movimento dos extratos com plano de contas único; filtro por mês, banco, grupo; reclassificar numa linha |
| Contas a pagar | Contas_a_Pagar, Custos_Fixos | Estado calculado (atrasada quando vence sem baixa); "Dar baixa" cria o lançamento no extrato |
| Contas a receber | Contas_a_Receber | "Receber" baixa o crédito e cria o lançamento de receita |
| Budget 2026 | Budget_2026 | Grelha editável; totais, resultado e acumulado recalculados; linha de realizado vinda dos lançamentos |
| Métricas | (nova) | MRR, ARR, ticket, churn de clientes e de receita, tempo de vida, LTV, CAC, LTV÷CAC, payback, concentração, receita recorrente × pontual |
| Clientes | Receitas_Esperadas | Funil Prospect → Proposta → Ativo → Encerrado, recebido por cliente |
| Dívidas | Passivo, parcelas | Passivo por fase e parcelas de tributos/empréstimos em aberto |
| Planilha original | todas as 24 abas | Cópia só de leitura, tal como estavam na importação |

## Base de dados (coleções)

- `lancamentos/rd-NNNN` — `data, mes, banco, descricao, valor (negativo = saída), grupo, sub, categoria_original, modo, cliente, tag, recorrente (bool; ausente = pontual), origem`
- `pagar/cp-NNNN` — `vencimento, mes, descricao, categoria, previsto, conta, baixa, pago, estado, codigo, no_registro, obs` (sem `codigo`, o app procura o código de barras nas obs). `conta` = de onde sai o pagamento, sempre um destes: Inter PJ, Itau PJ, Itau PJ FSA4Future (em abertura), Inter PF Catia, PF Fernando, Cartao Mercado Livre (Fernando), Cartao Daise, Cartao de credito, A definir. A assinatura do Claude vai no cartão Mercado Livre do Fernando: é custo da PJ, a baixa fica "PAGO PF - RESTITUIR" e conta no fluxo da PJ (o nome não leva "PF" de propósito). O cartão da Daise é o crédito que a empresa usa por não ter cartão próprio: só valores altos (refinanciamento e conserto do carro) e mensalidades de rotina da empresa que só aceitam crédito. Tudo que passa nele é custo da PJ, que reembolsa a Daise
- `receber/cr-NNNN` — `devedor, total, ja_pago, aberto, previsto, estado, baixa, obs`
- `budget/b-NN` — `secao, item, ordem, meses[12]`
- `clientes/cli-<nome>` — `nome, status, tipo (Recorrente | Projeto fechado), caixa_pj (bool), inicio/fim (aaaa-mm), valor_mensal | previsto{mai..dez}, contato, obs`
- `passivo/pv-NN` — `divida, direcao, fase, original, negociavel, status, obs`
- `config/geral` — `saldo_pj, saldo_piso, saldo_obs, saldo_data, fonte, importado_em, prolabore_meta, mkt_palavra, mkt_percentual, mkt_desde, investimento_comercial, metricas_periodo, margem_contribuicao`
- `abas/<aba>` — cópia fiel de cada aba (`linhas: [{c: [...]}]`)

O NNNN dos ids é a linha da planilha de origem; registos criados no app têm id gerado e `origem: "app"`.

## Plano de contas dos lançamentos

Receita · Outras entradas · Rendimento/Aplicação · Custo fixo · Custo variável · Transporte · Tributos ·
Bancário · Comissões · Empréstimos · Pró-labore · Adiantamento a sócio · Pessoal (PF) · Transferência ·
Estorno · A classificar.

Transferência, Estorno e Rendimento/Aplicação ficam fora do "realizado" (não são operação).
As 45 grafias de categoria da planilha foram mapeadas por `tools/gestao_fsa/convert.py`; o que não deu
para mapear ficou em **A classificar** (36 na importação de 11/10/2026).

## Fórmulas

- **Falta entrar para fechar as contas** = contas a pagar em aberto até dezembro − saldo PJ de hoje.
- **Fluxo projetado**: entradas = clientes ativos com `caixa_pj` (no mês atual, menos a receita já recebida); saídas = contas em aberto que saem de conta PJ, com as atrasadas no mês atual. Contas pagas pela PF (escola, van, ballet) ficam fora, porque saem do pró-labore, que já é saída da PJ. Contas a receber ficam fora até caírem no extrato.
- **Ponto de equilíbrio** = custos orçados do mês + `prolabore_meta` (R$ 6.000) quando o mês não tem pró-labore orçado. É a mesma conta da linha "Break-even c/ pró-labore ATUAL" da planilha.
- **Churn** = clientes perdidos ÷ clientes-mês ativos no período; **tempo de vida** = 1 ÷ churn; **LTV** = ticket × margem × tempo de vida; **CAC** = investimento comercial ÷ clientes novos desde `mkt_desde`. O investimento vem das contas a pagar: `mkt_percentual`% das contas cuja descrição contém `mkt_palavra` (hoje 10% da assinatura Anthropic, desde 2026-08), mais `investimento_comercial` manual. Cliente sem `inicio` conta como já existente antes do período.

## Como o Claude opera o app

Numa sessão do Claude, a Cátia pode pedir em linguagem natural, por exemplo:

- "Paguei o aluguel hoje pelo Itaú, 8.236,26" → baixa em `pagar` + lançamento em `lancamentos`
- "Chegou o extrato do Inter de ontem" (com o ficheiro) → lançamentos novos, conferidos contra o que já existe
- "Saldo PJ hoje: Inter 12.000, Itaú 3.000" → `config/geral.saldo_pj`
- "O que vence esta semana?" / "Como estamos contra o budget em setembro?" → leitura e resposta

Os extratos ficam no Google Drive da Cátia, pasta **Extratos** (dentro da pasta do financeiro), em PDF, CSV ou TXT por conta (Inter PJ, Inter PF, Itaú PJ). Antes de dar baixa ou corrigir um valor duvidoso, o Claude confere ali.

A Educbank vem em 4 boletos por mês: mensalidade e material da Sophia e da Nina. Escola, van e ballet são pagos pelo Inter PF da Cátia; a baixa de despesa pessoal pela PF fica PAGO (não "restituir"). A rematrícula de outubro sai da PJ.

O Claude escreve com a ferramenta `ArtifactData` no URL acima, sempre fixando `if_version`
do documento lido, para não pisar alterações feitas no app.

## Reimportar a planilha

Só se for preciso recomeçar do zero (apaga o trabalho feito no app):

```
python3 -I tools/gestao_fsa/convert.py Budget_FSA_Hub.xlsx .seed
```

Gera um JSON por documento e `manifest.json` com lotes de 50 writes para o `ArtifactData batch`.
