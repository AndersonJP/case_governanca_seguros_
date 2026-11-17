# Case rápido | Governança de Dados em Seguros

Um projeto demonstrativo pequeno para explicar como **dicionário, regras de negócio, De-Para, linhagem e SQL** ajudam a organizar dados e dar mais confiança aos indicadores.

**Cenário:** evolução fictícia de chamados de sustentação de 100 para 18 por mês (**−82%**). A ideia foi inspirada em um resultado profissional anterior em outro contexto. **Não são dados da Seguros Unimed e não há comprovação de que o dashboard causou a redução.** Os conceitos de seguros são simplificados e não substituem validação de especialistas.

## Ver em 1 minuto
1. Abra [`dashboard/index.html`](dashboard/index.html) no navegador (funciona offline).
2. Confira as consultas em [`sql/02_validacoes.sql`](sql/02_validacoes.sql).
3. Veja o [índice da documentação estilo Confluence](docs/confluence/00_PAGINA_INICIAL.md).
4. Veja a [arquitetura de ponta a ponta](assets/arquitetura.png).

## Reproduzir
Com Python 3, sem bibliotecas adicionais:

```bash
python src/gerar_case.py
python -m unittest discover -s tests -v
```

O script lê 3 CSVs, recria/atualiza a base SQLite e gera novamente o dashboard HTML. Abra `dashboard/index.html` após executar.

## O que tem aqui
`dados/`: apólices, sinistros e chamados inventados; `sql/`: modelo e consultas JOIN/Window Function; `src/`: ETL simples; `dashboard/`: visualização offline; `docs/confluence/`: páginas Markdown prontas para copiar para o Confluence; `tests/`: verificações.

## Como eu apresentaria
"Eu quis mostrar mais do que um dashboard: mapeei tabelas e chaves, defini regras, documentei o De-Para e a linhagem, validei com SQL e só então apresentei os indicadores. É um case fictício e intencionalmente simples, pensado para demonstrar método e clareza." 

**Limites:** Confluence, AWS Glue e Unity Catalog são discutidos como conceitos, mas não foram conectados. Publicação no Confluence é manual. Dados de seguros, métricas e regras são didáticos.
