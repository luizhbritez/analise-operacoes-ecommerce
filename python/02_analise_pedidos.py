import sqlite3

conexao = sqlite3.connect('ecommerce_atendimento.db')
cursor = conexao.cursor()

cursor.execute('SELECT id_pedido, status_pedido, valor_total FROM pedidos')
pedidos = cursor.fetchall()
for pedido in pedidos:
    print(
        f'Identificador: {pedido[0]} | Status do pedido: {pedido[1]} | Valor do pedido: R$ {pedido[2]:.2f}'
          )

cursor.execute('SELECT SUM(valor_total) FROM pedidos')
resultado_total = cursor.fetchone()
print(f'Valor total dos pedidos: R$ {resultado_total[0]:.2f}')

cursor.execute('SELECT COUNT(id_pedido) FROM pedidos')
resultado_quantidade = cursor.fetchone()
print(f'Quantidade total de pedidos: {resultado_quantidade[0]}')

cursor.execute('SELECT AVG(valor_total) FROM pedidos')
resultado_media = cursor.fetchone()
print(f'Valor médio dos pedidos: R$ {resultado_media[0]:.2f}')

cursor.close()
conexao.close()