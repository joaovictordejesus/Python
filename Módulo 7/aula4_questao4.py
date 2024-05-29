import random

def imprime_enforcado(erros):
    with open("gabarito_enforcado.txt", "r") as file:
        estagios = file.readlines()
    print(estagios[erros])
def jogar_forca():
    with open("gabarito_forca.txt", "r") as file:
        palavras = [linha.strip() for linha in file.readlines()]
    palavra = random.choice(palavras).upper()
    tentativas = 6
    letras_acertadas = ["_"] * len(palavra)
    letras_erradas = []
    while tentativas > 0 and "_" in letras_acertadas:
        print(" ".join(letras_acertadas))
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        chute = input("Digite uma letra: ").upper()
        if chute in letras_erradas or chute in letras_acertadas:
            print("Você já tentou essa letra.")
            continue
        if chute in palavra:
            for i, letra in enumerate(palavra):
                if letra == chute:
                    letras_acertadas[i] = chute
        else:
            letras_erradas.append(chute)
            tentativas -= 1
            imprime_enforcado(tentativas)
    if "_" not in letras_acertadas:
        print(f"Parabéns! Você acertou a palavra: {palavra}")
    else:
        print(f"Você perdeu! A palavra era: {palavra}")

jogar_forca()