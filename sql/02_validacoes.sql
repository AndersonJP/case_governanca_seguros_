-- JOIN: visão de chamados com seu produto; útil para explicar relacionamento.
SELECT c.id_chamado, a.produto, c.categoria, c.mes_referencia
FROM chamados c JOIN apolices a ON a.id_apolice = c.id_apolice
ORDER BY c.id_chamado LIMIT 10;

-- Window Function: tendência mês a mês preservando o registro mensal.
WITH mensal AS (
 SELECT mes_referencia, COUNT(*) AS quantidade
 FROM chamados GROUP BY mes_referencia
)
SELECT mes_referencia, quantidade,
 LAG(quantidade) OVER (ORDER BY mes_referencia) AS mes_anterior,
 ROUND(100.0 * (quantidade - LAG(quantidade) OVER (ORDER BY mes_referencia)) /
 NULLIF(LAG(quantidade) OVER (ORDER BY mes_referencia), 0), 1) AS variacao_pct
FROM mensal ORDER BY mes_referencia;

-- Qualidade: nenhum chamado sem uma apólice válida.
SELECT COUNT(*) AS chamados_orfaos FROM chamados c
LEFT JOIN apolices a ON a.id_apolice = c.id_apolice
WHERE a.id_apolice IS NULL;

-- Qualidade: identificadores duplicados e campos obrigatórios ausentes.
SELECT id_apolice, COUNT(*) AS ocorrencias FROM apolices GROUP BY id_apolice HAVING COUNT(*) > 1;
SELECT COUNT(*) AS mes_nulo FROM chamados WHERE mes_referencia IS NULL OR mes_referencia = '';
