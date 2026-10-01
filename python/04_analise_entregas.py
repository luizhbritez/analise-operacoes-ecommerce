import sqlite3
import datetime
conexao = sqlite3.connect('ecommerce_atendimento.db')
cursor = conexao.cursor()
data_atual = datetime.date.today()

cursor.execute('SELECT id_pedido, transportadora, data_envio, data_prevista, data_entrega, status_entrega FROM entregas')
entregas = cursor.fetchall()
quantidade_entregas_pendentes = 0
quantidade_entregas_atrasadas = 0
for entrega in entregas:
    data_prevista = datetime.date.fromisoformat(entrega[3])
    if entrega[4] is None:
        data_entrega_formatada = 'Ainda não entregue'
        quantidade_entregas_pendentes = quantidade_entregas_pendentes + 1
        if data_prevista < data_atual:
            quantidade_entregas_atrasadas = quantidade_entregas_atrasadas +1
    else:
        data_entrega_formatada = entrega[4]
    print(f'ID do pedido: {entrega[0]} | Transportadora: {entrega[1]} | Data de envio: {entrega[2]} | Data prevista: {entrega[3]} | Data da entrega: {data_entrega_formatada} | Status da entrega: {entrega[5]}')
print(f'Quantidade de entregas pendentes: {quantidade_entregas_pendentes}')
print(f'Quantidade de entregas atrasadas: {quantidade_entregas_atrasadas}')
cursor.close()
conexao.close()