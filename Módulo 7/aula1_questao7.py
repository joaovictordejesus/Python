# Criptografia de nomes

import random

def encrypt(nomes):
    n = random.randint(1, 10)
    nomes_criptografados = []
    for nome in nomes:
        nome_cript = ''.join(chr((ord(c) - 33 + n) % 94 + 33) for c in nome)
        nomes_criptografados.append(nome_cript)
    return nomes_criptografados, n

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave = encrypt(nomes)
print(f"Chave de criptografia: {chave}")
print(f"Nomes criptografados: {nomes_cript}")
