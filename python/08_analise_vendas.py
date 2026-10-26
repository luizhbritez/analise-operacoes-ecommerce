import sqlite3
conexao = sqlite3.connect('ecommerce_atendimento.db')
cursor = conexao.cursor()

cursor.execute("SELECT pr.nome_produto, pr.categoria, SUM(i.quantidade), SUM(i.quantidade * i.preco_unitario) FROM produtos AS pr LEFT JOIN itens_pedido AS i ON pr.id_produto = i.id_produto LEFT JOIN pedidos AS p ON i.id_pedido = p.id_pedido WHERE p.status_pedido <> 'Cancelado' GROUP BY pr.id_produto, pr.nome_produto, pr.categoria")
vendas = cursor.fetchall()
for venda in vendas:
    print(f'Nome do produto: {venda[0]} | Categoria: {venda[1]} | Quantidade: {venda[2]} | valor total vendido: R$ {venda[3]:.2f}')

cursor.execute("SELECT pr.categoria, SUM(i.quantidade), SUM(i.quantidade * i.preco_unitario) FROM produtos AS pr LEFT JOIN itens_pedido AS i ON pr.id_produto = i.id_produto LEFT JOIN pedidos AS p ON i.id_pedido = p.id_pedido WHERE p.status_pedido <> 'Cancelado' GROUP BY pr.categoria")
vendas_por_categoria = cursor.fetchall()
for venda_por_categoria in vendas_por_categoria:
    print(f'Categoria: {venda_por_categoria[0]} | Quantidade: {venda_por_categoria[1]} | Valor total vendido: R$ {venda_por_categoria[2]:.2f}')

cursor.close()
conexao.close()