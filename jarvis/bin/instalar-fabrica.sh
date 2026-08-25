#!/usr/bin/env bash
# Instala a estrutura da fábrica de software AI-first da FSA num repositório.
# Uso: bash instalar-fabrica.sh /caminho/do/repo
set -euo pipefail

REPO="${1:-}"
if [[ -z "$REPO" ]]; then
  echo "uso: bash instalar-fabrica.sh /caminho/do/repo" >&2
  exit 1
fi
if [[ ! -d "$REPO/.git" ]]; then
  echo "erro: $REPO não é um repositório git" >&2
  exit 1
fi

AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

mkdir -p "$REPO/docs"

criar_se_falta() {
  local alvo="$1" conteudo="$2"
  if [[ -e "$alvo" ]]; then
    echo "  mantido (já existe): ${alvo#$REPO/}"
  else
    printf '%s\n' "$conteudo" > "$alvo"
    echo "  criado: ${alvo#$REPO/}"
  fi
}

echo "instalando a fábrica em $REPO"

criar_se_falta "$REPO/docs/DDE.md" "# DDE — Documento de Declaração de Escopo

Nenhuma linha de código antes deste documento estar aprovado.

## 1. Escopo (numerado, com critério de pronto por item)

## 2. Fora de escopo (explícito — é isto que evita aditivo grátis)

## 3. Insumos externos

| Insumo | Dono | Data acordada | Recebido? |
|---|---|---|---|

## 4. Marco zero

Data: ____  Aprovado por: ____
O prazo só começa a contar quando todos os insumos da tabela acima chegarem."

criar_se_falta "$REPO/docs/BACKLOG.md" "# Backlog — decomposição do DDE

Tarefas de no máximo meio dia. Tarefa que não cabe aqui está mal entendida.

| ID | Item do DDE | O que muda | Como se prova | Arquivos |
|---|---|---|---|---|"

criar_se_falta "$REPO/docs/STATUS.md" "# Status — para o cliente ler

Reescrito toda sexta pela rotina semanal.

## Semana de __/__ a __/__

Fechou:
Atrasou (e por quê):
Impacto em data:"

criar_se_falta "$REPO/docs/PEDIDOS-EXTRA.md" "# Pedidos fora de escopo

Tudo que o cliente pediu e não está no DDE. Cada linha é aditivo, com horas.

| Data | Quem pediu | O quê | Horas estimadas | Virou aditivo? |
|---|---|---|---|---|"

if [[ -e "$REPO/CLAUDE.md" ]]; then
  echo "  mantido (já existe): CLAUDE.md — confira se contém o prompt da fábrica"
else
  sed -n '/^## Prompt (salvar como/,/^---$/p' "$AQUI/03-FABRICA-SOFTWARE.md" \
    | sed '1d;$d' > "$REPO/CLAUDE.md"
  echo "  criado: CLAUDE.md (prompt da fábrica)"
fi

echo
echo "pronto. próximo passo, dentro de $REPO:"
echo "  claude  →  \"leia docs/DDE.md e decomponha o item 1 em tarefas de meio dia\""
