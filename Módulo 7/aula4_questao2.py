# Abre uma frase de um arquivo em txt

import re
def processar_frase():
    with open("frase.txt", "r") as file:
        conteudo = file.read()
    palavras = re.findall(r'\b[A-Za-z]+\b', conteudo)
    with open("palavras.txt", "w") as file:
        for palavra in palavras:
            file.write(palavra + '\n')
    with open("palavras.txt", "r") as file:
        print(file.read())
processar_frase()
