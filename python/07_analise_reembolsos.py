import sqlite3
conexao = sqlite3.connect('ecommerce_atendimento.db')
cursor = conexao.cursor()

cursor.execute('SELECT id_reembolso, id_pagamento, data_solicitacao, data_conclusao, valor_reembolso, motivo_reembolso, status_reembolso FROM reembolsos')
reembolsos = cursor.fetchall()

quantidade_reembolsos_pendentes = 0
valor_total_pendente = 0

for reembolso in reembolsos:
    if reembolso[6] == 'Pendente':
        quantidade_reembolsos_pendentes = quantidade_reembolsos_pendentes + 1
        valor_total_pendente = valor_total_pendente + reembolso[4]
    if reembolso[3] is None:
        data_conclusao_formatada = 'Ainda não concluído'
    else:
        data_conclusao_formatada = reembolso[3]

    print(f'ID de reembolso: {reembolso[0]} | ID de pagamento: {reembolso[1]} | Data de solicitação: {reembolso[2]} | Data de conclusão: {data_conclusao_formatada} | Valor do reembolso: R$ {reembolso[4]:.2f} | Motivo do reembolso: {reembolso[5]} | Status do reembolso: {reembolso[6]}')

print(f'Quantidade de reembolsos pendentes: {quantidade_reembolsos_pendentes}')
print(f'Valor total pendente: R$ {valor_total_pendente:.2f}')

cursor.close()
conexao.close()