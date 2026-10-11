# Gestão FSA Hub

App de gestão financeira que substitui a planilha `Budget_FSA_Hub.xlsx`.
Vive como artifact privado no claude.ai, com base de dados própria:

- App: https://claude.ai/artifact/4demuMvq1UgX3Ych8oUjcY (só a dona da conta abre)
- Os dados **não** ficam neste repositório, que é público. `.seed/` e `*.xlsx` estão no `.gitignore`.

## Módulos

| Módulo | Substitui as abas | O que faz |
|---|---|---|
| Painel | Mes_Atual, Painel_Risco | Saldo PJ, contas em aberto do mês, saldo projetado contra o piso, atrasadas, alertas, gráfico budget × realizado |
| Lançamentos | Registro_Diario | Movimento dos extratos com plano de contas único; filtro por mês, banco, grupo; reclassificar numa linha |
| Contas a pagar | Contas_a_Pagar, Custos_Fixos | Estado calculado (atrasada quando vence sem baixa); "Dar baixa" cria o lançamento no extrato |
| Contas a receber | Contas_a_Receber | "Receber" baixa o crédito e cria o lançamento de receita |
| Budget 2026 | Budget_2026 | Grelha editável; totais, resultado e acumulado recalculados; linha de realizado vinda dos lançamentos |
| Clientes | Receitas_Esperadas | Funil Prospect → Proposta → Ativo → Encerrado, recebido por cliente |
| Dívidas | Passivo, parcelas | Passivo por fase e parcelas de tributos/empréstimos em aberto |
| Planilha original | todas as 24 abas | Cópia só de leitura, tal como estavam na importação |

## Base de dados (coleções)

- `lancamentos/rd-NNNN` — `data, mes, banco, descricao, valor (negativo = saída), grupo, sub, categoria_original, modo, cliente, tag, origem`
- `pagar/cp-NNNN` — `vencimento, mes, descricao, categoria, previsto, conta, baixa, pago, estado, no_registro, obs`
- `receber/cr-NNNN` — `devedor, total, ja_pago, aberto, previsto, estado, baixa, obs`
- `budget/b-NN` — `secao, item, ordem, meses[12]`
- `clientes/cli-<nome>` — `nome, status, valor_mensal | previsto{mai..dez}, contato, obs`
- `passivo/pv-NN` — `divida, direcao, fase, original, negociavel, status, obs`
- `config/geral` — `saldo_pj, saldo_piso, saldo_obs, saldo_data, fonte, importado_em`
- `abas/<aba>` — cópia fiel de cada aba (`linhas: [{c: [...]}]`)

O NNNN dos ids é a linha da planilha de origem; registos criados no app têm id gerado e `origem: "app"`.

## Plano de contas dos lançamentos

Receita · Outras entradas · Rendimento/Aplicação · Custo fixo · Custo variável · Transporte · Tributos ·
Bancário · Comissões · Empréstimos · Pró-labore · Adiantamento a sócio · Pessoal (PF) · Transferência ·
Estorno · A classificar.

Transferência, Estorno e Rendimento/Aplicação ficam fora do "realizado" (não são operação).
As 45 grafias de categoria da planilha foram mapeadas por `tools/gestao_fsa/convert.py`; o que não deu
para mapear ficou em **A classificar** (36 na importação de 11/10/2026).

## Como o Claude opera o app

Numa sessão do Claude, a Cátia pode pedir em linguagem natural, por exemplo:

- "Paguei o aluguel hoje pelo Itaú, 8.236,26" → baixa em `pagar` + lançamento em `lancamentos`
- "Chegou o extrato do Inter de ontem" (com o ficheiro) → lançamentos novos, conferidos contra o que já existe
- "Saldo PJ hoje: Inter 12.000, Itaú 3.000" → `config/geral.saldo_pj`
- "O que vence esta semana?" / "Como estamos contra o budget em setembro?" → leitura e resposta

O Claude escreve com a ferramenta `ArtifactData` no URL acima, sempre fixando `if_version`
do documento lido, para não pisar alterações feitas no app.

## Reimportar a planilha

Só se for preciso recomeçar do zero (apaga o trabalho feito no app):

```
python3 -I tools/gestao_fsa/convert.py Budget_FSA_Hub.xlsx .seed
```

Gera um JSON por documento e `manifest.json` com lotes de 50 writes para o `ArtifactData batch`.
