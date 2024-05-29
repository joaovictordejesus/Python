def contar_vogais():
    frase = input("Digite uma frase: ")
    vogais = 'aeiouAEIOUáéíóúÁÉÍÓÚãÃ'
    indices = [i for i, char in enumerate(frase) if char in vogais]
    print(f"{len(indices)} vogais")
    print(f"Índices {indices}")

contar_vogais()