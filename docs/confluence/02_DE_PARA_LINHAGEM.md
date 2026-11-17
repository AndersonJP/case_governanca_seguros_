# De-Para e linhagem (Data Lineage)
**Versão:** 1.0 | **Escopo:** origem simulada → dashboard HTML

## De-Para (campo de origem → coluna no modelo)
| Origem | Destino | Transformação | Validação |
|---|---|---|---|
| apolices.csv/id_apolice | apolices.id_apolice | sem transformação | único e não nulo |
| sinistros.csv/id_apolice | sinistros.id_apolice | sem transformação | deve existir em apolices |
| chamados.csv/id_apolice | chamados.id_apolice | sem transformação | deve existir em apolices |
| chamados.csv/mes_referencia | chamados.mes_referencia | manter YYYY-MM | mês válido |
| chamados.csv/categoria | chamados.categoria | preservar categoria | valor não vazio |
| chamados.csv/id_chamado | dashboard/total_mensal | COUNT(*) por mes_referencia | reconciliar contagem |
| dashboard/primeiro_e_ultimo_mes | dashboard/reducao_pct | (1-último/primeiro)*100 | janeiro = 100 e dezembro = 18 |

## Linhagem lógica
`CSV fictício → Python csv.DictReader → SQLite (PK/FK) → SQL GROUP BY → JSON embarcado no HTML → indicador do dashboard → decisão do negócio`

**Regra do indicador:** quantidade de registros em `chamados` agrupados por `mes_referencia`, independentemente do `status`. Escolha didática a ser validada em cenário real.

## Análise de impacto
Se `mes_referencia` mudar de formato, atualizar carga, testes SQL, dicionário e dashboard. Se mudar a definição de chamado, revisar com negócio antes da publicação.

## Ferramentas equivalentes, sem implantação aqui
Unity Catalog e AWS Glue Data Catalog poderiam armazenar/descobrir metadados; o case apenas documenta o conceito, não simula uma integração real com essas soluções.
