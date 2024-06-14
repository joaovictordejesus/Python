# Verificar se a soma de dois números é par ou ímpar

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2

if soma % 2 == 0:
    print("A soma é par.")
else:
    print("A soma é ímpar.")
