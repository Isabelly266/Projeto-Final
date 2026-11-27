 # Análise de Vendas da Zara

Trabalho prático de Python usando arquivos CSV e JSON.

## A empresa
Nós escolhemos a **Zara**, que é uma loja de roupas femininas, masculinas e infantis e também de acessórios. Imaginamos que a administração de uma loja precisa decidir o que fazer no próximo mês e, para isso, recebeu informações de dois lugares:

- a **equipe de vendas** mandou uma planilha com as vendas de 1 a 7 de abril de 2026;
- a **gerência** mandou as metas e as informações da empresa.

Nós usamos só uma semana porque a Zara vende muito, então em poucos dias já dá bastante venda para analisar.

Todos os dados (vendas, preços, metas, orçamento e nome do gerente) são inventados por nós, só para este trabalho.

## Os arquivos
- `vendas.csv`: tem 51 vendas. Cada linha mostra a data, o produto, a categoria, a quantidade, o preço unitário, o vendedor e a forma de pagamento.
- `configuracao.json`: tem as informações da gerência, como o nome da empresa, a loja, o gerente, o período, a meta de faturamento, a meta de unidades, as metas de cada categoria, o orçamento de despesas e as despesas previstas.
- `analise.py`: é o programa em Python que lê os dois arquivos, faz as contas e mostra o relatório.
- `README.md`: este arquivo, que explica o trabalho.

## Como o programa funciona
O programa usa os módulos `csv` e `json` do Python e faz o seguinte:

1. Lê o arquivo `configuracao.json`.
2. Lê o arquivo `vendas.csv` e transforma a quantidade e o preço em números.
3. Calcula o valor total de cada venda, multiplicando a quantidade pelo preço unitário.
4. Calcula o faturamento total, o total de unidades vendidas, o número de registros e a média de cada venda.
5. Descobre qual produto vendeu mais unidades.
6. Calcula quanto cada produto e cada categoria faturou.
7. Compara tudo com o que está no JSON: a meta de faturamento, a meta de unidades, as metas por categoria e o orçamento de despesas.
8. Mostra os resultados com mensagens fáceis de entender, como "Meta ATINGIDA" ou "Meta NÃO atingida".

O código tem comentários explicando o que cada parte faz.

## Como rodar
Precisa ter o Python 3 instalado. Não precisa instalar mais nada.

1. Deixe os arquivos `analise.py`, `vendas.csv` e `configuracao.json` na mesma pasta.
2. Abra o terminal dentro dessa pasta.
3. Digite:

```bash
python3 analise.py
```

No Windows, o comando é `python analise.py`.

## O resultado
Quando o programa roda, ele mostra um relatório assim:

```
RELATÓRIO GERENCIAL - Zara
Período analisado: 1 a 7 de abril de 2026

Registros de venda: 51
Unidades vendidas:  179
Faturamento total:  R$ 31641,50

Produto mais vendido: Jaqueta Jeans (27 unidades)

Meta NÃO atingida: 95.9% da meta (faltaram R$ 1358,50).
```

Ou seja, a loja vendeu 179 unidades e faturou R$ 31.641,50, que ficou um pouco abaixo da meta de R$ 33.000,00. O produto que mais saiu foi a Jaqueta Jeans.

## Integrantes e o que cada um fez
- **Giovana Bedone de Castro:** criou os dados e o arquivo `vendas.csv`.
- **Isabelly Tiemy Matsuura da Silva:** fez o código em Python e escreveu o `README.md`.
- **Rafaella de Almeida Reis:** escreveu o `README.md` e o `configuracao-2.json`
