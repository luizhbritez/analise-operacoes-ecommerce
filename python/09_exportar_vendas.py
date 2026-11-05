import sqlite3
import csv
conexao = sqlite3.connect('ecommerce_atendimento.db')
cursor = conexao.cursor()

cursor.execute("SELECT pr.nome_produto, pr.categoria, SUM(i.quantidade), SUM(i.quantidade * i.preco_unitario) FROM produtos AS pr LEFT JOIN itens_pedido AS i ON pr.id_produto = i.id_produto LEFT JOIN pedidos AS p ON i.id_pedido = p.id_pedido WHERE p.status_pedido <> 'Cancelado' GROUP BY pr.id_produto, pr.nome_produto, pr.categoria")
vendas = cursor.fetchall()

with open('vendas_por_produto.csv', 'w', newline = '', encoding = 'utf-8-sig') as arquivo:
    escritor = csv.writer(arquivo, delimiter = ';')
    escritor.writerow(['Produto', 'Categoria', 'Quantidade', 'Valor total vendido'])
    escritor.writerows(vendas)

cursor.execute("SELECT pr.categoria, SUM(i.quantidade), SUM(i.quantidade * i.preco_unitario) FROM produtos AS pr LEFT JOIN itens_pedido AS i ON pr.id_produto = i.id_produto LEFT JOIN pedidos AS p ON i.id_pedido = p.id_pedido WHERE p.status_pedido <> 'Cancelado' GROUP BY pr.categoria")
vendas_por_categoria = cursor.fetchall()

with open('vendas_por_categoria.csv', 'w', newline = '', encoding = 'utf-8-sig') as arquivo:
    escritor = csv.writer(arquivo, delimiter = ';')
    escritor.writerow(['Categoria', 'Quantidade', 'Valor total vendido'])
    escritor.writerows(vendas_por_categoria)

cursor.close()
conexao.close()