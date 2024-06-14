# Solicitar a frase do usuário depois mostra Lista de vogais e consoantes e após isso Imprimir as listas

frase = input("Digite uma frase: ")

vogais = sorted([char for char in frase if char.lower() in 'aeiou'])
consoantes = [char for char in frase if char.lower() in 'bcdfghjklmnpqrstvwxyz']

print("Vogais:", vogais)
print("Consoantes:", consoantes)
