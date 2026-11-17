# Case | Governança de Dados em Seguros
**Status:** Demonstração | **Versão:** 1.0 | **Responsável:** autor do case | **Data:** 17/11/2026

> Ambiente fictício, sem acesso a sistemas da Seguros Unimed. Resultado de 82% é cenário inspirado em uma conquista profissional anterior em sustentação, não uma medição da seguradora nem um efeito causal comprovado deste projeto.

## Problema de negócio
Divergências de definição, campos pouco documentados e ausência de visão integrada dificultam identificar as causas de chamados recorrentes. O case documenta um pequeno conjunto de tabelas e mede a evolução mensal desses chamados.

## Escopo
- Três fontes CSV: apólices, sinistros e chamados.
- SQL/SQLite para relacionamentos, verificações e indicadores.
- Dicionário, De-Para, glossário, regras, linhagem e aprovação antes de produção.
- Dashboard HTML offline e recomendações.

## Fora do escopo
Sistemas reais, dados pessoais verdadeiros, apuração regulatória, Unity Catalog/AWS operacionais, publicação em Confluence via API e automação em produção.

## Índice da documentação
1. [Catálogo e dicionário](01_CATALOGO_DICIONARIO.md)
2. [De-Para e linhagem](02_DE_PARA_LINHAGEM.md)
3. [Glossário e regras](03_GLOSSARIO_REGRAS.md)
4. [Especificação funcional e processo](04_ESPECIFICACAO_PROCESSO.md)
5. [Qualidade, classificação e aprovação](05_QUALIDADE_APROVACAO.md)
6. [Operação e decisões](06_OPERACAO_NEGOCIO.md)

## Quem valida no cenário
- Área de negócio: conceitos e regras de seguros.
- Engenharia de Dados: modelo técnico, carga e linhagem.
- Governança: classificação, nomenclatura, versões e aprovação.

## Processo de atualização
Solicitação → análise de impacto → revisão de campos/regras → testes SQL → validação do negócio → aprovação de governança → publicação → comunicação aos consumidores.
