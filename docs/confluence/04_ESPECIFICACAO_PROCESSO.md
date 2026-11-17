# Especificação funcional e mapeamento do processo
**Pedido do negócio:** enxergar evolução e principais motivos de chamados de sustentação.

## História do usuário
Como responsável pela operação, quero consultar chamados mensais e categorias recorrentes para priorizar a revisão de processos, campos e regras de negócio.

## Critérios de aceite
1. Quantidade mensal corresponde à contagem direta dos registros CSV/SQLite.
2. Redução entre janeiro e dezembro é 82% no cenário (100 → 18).
3. Dashboard exibe 12 meses e lista categorias com volume.
4. Documento informa origem, regras, responsável e limites do indicador.
5. Um novo campo não é publicado sem descrição, tipo, classificação e aprovação.

## Fluxo do processo de negócio e dados
Operação registra chamado → Engenharia identifica tabela/campo envolvido → Governança verifica definição no glossário/dicionário → SQL valida causa e relacionamento → relatório mostra tendência → negócio prioriza ação → nova medição.

## Modelo relacional
`apolices (1) → (N) chamados` e `apolices (1) → (N) sinistros`.

## Modelo dimensional: alternativa possível
`fato_chamado` (uma linha por chamado) com `dim_apolice`, `dim_mes`, `dim_categoria`. Neste case simples, optou-se pelo relacional para reduzir complexidade; a alternativa dimensional foi documentada sem implementação.

## Critério de sucesso (hipótese)
Diminuir retrabalho e padronizar conceitos, sem inferir que a documentação isoladamente causou a redução simulada.
