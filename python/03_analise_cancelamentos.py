import sqlite3

conexao = sqlite3.connect('ecommerce_atendimento.db')
cursor = conexao.cursor()

cursor.execute("SELECT id_pedido, valor_total, motivo_cancelamento FROM pedidos WHERE status_pedido = 'Cancelado'")
pedidos_cancelados = cursor.fetchall()
valor_total_cancelado = 0
for pedido_cancelado in pedidos_cancelados:
    print(f'Identificador do pedido: {pedido_cancelado[0]} | Valor do pedido: R$ {pedido_cancelado[1]:.2f} | Motivo do cancelamento: {pedido_cancelado[2]}')
    valor_total_cancelado += pedido_cancelado[1]
print('Quantidade de pedidos cancelados: ', len(pedidos_cancelados))
print(f'Valor total cancelado: R$ {valor_total_cancelado:.2f}')

cursor.close()
conexao.close()