# Glossário e catálogo de regras de negócio
**Versão:** 1.0 | **Validação real de seguros:** pendente (demonstração)

## Glossário para áreas de negócio
| Termo | Definição de trabalho | Observação |
|---|---|---|
| Apólice | instrumento que formaliza o contrato de seguro | validar com Jurídico/Produto |
| Endosso | alteração formal das condições da apólice | não modelado no CSV |
| Sinistro | ocorrência comunicada para análise de cobertura | sinistro não equivale automaticamente a indenização |
| Prêmio | valor cobrado pela cobertura | não confundir com indenização |
| Prêmio ganho | parcela reconhecida conforme competência e normas aplicáveis | **não calculado aqui** |
| Cosseguro | divisão de um mesmo risco entre seguradoras | não modelado aqui |
| Comissão | remuneração contratual de intermediação | **não calculado aqui** |
| Chamado de sustentação | registro de demanda corretiva/de esclarecimento no cenário | definição didática |

## Regras documentadas
| ID | Regra | Implementação | Dono da aprovação |
|---|---|---|---|
| RN-01 | cada apólice possui `id_apolice` único | PK em SQLite | Eng. Dados |
| RN-02 | sinistro e chamado precisam apontar para apólice existente | FKs e teste SQL | Eng. Dados |
| RN-03 | chamado mensal é `COUNT(*)` por `mes_referencia` | query e HTML | Operação |
| RN-04 | redução comparativa = (1 - Dez/Jan)*100 | Python | Operação |
| RN-05 | cancelamento é representado pelo status textual da apólice | simplificação, não valida regras contratuais | Produto |
| RN-06 | prêmio ganho exige regra técnica/contábil específica, a aprovar | fora do escopo | Atuária/Contabilidade |
| RN-07 | comissionamento depende de contrato, data e produto | fora do escopo | Comercial |

**Atenção:** não apresentar RN-05, RN-06 ou RN-07 como fórmulas regulatórias ou regras oficiais da Seguros Unimed.
