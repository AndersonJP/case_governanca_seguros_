# Catálogo de ativos e dicionário de dados
**Versão:** 1.0 | **Ambiente:** simulado SQLite | **Proprietário:** a definir em ambiente real

## Catálogo de ativos
| Ativo | Origem | Granularidade | Chave | Consumo |
|---|---|---|---|---|
| apolices | dados/apolices.csv | 1 linha/apólice | id_apolice | visão de produtos e relacionamento |
| sinistros | dados/sinistros.csv | 1 linha/sinistro | id_sinistro | contexto operacional |
| chamados | dados/chamados.csv | 1 linha/chamado | id_chamado | dashboard mensal |

## Dicionário técnico
| Tabela.campo | Tipo SQLite | Regra / definição | Chave / vínculo | Classificação |
|---|---|---|---|---|
| apolices.id_apolice | TEXT | identificador único fictício | PK | Interno |
| apolices.id_cliente | TEXT | identificador pseudônimo fictício | — | Restrito no cenário real |
| apolices.produto | TEXT | modalidade de produto | — | Interno |
| apolices.data_inicio | TEXT (ISO date) | início da vigência de exemplo | — | Interno |
| apolices.data_fim | TEXT (ISO date) | fim da vigência de exemplo | — | Interno |
| apolices.status | TEXT | Ativa/Cancelada; simplificação | — | Interno |
| apolices.premio_total | REAL | valor fictício do prêmio da apólice | — | Restrito comercial |
| sinistros.id_sinistro | TEXT | identificador único de sinistro | PK | Interno |
| sinistros.id_apolice | TEXT | apólice associada | FK → apolices | Interno |
| sinistros.data_aviso | TEXT | data do aviso do sinistro | — | Interno |
| sinistros.tipo | TEXT | categoria de ocorrência de exemplo | — | Interno |
| sinistros.status | TEXT | Aberto/Concluído no cenário | — | Interno |
| chamados.id_chamado | TEXT | identificador único de chamado | PK | Interno |
| chamados.id_apolice | TEXT | apólice ligada ao suporte | FK → apolices | Interno |
| chamados.mes_referencia | TEXT (YYYY-MM) | mês para contagem | — | Interno |
| chamados.categoria | TEXT | natureza da demanda | — | Interno |
| chamados.status | TEXT | estado operacional do chamado | — | Interno |
| chamados.origem | TEXT | canal/fonte do chamado | — | Interno |
| chamados.horas_resolucao | INTEGER | duração total em horas no cenário | — | Interno |

## Convenções
Snake_case; datas em ISO 8601; identificadores textuais; não alterar o sentido de campos sem revisão de regra e aprovação. Em produção, usar tipos DATE/DECIMAL apropriados e controles de acesso reais.
