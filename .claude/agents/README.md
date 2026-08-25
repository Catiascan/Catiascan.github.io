# Subagentes deste projeto

Arquivos Markdown com um cabeçalho YAML, lidos pelo Claude Code na pasta
`.claude/agents/`. Como estão versionados no repositório, valem sempre que se
trabalha neste projeto — em qualquer máquina e também no Claude Code na web.

| Agente | Para quê | Escreve arquivo? |
|---|---|---|
| `revisor-site` | HTML, CSS, celular, acessibilidade, links quebrados e conformidade com o brand book | Não |
| `seo-tecnico` | Meta tags, preview no WhatsApp, Google, dados estruturados, robots e sitemap | Só quando pedido |
| `copy-fsa` | Texto do site na voz da FSA e da S.E.A. | Só quando pedido |
| `conselho-fsa` | Pergunta de negócio, encaminhada para a skill da área certa | Não |
| `status-para-iris` | Lê o andamento no git e escreve o status para a Iris, com os pontos que ela precisa validar | Não |

## Como usar

Falando o nome, em português normal:

```
Usa o revisor-site para verificar a acessibilidade da página
```

Ou garantindo o agente com @:

```
@"seo-tecnico (agent)" o link está sem preview no WhatsApp
```

## Como mudar um agente

Edite o `.md` correspondente. O campo `description` é o que decide quando o
Claude chama aquele agente — quanto mais concreto ("use quando pedirem X"),
melhor. O campo `tools` é uma lista de permissão: o que não estiver ali, o
agente não consegue fazer.

## Marca

Os agentes seguem o **Brand Book FSA 2026**: paleta Azul `#020084`, Amarelo
`#FFDE59`, Cinza `#38424C`; slogan "Sua visão. Nosso código. Um negócio.";
tipografia Sora (títulos) e Inter (corpo), substitutas oficiais de LASTICA e
ASTRON; e o emblema FSA nunca recriado à mão.

Documentação dos subagentes: https://code.claude.com/docs/en/sub-agents
