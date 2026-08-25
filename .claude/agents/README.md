# Subagentes deste projeto

Ficheiros Markdown com frontmatter YAML que o Claude Code lê a partir de
`.claude/agents/`. Como estão versionados no repositório, valem sempre que se
trabalha neste projeto — em qualquer máquina e também no Claude Code na web.

| Agente | Para quê | Ferramentas | Escreve ficheiros? |
|---|---|---|---|
| `revisor-site` | HTML, CSS, responsividade, acessibilidade, links partidos | Read, Grep, Glob, Bash | Não |
| `seo-tecnico` | Meta tags, Open Graph, JSON-LD, robots, sitemap | Read, Grep, Glob, Edit, WebFetch | Só quando pedido |
| `copy-fsa` | Texto do site na voz da FSA e da S.E.A. | Read, Grep, Glob, Edit, Skill | Só quando pedido |
| `conselho-fsa` | Perguntas de negócio, encaminhadas para a skill da área | Read, Grep, Glob, Skill, WebSearch, WebFetch | Não |

## Como usar

Em linguagem natural, dizendo o nome:

```
Usa o revisor-site para verificar a acessibilidade da página
```

Ou garantindo o agente com @-menção:

```
@"seo-tecnico (agent)" o link está a ficar sem preview no WhatsApp
```

## Como alterar

Editar o `.md` correspondente. O `description` é o que decide quando o Claude
delega — quanto mais concreto ("usa quando pedirem X"), melhor o encaminhamento.
O `tools` é uma lista de permissão: o que não estiver lá, o agente não faz.

Documentação: https://code.claude.com/docs/en/sub-agents
