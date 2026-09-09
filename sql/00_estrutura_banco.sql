PRAGMA foreign_keys = ON;

BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "atendimentos" (
	"id_atendimento"	INTEGER,
	"id_pedido"	INTEGER NOT NULL,
	"canal"	TEXT NOT NULL,
	"motivo_atendimento"	TEXT NOT NULL,
	"data_abertura"	TEXT NOT NULL,
	"data_fechamento"	TEXT,
	"status_atendimento"	TEXT NOT NULL,
	"nota_satisfacao"	INTEGER,
	PRIMARY KEY("id_atendimento" AUTOINCREMENT),
	FOREIGN KEY("id_pedido") REFERENCES "pedidos"("id_pedido")
);
CREATE TABLE IF NOT EXISTS "clientes" (
	"id_cliente"	INTEGER,
	"nome"	TEXT NOT NULL,
	"cidade"	TEXT NOT NULL,
	"estado"	TEXT NOT NULL,
	"data_cadastro"	TEXT NOT NULL,
	PRIMARY KEY("id_cliente" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "entregas" (
	"id_entrega"	INTEGER,
	"id_pedido"	INTEGER NOT NULL,
	"transportadora"	TEXT NOT NULL,
	"data_envio"	TEXT,
	"data_prevista"	TEXT NOT NULL,
	"data_entrega"	TEXT,
	"status_entrega"	TEXT NOT NULL,
	PRIMARY KEY("id_entrega" AUTOINCREMENT),
	FOREIGN KEY("id_pedido") REFERENCES "pedidos"("id_pedido")
);
CREATE TABLE IF NOT EXISTS "itens_pedido" (
	"id_item"	INTEGER,
	"id_pedido"	INTEGER NOT NULL,
	"id_produto"	INTEGER NOT NULL,
	"quantidade"	INTEGER NOT NULL,
	"preco_unitario"	REAL NOT NULL,
	PRIMARY KEY("id_item" AUTOINCREMENT),
	FOREIGN KEY("id_pedido") REFERENCES "pedidos"("id_pedido"),
	FOREIGN KEY("id_produto") REFERENCES "produtos"("id_produto")
);
CREATE TABLE IF NOT EXISTS "pagamentos" (
	"id_pagamento"	INTEGER,
	"id_pedido"	INTEGER NOT NULL,
	"metodo_pagamento"	TEXT NOT NULL,
	"status_pagamento"	TEXT NOT NULL,
	"valor_pago"	REAL NOT NULL,
	"data_pagamento"	TEXT,
	PRIMARY KEY("id_pagamento" AUTOINCREMENT),
	FOREIGN KEY("id_pedido") REFERENCES "pedidos"("id_pedido")
);
CREATE TABLE IF NOT EXISTS "pedidos" (
	"id_pedido"	INTEGER,
	"id_cliente"	INTEGER NOT NULL,
	"data_pedido"	TEXT NOT NULL,
	"status_pedido"	TEXT NOT NULL,
	"valor_total"	REAL NOT NULL,
	"motivo_cancelamento"	TEXT,
	PRIMARY KEY("id_pedido" AUTOINCREMENT),
	FOREIGN KEY("id_cliente") REFERENCES "clientes"("id_cliente")
);
CREATE TABLE IF NOT EXISTS "produtos" (
	"id_produto"	INTEGER,
	"nome_produto"	TEXT NOT NULL,
	"categoria"	TEXT NOT NULL,
	"preco"	REAL NOT NULL,
	"quantidade_estoque"	INTEGER NOT NULL,
	PRIMARY KEY("id_produto" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "reembolsos" (
	"id_reembolso"	INTEGER,
	"id_pagamento"	INTEGER NOT NULL,
	"data_solicitacao"	TEXT NOT NULL,
	"data_conclusao"	TEXT,
	"valor_reembolso"	REAL NOT NULL,
	"motivo_reembolso"	TEXT NOT NULL,
	"status_reembolso"	TEXT NOT NULL,
	PRIMARY KEY("id_reembolso" AUTOINCREMENT),
	FOREIGN KEY("id_pagamento") REFERENCES "pagamentos"("id_pagamento")
);
COMMIT;
