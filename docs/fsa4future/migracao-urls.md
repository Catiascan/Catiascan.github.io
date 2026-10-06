# FSA⁴Future · Mapa de migração de URLs (G3)

**Status:** bloqueado — falta o inventário do site atual e acesso ao Search Console e ao analytics (pendência F, "Site atual").
**Regra (handoff §15):** não publicar o rebranding sem este mapa. Cada URL antiga com valor ganha um 301 **individual** para a equivalente nova. Nada de mandar tudo para a home. Sem cadeias nem loops.

## Como preencher
1. Exportar do Search Console (Desempenho → Páginas, 16 meses) e do analytics (páginas de entrada, 12 meses).
2. Rodar um rastreamento do site atual (Screaming Frog ou similar) e juntar: URL, status, title, canonical, backlinks (Search Console → Links).
3. Para cada URL indexável, preencher a linha abaixo. URL sem equivalente e sem valor: 410. URL com valor e sem equivalente: 301 para a página mais próxima em intenção (nunca a home por padrão).
4. Gerar o arquivo de redirects da hospedagem escolhida a partir da tabela e testar cada linha (status 301, destino 200, sem cadeia).

## Tabela
| URL antiga | Status atual | Title atual | Cliques 16m | Backlinks | Função | URL nova | Ação (301/410/manter) | Testado |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## URLs novas disponíveis (destinos)
`/` · `/desafios/` · `/como-fazemos/` · `/como-fazemos/{ouvir,entender,conectar,construir,validar,evoluir}/` · `/hub/` · `/hub/fsa-4-flow/` · `/hub/fsa-4-partners/` · `/hub/fsa-4-partners/programa/` · `/hub/fsa-4-solutions/` · `/hub/fsa-4-products/` · `/cases/` · `/sobre/` · `/conteudos/` · `/conversar/` · `/privacidade/` · `/cookies/`

## Modelos de arquivo de redirects
Netlify / Cloudflare Pages (`_redirects` na raiz publicada):
```
/servicos/automacao   /hub/fsa-4-flow/        301
/contato              /conversar/             301
```
Vercel (`vercel.json`):
```json
{ "redirects": [ { "source": "/contato", "destination": "/conversar/", "permanent": true } ] }
```
(As linhas acima são exemplos de formato, não URLs reais do site atual.)

## Depois do go-live
Search Console: enviar `https://fsa4future.com.br/sitemap.xml`, acompanhar Cobertura/Páginas por 30 dias, inspecionar as 20 URLs antigas com mais cliques. Bing Webmaster Tools: importar do Search Console e enviar o sitemap. IndexNow: publicar a chave na raiz e enviar as URLs novas (Bing/Yandex).
