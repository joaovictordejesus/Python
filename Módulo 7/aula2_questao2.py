def substituir_vogais():
    frase = input("Digite uma frase: ")
    vogais = "aeiouAEIOUÁáÉéÍíÓóÚúãÃ"
    frase_modificada = ''.join(['*' if char in vogais else char for char in frase])
    print(f"Frase modificada: {frase_modificada}")

substituir_vogais()