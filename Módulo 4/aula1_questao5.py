# Define a média de idades de um determinado grupo.

N = int(input("Digite a quantidade de participantes: "))

soma_idades = 0


contador = 0

while contador < N:
    idade = int(input(f"Digite a idade do participante {contador+1}: "))
    soma_idades += idade
    contador += 1

media_idades = soma_idades / N

print("A média das idades é:", media_idades)
