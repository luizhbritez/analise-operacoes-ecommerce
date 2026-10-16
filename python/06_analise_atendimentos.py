import sqlite3
conexao = sqlite3.connect('ecommerce_atendimento.db')
cursor = conexao.cursor()

cursor.execute('SELECT id_atendimento, id_pedido, canal, motivo_atendimento, data_abertura, data_fechamento, status_atendimento, nota_satisfacao FROM atendimentos')
atendimentos = cursor.fetchall()

atendimento_resolvido = 0
soma_notas = 0
quantidade_notas = 0

for atendimento in atendimentos:
    if atendimento[6] == 'Resolvido':
        atendimento_resolvido = atendimento_resolvido + 1
    if atendimento[7] is not None:
        soma_notas = soma_notas + atendimento[7]
        quantidade_notas = quantidade_notas + 1

    print(f'ID de atendimento: {atendimento[0]} | ID do pedido: {atendimento[1]} | Canal de atendimento: {atendimento[2]} | Motivo de atendimento: {atendimento[3]} | Data da abertura: {atendimento[4]} | Data do fechamento: {atendimento[5]} | Status do atendimento: {atendimento[6]} | Nota de satisfação: {atendimento[7]}')

print('Atendimentos resolvidos:', atendimento_resolvido)

if quantidade_notas > 0:
    media_satisfacao = soma_notas / quantidade_notas
    print(f'Média de satisfação: {media_satisfacao:.2f}')

cursor.close()
conexao.close()