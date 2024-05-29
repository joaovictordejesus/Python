def salvar_frase():
    frase = input("Digite uma frase: ")
    with open("frase.txt", "w") as file:
        file.write(frase)
    import os
    caminho_completo = os.path.abspath("frase.txt")
    print(f"Frase salva em {caminho_completo}")

salvar_frase()