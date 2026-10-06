# FSA⁴Future · Operação do atendimento@ (D8)

**Endereço:** atendimento@fsa4f.com.br (handoff v1.3 §25). **Status:** a criar. O domínio fsa4f.com.br precisa estar registrado em nome da FSA IT4FUTURE HUB TECNOLOGIA LTDA (CNPJ 69.447.199/0001-05).

## Checklist
- [ ] Domínio registrado no CNPJ da FSA IT4FUTURE e DNS sob conta da empresa (não pessoal).
- [ ] Caixa ou grupo `atendimento@` (Google Workspace: Grupo colaborativo; Microsoft 365: caixa compartilhada) — sem senha compartilhada.
- [ ] **Dois responsáveis** com acesso nominal: Cátia + _(definir)_. **Contingência:** _(definir)_. Hoje a base de regras diz "por enquanto, tudo com a Cátia": isso não cumpre o requisito de dois responsáveis.
- [ ] MFA obrigatório para todos os responsáveis.
- [ ] Assinatura institucional padronizada (FSA⁴Future · Technology & Business Hub · Technology 4 what's next.).
- [ ] Resposta automática fora do horário **sem prometer prazo** (decisão de 06/10): "Recebemos sua mensagem. Nosso atendimento é de segunda a sexta, das 9h às 18h."
- [ ] Rótulo/etiqueta automática para assunto "Privacidade" (pedidos LGPD, resposta em até 15 dias — prazo legal interno).
- [ ] Processo de cobertura de férias e ausências.
- [ ] Teste de envio, recebimento, resposta e encaminhamento antes do go-live.

## DNS (modelo — confirmar valores no provedor de e-mail)
| Tipo | Nome | Valor (exemplo Google Workspace) |
|---|---|---|
| MX | @ | `smtp.google.com` (prioridade 1) |
| TXT (SPF) | @ | `v=spf1 include:_spf.google.com ~all` (incluir também o serviço de envio do site, se houver) |
| TXT (DKIM) | `google._domainkey` | chave gerada no Admin Console |
| TXT (DMARC) | `_dmarc` | `v=DMARC1; p=none; rua=mailto:atendimento@fsa4f.com.br; fo=1` → subir para `p=quarantine` após 2–4 semanas de relatórios limpos |

## Integrações
- **Site:** links de e-mail e resumo já apontam para atendimento@ (`CONFIG.email` em `fsa4future/assets/js/site.js`).
- **FSiA:** o e-mail com resumo sai do cliente de e-mail da própria pessoa, com o resumo no corpo (só com consentimento).
- **Formulário:** opcional `CONFIG.formEndpoint` (ex.: Google Apps Script que grava numa planilha e envia cópia a atendimento@).
- **Agenda:** no Calendly, notificações de agendamento para atendimento@ e o evento "Conversa de Entendimento FSA — 30 min".

## Desligamento do e-mail nominal da Cátia
Só depois de **todos** os pontos de contato usarem atendimento@: site, FSiA, Calendly, assinaturas, propostas e materiais comerciais, perfis em redes, Google Business Profile, cadastros de fornecedores e clientes, contratos do Programa de Parceiros. Até lá, o nominal continua recebendo normalmente e as respostas passam a apresentar atendimento@ como canal oficial.
