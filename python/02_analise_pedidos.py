import sqlite3

conexao = sqlite3.connect('ecommerce_atendimento.db')
cursor = conexao.cursor()

cursor.execute('SELECT id_pedido, status_pedido, valor_total FROM pedidos')
pedidos = cursor.fetchall()
for pedido in pedidos:
    print(
        f'Identificador: {pedido[0]} | Status do pedido: {pedido[1]} | Valor do pedido: R$ {pedido[2]:.2f}'
          )

cursor.execute('SELECT SUM(valor_total), COUNT(id_pedido), AVG(valor_total) FROM pedidos')

resumo_geral = cursor.fetchone()

print(f'Valor total dos pedidos: R$ {resumo_geral[0]:.2f}')
print(f'Quantidade total de pedidos: {resumo_geral[1]}')
print(f'Valor médio dos pedidos: R$ {resumo_geral[2]:.2f}')

cursor.execute('SELECT status_pedido, COUNT(id_pedido), SUM(valor_total) FROM pedidos GROUP BY status_pedido')
pedidos_por_status = cursor.fetchall()
for status in pedidos_por_status:
    print(f'Status: {status[0]} | Quantidade: {status[1]} | Valor total: R$ {status[2]:.2f}')


cursor.close()
conexao.close()