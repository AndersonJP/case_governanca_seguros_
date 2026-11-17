-- Base demonstrativa SQLite. Tipos e chaves documentados para o catálogo.
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS apolices (
 id_apolice TEXT PRIMARY KEY, id_cliente TEXT NOT NULL, produto TEXT NOT NULL,
 data_inicio TEXT NOT NULL, data_fim TEXT NOT NULL, status TEXT NOT NULL,
 premio_total REAL NOT NULL CHECK (premio_total >= 0)
);
CREATE TABLE IF NOT EXISTS sinistros (
 id_sinistro TEXT PRIMARY KEY, id_apolice TEXT NOT NULL,
 data_aviso TEXT NOT NULL, tipo TEXT NOT NULL, status TEXT NOT NULL,
 FOREIGN KEY(id_apolice) REFERENCES apolices(id_apolice)
);
CREATE TABLE IF NOT EXISTS chamados (
 id_chamado TEXT PRIMARY KEY, id_apolice TEXT NOT NULL,
 mes_referencia TEXT NOT NULL, categoria TEXT NOT NULL, status TEXT NOT NULL,
 origem TEXT NOT NULL, horas_resolucao INTEGER NOT NULL,
 FOREIGN KEY(id_apolice) REFERENCES apolices(id_apolice)
);
