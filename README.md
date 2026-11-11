# Análise de Operações de E-commerce e Atendimento

Este projeto analisa dados simulados de uma operação de e-commerce, incluindo vendas, cancelamentos, entregas, pagamentos, atendimentos e reembolsos. Usei SQL para estruturar e consultar o banco SQLite, Python para executar as análises e exportar os resultados de vendas em CSV, e Excel para comparar as vendas por produto e por categoria em gráficos. 

## Estrutura do projeto

- `sql/`: criação das tabelas, carga dos dados simulados e consulta de pedidos.
- `python/`: criação do banco SQLite, análises e exportação dos resultados de vendas em CSV.
- `excel/`: planilha com tabelas e gráficos de vendas por produto e por categoria.

## Análises realizadas

- Quantidade e valor total dos pedidos.
- Pedidos cancelados e seus motivos.
- Situação das entregas.
- Pagamentos aprovados e recusados.
- Atendimentos resolvidos e média de satisfação.
- Quantidade e valor dos reembolsos pendentes.
- Quantidade de unidades e valor vendido por produto e categoria.

Na análise de vendas, os pedidos cancelados são desconsiderados.

## Como executar

É necessário ter Python 3 instalado. Os scripts usam apenas bibliotecas padrão do Python.

Execute os comandos no terminal, a partir da pasta principal do projeto.

### 1. Criar o banco e carregar os dados

```bash
python python/00_criar_banco.py
```

Atenção: esse script apaga o banco existente e o recria com os dados simulados. Feche qualquer programa que esteja usando o banco antes de executá-lo.

### 2. Executar as análises

Os scripts de `02_analise_pedidos.py` a `08_analise_vendas.py` podem ser executados individualmente. Por exemplo:

```bash
python python/08_analise_vendas.py
```

### 3. Exportar os resultados de vendas

```bash
python python/09_exportar_vendas.py
```

Esse comando cria ou substitui os arquivos `vendas_por_produto.csv` e `vendas_por_categoria.csv` na pasta principal.

A planilha na pasta `excel/` contém as visualizações montadas manualmente e não é atualizada automaticamente pelo script.

## Resultados com os dados simulados

| Indicador | Resultado |
| --- | --- |
| Valor vendido, excluindo pedidos cancelados | R$ 649,80 |
| Unidades vendidas, excluindo pedidos cancelados | 2 |
| Média das notas de satisfação | 4,50 |
| Reembolsos pendentes | 1 |
| Valor total dos reembolsos pendentes | R$ 129,90 |

A base é pequena e foi criada para estudo. Esses resultados demonstram o funcionamento das análises e não representam uma operação real.