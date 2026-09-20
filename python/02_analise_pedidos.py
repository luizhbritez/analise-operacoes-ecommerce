import sqlite3
conexao = sqlite3.connect('ecommerce_atendimento.db')
cursor = conexao.cursor()
cursor.execute('SELECT id_pedido, status_pedido, valor_total FROM pedidos')
pedidos = cursor.fetchall()
for pedido in pedidos:
    print(
        f'Identificador: {pedido[0]} | Status do pedido: {pedido[1]} | Valor do pedido: R$ {pedido[2]:.2f}'
          )
cursor.close()
conexao.close()