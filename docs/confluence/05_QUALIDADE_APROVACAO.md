# Qualidade dos dados, classificação e liberação
**Versão:** 1.0 | **Tipo:** checklist de governança

## Testes de qualidade
| Controle | Como testar | Esperado |
|---|---|---|
| Unicidade | GROUP BY id_apolice HAVING COUNT(*) > 1 | 0 duplicados |
| Integridade | JOIN de chamados com apólices sem correspondência | 0 órfãos |
| Completude | mes_referencia vazio/nulo | 0 linhas |
| Validade | mês em YYYY-MM | somente 2026-01 a 2026-12 |
| Reconciliação | soma dos 12 meses = total de chamados | igualdade |
| Exatidão ilustrativa | Jan=100, Dez=18 | redução=82% |

## Exemplo de validação de novo campo
**Campo proposto:** `chamados.prioridade` (não implementado)
- Definição e domínio: Baixa/Média/Alta, aprovados por Operação.
- Origem: sistema de atendimento real (a identificar).
- Tipo: TEXT com CHECK ou dimensão controlada.
- Classificação: Interno.
- Qualidade: completude e valores fora do domínio.
- Linhagem: origem → ETL → tabela → dashboard.
- Versionamento: atualizar dicionário, De-Para, testes e changelog.

## Gate antes de produção (exemplo)
- [ ] Campo e regra validados pelo dono de negócio
- [ ] Tipo, PK/FK e classificação documentados
- [ ] Testes SQL executados e sem divergências
- [ ] Linhagem e impacto nos relatórios mapeados
- [ ] Governança aprovou e registrou versão
- [ ] Consumidores foram informados

**Status deste repositório:** demonstração local, não homologado para produção real.

## Boas práticas DAMA-DMBOK aplicadas
Definições compartilhadas, responsabilidade clara, metadados, qualidade, governança e ciclo de mudança. Não representa certificação nem implementação integral do framework.
