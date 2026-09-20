import sqlite3
conexao = sqlite3.connect('ecommerce_atendimento.db')
print('Conexão realizada com sucesso!')
cursor = conexao.cursor()
cursor.execute('SELECT * FROM clientes')
clientes = cursor.fetchall()
for cliente in clientes:
    print(f'Nome: {cliente[1]} | Cidade: {cliente[2]}')
cursor.close()
conexao.close()