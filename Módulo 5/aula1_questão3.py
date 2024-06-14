# Adivinhação de um número aleatório

import random

def adivinhar_numero():
    numero_secreto = random.randint(1, 10)
    palpite = None
    
    while palpite != numero_secreto:
        palpite = int(input("Adivinhe o número entre 1 e 10: "))
        if palpite < numero_secreto:
            print("Muito baixo, tente novamente!")
        elif palpite > numero_secreto:
            print("Muito alto, tente novamente!")
        else:
            print(f"Correto! O número é {numero_secreto}.")

adivinhar_numero()
