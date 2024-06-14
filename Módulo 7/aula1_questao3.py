#Conta quantos espaços tem em uma frase.

def contar_espacos():
    frase = input("Digite a frase: ")
    espacos = frase.count(' ')
    print(f"Espaços em branco: {espacos}")

contar_espacos()
