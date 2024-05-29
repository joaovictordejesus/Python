def analisar_roteiro():
    with open("estomago.txt", "r", encoding='latin-1') as file:
        linhas = file.readlines()
    print("Primeiras 25 linhas do texto:")
    for linha in linhas[:25]:
        print(linha.strip())
    num_linhas = len(linhas)
    print(f"\nNúmero total de linhas: {num_linhas}")
    linha_mais_longa = max(linhas, key=len)
    print(f"\nLinha com maior número de caracteres: {linha_mais_longa.strip()}")
    texto_completo = " ".join(linhas).lower()
    num_mencoes_nonato = texto_completo.count("nonato")
    num_mencoes_iria = texto_completo.count("íria")
    print(f"\nNúmero de menções a 'Nonato': {num_mencoes_nonato}")
    print(f"Número de menções a 'Íria': {num_mencoes_iria}")

analisar_roteiro()