SELECT p.id_pedido, c.nome, p.data_pedido, p.status_pedido, p.valor_total, i.quantidade,
i.preco_unitario, pr.nome_produto, pr.categoria
FROM pedidos AS p
INNER JOIN clientes AS c
ON p.id_cliente = c.id_cliente
INNER JOIN itens_pedido AS i
ON p.id_pedido = i.id_pedido
INNER JOIN produtos AS pr
ON i.id_produto = pr.id_produto;