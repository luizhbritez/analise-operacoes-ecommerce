import sqlite3
from pathlib import Path

caminho_banco = Path('ecommerce_atendimento.db')
caminho_estrutura = Path('sql/00_estrutura_banco.sql')
caminho_carga = Path('sql/01_carga_dados.sql')
estrutura_sql = caminho_estrutura.read_text(encoding='utf-8-sig')
carga_sql = caminho_carga.read_text(encoding='utf-8-sig')

if caminho_banco.exists():
    caminho_banco.unlink()

conexao = sqlite3.connect(caminho_banco)
conexao.executescript(estrutura_sql)
conexao.executescript(carga_sql)

conexao.close()
print('Banco criado e dados carregados com sucesso.')