INSERT INTO clientes (nome, cidade, estado, data_cadastro)
 VALUES ('Bruna Lima', 'Guarulhos', 'SP', '2026-09-10');

INSERT INTO clientes (nome, cidade, estado, data_cadastro)
 VALUES ('Carlos Mendes', 'Campinas', 'SP', '2026-09-11');

INSERT INTO pedidos (id_cliente, data_pedido, status_pedido, valor_total)
 VALUES (2, '2026-09-10', 'Enviado', 399.90);

INSERT INTO pedidos (id_cliente, data_pedido, status_pedido, valor_total, motivo_cancelamento)
 VALUES (3, '2026-09-11', 'Cancelado', 129.90, 'Pagamento não aprovado');
