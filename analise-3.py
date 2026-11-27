

import csv
import json


def mostrar_dinheiro(valor):
    texto = f"{valor:.2f}"
    texto = texto.replace(".", ",")
    return "R$ " + texto


with open("configuracao-2.json") as arquivo_json:
    config = json.load(arquivo_json)


vendas = []  

with open("vendas-2.csv") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv, delimiter=";")

    for linha in leitor:
        quantidade = int(linha["quantidade"])
        preco_unitario = float(linha["preco_unitario"])  

        
        total = quantidade * preco_unitario

        venda = {
            "produto": linha["produto"],
            "categoria": linha["categoria"],
            "quantidade": quantidade,
            "preco_unitario": preco_unitario,
            "total": total,
        }
        vendas.append(venda)


faturamento_total = 0
unidades_vendidas = 0
for venda in vendas:
    faturamento_total = faturamento_total + venda["total"]
    unidades_vendidas = unidades_vendidas + venda["quantidade"]

numero_registros = len(vendas)
media_por_venda = faturamento_total / numero_registros


unidades_por_produto = {}
faturamento_por_produto = {}
faturamento_por_categoria = {}

for venda in vendas:
    produto = venda["produto"]
    categoria = venda["categoria"]

    
    if produto in unidades_por_produto:
        unidades_por_produto[produto] = unidades_por_produto[produto] + venda["quantidade"]
        faturamento_por_produto[produto] = faturamento_por_produto[produto] + venda["total"]
    else:
        unidades_por_produto[produto] = venda["quantidade"]
        faturamento_por_produto[produto] = venda["total"]

    
    if categoria in faturamento_por_categoria:
        faturamento_por_categoria[categoria] = faturamento_por_categoria[categoria] + venda["total"]
    else:
        faturamento_por_categoria[categoria] = venda["total"]


produto_mais_vendido = ""
maior_quantidade = 0
for produto in unidades_por_produto:
    if unidades_por_produto[produto] > maior_quantidade:
        maior_quantidade = unidades_por_produto[produto]
        produto_mais_vendido = produto


meta = config["meta_faturamento"]
orcamento = config["orcamento_despesas"]
meta_unidades = config["meta_unidades"]

percentual_meta = faturamento_total / meta * 100
percentual_unidades = unidades_vendidas / meta_unidades * 100
resultado_estimado = faturamento_total - orcamento


print("=" * 55)
print("RELATÓRIO GERENCIAL - " + config["empresa"])
print("Unidade: " + config["unidade"] + " | Gerente: " + config["gerente"])
print("Período analisado: " + config["periodo"])
print("=" * 55)

print("\nRegistros de venda:", numero_registros)
print("Unidades vendidas: ", unidades_vendidas)
print("Faturamento total: ", mostrar_dinheiro(faturamento_total))
print("Média por venda:   ", mostrar_dinheiro(media_por_venda))

print("\nProduto mais vendido:", produto_mais_vendido,
      "(" + str(maior_quantidade) + " unidades)")

print("\nFaturamento por produto:")
for produto in faturamento_por_produto:
    print("  -", produto + ":", mostrar_dinheiro(faturamento_por_produto[produto]))

print("\nFaturamento por categoria:")
for categoria in faturamento_por_categoria:
    print("  -", categoria + ":", mostrar_dinheiro(faturamento_por_categoria[categoria]))


print("\n--- Comparação com a meta ---")
print("Meta de faturamento:", mostrar_dinheiro(meta))
if faturamento_total >= meta:
    print(f"Meta ATINGIDA! Faturamento em {percentual_meta:.1f}% da meta.")
else:
    falta = meta - faturamento_total
    print(f"Meta NÃO atingida: {percentual_meta:.1f}% da meta "
          f"(faltaram {mostrar_dinheiro(falta)}).")


print(f"\nMeta de unidades: {meta_unidades} | Vendidas: {unidades_vendidas} "
      f"({percentual_unidades:.1f}% da meta)")


print("\n--- Metas por categoria ---")
metas_categorias = config["metas_categorias"]
for categoria in metas_categorias:
    meta_categoria = metas_categorias[categoria]
    vendido = faturamento_por_categoria[categoria]
    percentual = vendido / meta_categoria * 100
    if vendido >= meta_categoria:
        situacao = "atingida"
    else:
        situacao = "não atingida"
    print(f"  - {categoria}: {mostrar_dinheiro(vendido)} de "
          f"{mostrar_dinheiro(meta_categoria)} ({percentual:.1f}%) - meta {situacao}")


print("\n--- Faturamento x orçamento de despesas ---")
print("Orçamento previsto de despesas:", mostrar_dinheiro(orcamento))
despesas = config["despesas_previstas"]
for tipo in despesas:
    print("  -", tipo + ":", mostrar_dinheiro(despesas[tipo]))

if resultado_estimado >= 0:
    print("Resultado estimado positivo:", mostrar_dinheiro(resultado_estimado))
else:
    print("Atenção: resultado estimado negativo:", mostrar_dinheiro(resultado_estimado))
print("=" * 55)
