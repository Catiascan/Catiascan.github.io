# O ciclo completo — comandos, não intenções

Três anéis. Cada um tem gatilho, instrução e destino. Se faltar uma das três,
não roda — foi sempre isso que quebrou.

| Anel | Gatilho | Instrução | Destino |
|---|---|---|---|
| Diário | Rotina 07:00 dias úteis | `02-ROTINA-DIARIA.md` | boletim + `FSA — ESTADO` reescrito |
| Semanal | Rotina sexta 17:00 | bloco "semanal" abaixo | `docs/STATUS.md` de cada projeto |
| Sob demanda | você digita | `00-JARVIS.md` | resposta em PULSO / ESTUDO / DECISÃO |

---

## Anel 1 — diário (o que resolve o "demora uma vida")

### 1.1 Criar o painel, uma vez só

No Drive, crie um documento chamado exatamente `FSA — ESTADO` e cole dentro o
conteúdo de `01-ESTADO.md`. Preencha à mão, hoje, só estas cinco linhas:

- Saldo em conta
- A receber 30d
- A pagar 30d
- Maior cliente (% receita)
- O quadro PENDENTE COM TERCEIROS

O resto a rotina preenche. Cinco linhas: quinze minutos, uma vez.

### 1.2 Ligar a rotina

Cowork Desktop → menu esquerdo → **Rotinas** → nova rotina →
colar o prompt de `02-ROTINA-DIARIA.md` → 07:00 → seg a sex.

Se preferir que rode aqui na web (roda mesmo com o computador desligado), me
peça: "arma a rotina diária às 7h" e eu crio.

### 1.3 Testar hoje, sem esperar amanhã

Abra o projeto `JARVIS` e escreva: `roda o boletim agora`.
Se demorar mais que 20 segundos, ele está indo ao Drive em vez de ler o painel —
responda "leia só o FSA — ESTADO" e a instrução corrige.

---

## Anel 2 — semanal

Rotina, sexta-feira 17:00, com este prompt:

> Você é o JARVIS. Fecho de semana da FSA, execução automática.
>
> 1. Para cada projeto ativo em `docs/BACKLOG.md` de cada repositório: liste os
>    PRs mergeados nos últimos 7 dias, cruze com o backlog, e reescreva
>    `docs/STATUS.md` com o que fechou, o que atrasou, por quê, e o impacto em
>    data. Máximo 10 linhas por projeto. Marque `>>>` em marco que vai estourar.
> 2. Atualize no `FSA — ESTADO` as linhas de ENTREGA: projetos ativos, marcos a
>    vencer em 7 dias, marcos estourados, alocação vs capacidade.
> 3. Devolva uma única mensagem: os `>>>` da semana e uma decisão para segunda.
>    Se não houver `>>>`, escreva "semana limpa" e a decisão mesmo assim.
>
> Não escreva proposta, não abra projeto, não analise área. Só o fecho.

---

## Anel 3 — sob demanda

Projeto Cowork chamado `JARVIS`, instruções = `00-JARVIS.md` inteiro.
É a porta de entrada. Você escreve português normal, ele escolhe o modo.

---

## Instalação num repositório de projeto (terminal)

```bash
# 1. entrar no repo do cliente
cd ~/projetos/<cliente>

# 2. estrutura mínima da fábrica
mkdir -p docs
touch docs/DDE.md docs/BACKLOG.md docs/STATUS.md docs/PEDIDOS-EXTRA.md

# 3. instalar o prompt da fábrica (bloco de 03-FABRICA-SOFTWARE.md)
#    copie o bloco "Prompt (salvar como CLAUDE.md)" para:
$EDITOR CLAUDE.md

# 4. conferir que a sessão lê o prompt
claude
# depois, dentro da sessão:  /init   (confirma que o CLAUDE.md foi carregado)

# 5. primeira tarefa sempre
#    "leia docs/DDE.md e decomponha o item 1 em tarefas de meio dia"
```

Ou rode o script pronto: `bash jarvis/bin/instalar-fabrica.sh ~/projetos/<cliente>`

---

## Ordem de execução — faça nesta sequência

1. [ ] Criar `FSA — ESTADO` no Drive e preencher as 5 linhas manuais
2. [ ] Criar projeto `JARVIS` no Cowork com `00-JARVIS.md`
3. [ ] Testar: `roda o boletim agora` — tem que responder em segundos
4. [ ] Ligar a Rotina diária 07:00
5. [ ] Ligar a Rotina semanal sexta 17:00
6. [ ] Rodar `instalar-fabrica.sh` no repo do próximo projeto que começar

Passos 1 a 4 dão o acompanhamento de CEO funcionando. 5 e 6 podem esperar uma
semana. Não tente fazer os seis num dia — o painel precisa de alguns dias de
dado real antes de valer alguma coisa.
