import sqlite3
conexao = sqlite3.connect('ecommerce_atendimento.db')

cursor = conexao.cursor()

cursor.execute('SELECT id_pagamento, id_pedido, metodo_pagamento, status_pagamento, valor_pago, data_pagamento FROM pagamentos')
pagamentos = cursor.fetchall()

pagamentos_aprovados = 0
pagamentos_recusados = 0
valor_total_aprovado = 0
for pagamento in pagamentos:
    if pagamento[3] == 'Aprovado':
        pagamentos_aprovados = pagamentos_aprovados + 1
        valor_total_aprovado = valor_total_aprovado + pagamento[4]
    if pagamento[3] == 'Recusado':
        pagamentos_recusados = pagamentos_recusados + 1
    if pagamento[5] is None:
        data_pagamento_formatada = 'Pagamento não realizado'
    else:
        data_pagamento_formatada = pagamento[5]
    print(f'ID do pagamento: {pagamento[0]} | ID do pedido: {pagamento[1]} | Método: {pagamento[2]} | Status: {pagamento[3]} | Valor pago: {pagamento[4]:.2f} | Data do pagamento: {data_pagamento_formatada}')
print(f'O total de pagamentos aprovados: {pagamentos_aprovados}')
print(f'O total de pagamentos recusados: {pagamentos_recusados}')
print(f'Valor total aprovado: R$ {valor_total_aprovado:.2f}')
cursor.close()
conexao.close()