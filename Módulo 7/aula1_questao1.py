def escada_nome():
    nome = input("Digite seu nome: ")
    for i in range(1, len(nome) + 1):
        print(nome[:i])

escada_nome()