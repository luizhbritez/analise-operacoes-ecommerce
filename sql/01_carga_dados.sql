PRAGMA foreign_keys = ON;

BEGIN TRANSACTION;

INSERT INTO produtos (nome_produto, categoria, preco, quantidade_estoque)
 VALUES ('Teclado mecânico RGB', 'Informática', 249.90, 35);

INSERT INTO produtos (nome_produto, categoria, preco, quantidade_estoque)
 VALUES ('Headset gamer', 'Áudio', 399.90, 20);

INSERT INTO produtos (nome_produto, categoria, preco, quantidade_estoque)
 VALUES ('Mouse sem fio', 'Informática', 129.90, 50);

INSERT INTO clientes (nome, cidade, estado, data_cadastro)
 VALUES ('Ana Souza', 'São Paulo', 'SP', '2026-09-07');
INSERT INTO pedidos (id_cliente, data_pedido, status_pedido, valor_total)
 VALUES (1, '2026-09-07', 'Aprovado', 249.90);

INSERT INTO itens_pedido (id_pedido, id_produto, quantidade, preco_unitario)
 VALUES (1, 1, 1, 249.90);

INSERT INTO entregas (id_pedido, transportadora, data_envio, data_prevista, data_entrega, status_entrega)
 VALUES (1, 'Jadlog', '2026-09-08', '2026-09-12', NULL, 'Em trânsito');

INSERT INTO pagamentos (id_pedido, metodo_pagamento, status_pagamento, valor_pago, data_pagamento)
 VALUES (1, 'Cartão de crédito', 'Aprovado', 249.90, '2026-09-07');

INSERT INTO atendimentos (id_pedido, canal, motivo_atendimento, data_abertura, data_fechamento, status_atendimento, nota_satisfacao)
 VALUES (1, 'Chat', 'Acompanhamento da entrega', '2026-09-09 10:15:00', '2026-09-09 10:27:00', 'Resolvido', 5);

INSERT INTO clientes (nome, cidade, estado, data_cadastro)
 VALUES ('Bruna Lima', 'Guarulhos', 'SP', '2026-09-10');
INSERT INTO pedidos (id_cliente, data_pedido, status_pedido, valor_total)
 VALUES (2, '2026-09-10', 'Enviado', 399.90);

INSERT INTO itens_pedido (id_pedido, id_produto, quantidade, preco_unitario)
 VALUES (2, 2, 1, 399.90);

INSERT INTO entregas (id_pedido, transportadora, data_envio, data_prevista, data_entrega, status_entrega)
 VALUES (2, 'Loggi', '2026-09-11', '2026-09-26', NULL, 'Em trânsito');

INSERT INTO pagamentos (id_pedido, metodo_pagamento, status_pagamento, valor_pago, data_pagamento)
 VALUES (2, 'Pix', 'Aprovado', 399.90, '2026-09-10');

INSERT INTO clientes (nome, cidade, estado, data_cadastro)
 VALUES ('Carlos Mendes', 'Campinas', 'SP', '2026-09-11');
INSERT INTO pedidos (id_cliente, data_pedido, status_pedido, valor_total, motivo_cancelamento)
 VALUES (3, '2026-09-11', 'Cancelado', 129.90, 'Pagamento não aprovado');

INSERT INTO itens_pedido (id_pedido, id_produto, quantidade, preco_unitario)
 VALUES (3, 3, 1, 129.90);

INSERT INTO pagamentos (id_pedido, metodo_pagamento, status_pagamento, valor_pago, data_pagamento)
 VALUES (3, 'Cartão de crédito', 'Recusado', 0.00, NULL);

INSERT INTO atendimentos (id_pedido, canal, motivo_atendimento, data_abertura, data_fechamento, status_atendimento, nota_satisfacao)
 VALUES (3, 'Chat', 'Pagamento não aprovado', '2026-09-11 11:00:00', '2026-09-11 11:20:00', 'Resolvido', 4);

COMMIT;