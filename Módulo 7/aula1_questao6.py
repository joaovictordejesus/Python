def encontrar_anagramas():
    frase = input("Digite uma frase: ").split()
    palavra_objetivo = input("Digite a palavra objetivo: ")
    sorted_objetivo = sorted(palavra_objetivo)
    anagramas = [palavra for palavra in frase if sorted(palavra) == sorted_objetivo]
    print(f"Anagramas: {anagramas}")

encontrar_anagramas()