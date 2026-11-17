"""Gera SQLite e dashboard HTML offline usando somente biblioteca padrão do Python.
Execute na raiz: python src/gerar_case.py
"""
from pathlib import Path
import csv, sqlite3, json, html
ROOT=Path(__file__).resolve().parents[1]
DB=ROOT/'dados/case_seguros.sqlite'
con=sqlite3.connect(DB)
con.executescript((ROOT/'sql/01_modelo.sql').read_text(encoding='utf-8'))
for tab in ('apolices','sinistros','chamados'):
    with (ROOT/'dados'/f'{tab}.csv').open(encoding='utf-8',newline='') as f:
        rows=list(csv.DictReader(f))
    # Mantém a carga reproduzível.
    con.execute(f'DELETE FROM {tab}') if tab=='chamados' else None
    # ON CONFLICT permite executar mais de uma vez sem duplicação.
    colunas=list(rows[0]); marcadores=','.join('?' for _ in colunas)
    con.executemany(f'INSERT OR REPLACE INTO {tab} ({",".join(colunas)}) VALUES ({marcadores})',
                   [[r[c] for c in colunas] for r in rows])
con.commit()
series=[{'mes':m,'quantidade':q} for m,q in con.execute(
    'SELECT mes_referencia,COUNT(*) FROM chamados GROUP BY mes_referencia ORDER BY mes_referencia')]
categorias=[{'categoria':c,'total':n} for c,n in con.execute(
    'SELECT categoria,COUNT(*) AS total FROM chamados GROUP BY categoria ORDER BY total DESC')]
primeiro,ultimo=series[0]['quantidade'],series[-1]['quantidade']
reducao=round((1-ultimo/primeiro)*100,1)
# Tokens substituídos no HTML: nenhum CDN nem consulta externa.
template=(ROOT/'dashboard/template.html').read_text(encoding='utf-8')
result=template.replace('/*__DADOS__*/', json.dumps({'serie':series,'categorias':categorias,'reducao':reducao}, ensure_ascii=False))
(ROOT/'dashboard/index.html').write_text(result,encoding='utf-8')
con.close()
print(f'Banco: {DB}; dashboard: dashboard/index.html; redução ilustrativa: {reducao}%')
