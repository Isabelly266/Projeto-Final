# Análise de Vendas - Zara

Trabalho prático de Python usando os módulos `csv` e `json`.

## Contexto da empresa
A **Zara** é uma rede de moda que vende roupas femininas, masculinas e infantis, além de acessórios.
Neste trabalho, a administração de uma loja quer decidir o próximo mês com base nas vendas da
**primeira semana de abril de 2026 (1 a 7 de abril)** e nas metas definidas pela gerência.

> Todos os dados (vendas, preços, metas, orçamento e nome do gerente) são **fictícios**,
> criados apenas para este exercício acadêmico.

## Arquivos
| Arquivo | Descrição |
|---|---|
| `vendas.csv` | 51 registros de vendas (separador `;`) com data, produto, categoria, quantidade, preço unitário, vendedor e forma de pagamento. Representa a planilha enviada pela equipe de vendas. |
| `configuracao.json` | Dados da gerência: empresa, unidade, gerente, período, meta de faturamento, meta de unidades, metas por categoria, orçamento de despesas e despesas previstas por tipo. |
| `analise.py` | Programa que lê os dois arquivos, faz os cálculos e mostra o relatório. |

## Como o programa funciona
1. Lê o `configuracao.json` com o módulo `json`.
2. Lê o `vendas.csv` com o módulo `csv` e converte quantidade e preço para número.
3. Calcula o valor total de cada venda (quantidade x preço unitário).
4. Calcula o faturamento total, as unidades vendidas, o número de registros e a média por venda.
5. Identifica o produto com maior quantidade vendida.
6. Calcula o faturamento por produto e por categoria.
7. Compara os resultados com a meta de faturamento, a meta de unidades, as metas por categoria e o orçamento de despesas.
8. Mostra mensagens claras para a administração, como "Meta atingida" ou "Meta não atingida".

## Como executar
É necessário ter o Python 3 instalado. Não precisa instalar nenhuma biblioteca.

1. Baixe os três arquivos (`analise.py`, `vendas.csv` e `configuracao.json`) e deixe todos na **mesma pasta**, com esses nomes exatos.
2. Abra o terminal e entre na pasta do projeto, por exemplo:
   ```bash
   cd "Desktop/Projeto final Python"
   ```
3. Execute o programa:

   **macOS / Linux**
   ```bash
   python3 analise.py
   ```

   **Windows**
   ```bash
   python analise.py
   ```

### Problemas comuns
- **`can't open file ... No such file or directory`**: o terminal não achou o arquivo. Confira com `ls` (macOS/Linux) ou `dir` (Windows) se `analise.py`, `vendas.csv` e `configuracao.json` estão na pasta onde você está.
- **Caminho completo com aspas**: use aspas simples **ou** duplas, nunca as duas juntas. Exemplo correto: `python3 "/Users/nome/Desktop/Projeto final Python/analise.py"`.
- **`FileNotFoundError`**: o programa procura o CSV e o JSON na pasta onde o comando é executado. Rode o comando de dentro da pasta do projeto.

## Exemplo do resultado
```
RELATÓRIO GERENCIAL - Zara
Período analisado: 1 a 7 de abril de 2026

Registros de venda: 51
Unidades vendidas:  179
Faturamento total:  R$ 31641,50

Produto mais vendido: Jaqueta Jeans (27 unidades)

Meta NÃO atingida: 95.9% da meta (faltaram R$ 1358,50).
```

## Integrantes
- Nome do aluno(a) - descreva aqui a sua contribuição
