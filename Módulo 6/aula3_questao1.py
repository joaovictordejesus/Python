def solicita_numeros():
    numeros = []
    while len(numeros) < 4:
        try:
            num = int(input("Digite um número inteiro (ou 'P' para parar): "))
            numeros.append(num)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
    while True:
        try:
            num = int(input("Digite um número inteiro (ou 'P' para parar): "))
            numeros.append(num)
        except ValueError:
            break
    return numeros

numeros = solicita_numeros()

print("Lista original:", numeros)
print("Os 3 primeiros elementos:", numeros[:3])
print("Os 2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])