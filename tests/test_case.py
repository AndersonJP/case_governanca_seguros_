import csv, unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'dados'
class TestCase(unittest.TestCase):
    def load(self,name):
        with (P/name).open(encoding='utf-8',newline='') as f: return list(csv.DictReader(f))
    def test_integridade(self):
        ap={x['id_apolice'] for x in self.load('apolices.csv')}
        self.assertTrue(all(x['id_apolice'] in ap for x in self.load('chamados.csv')))
        self.assertTrue(all(x['id_apolice'] in ap for x in self.load('sinistros.csv')))
    def test_pk_e_nao_nulos(self):
        for tab,key in [('apolices.csv','id_apolice'),('sinistros.csv','id_sinistro'),('chamados.csv','id_chamado')]:
            ids=[r[key] for r in self.load(tab)]
            self.assertEqual(len(ids),len(set(ids)))
            self.assertTrue(all(ids))
    def test_reducao_82(self):
        chamados=self.load('chamados.csv'); jan=sum(x['mes_referencia']=='2026-01' for x in chamados);dez=sum(x['mes_referencia']=='2026-12' for x in chamados)
        self.assertEqual((jan,dez),(100,18));self.assertAlmostEqual(100*(1-dez/jan),82)
    def test_mes(self):
        self.assertTrue(all(x['mes_referencia'].startswith('2026-') and 1 <= int(x['mes_referencia'][-2:]) <= 12 for x in self.load('chamados.csv')))
