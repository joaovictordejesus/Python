# Solicitar a frase do usuário
frase = input("Digite uma frase: ")

# Lista de vogais e consoantes
vogais = sorted([char for char in frase if char.lower() in 'aeiou'])
consoantes = [char for char in frase if char.lower() in 'bcdfghjklmnpqrstvwxyz']

# Imprimir as listas
print("Vogais:", vogais)
print("Consoantes:", consoantes)