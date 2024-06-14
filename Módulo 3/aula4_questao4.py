# Cálculo do valor do frete

distancia = float(input("Digite a distância da entrega em quilômetros: "))
peso = float(input("Digite o peso do pacote em quilogramas: "))

if distancia <= 100:
    custo_por_kg = 1.00
elif distancia <= 300:
    custo_por_kg = 1.50
else:
    custo_por_kg = 2.00

frete = distancia * custo_por_kg

# Para pacotes com mais de 10 kg, acrescenta R$ 10

if peso > 10:
    frete += 10  

print(f"O valor do frete é: R${frete:.2f}")
