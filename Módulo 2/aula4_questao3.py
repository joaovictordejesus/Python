# Calcula Preço de comprar online

print("Cálculo de preço de uma compra online")
produtos = []
for i in range(3):
    nome = input(f'Digite o nome do produto: {i+1}: ')
    preco_unitario = float(input(f'Digite o preço unitário do produto {i+1}: '))
    quantidade = int(input(f'Digite a quantidade do produto {i+1}: '))
    produtos.append((nome, preco_unitario, quantidade))

preco_total_compra = sum(preco * quantidade for _, preco, quantidade in produtos)

print(f'Total: R${preco_total_compra:,.2f}')
