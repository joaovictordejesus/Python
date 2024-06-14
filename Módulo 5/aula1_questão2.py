# Gere n valores inteiros aleatórios entre 0 e 100 e calcula a raíz quadrada da soma destes valores.

import random
import math

n = int(input("Insira o valor de n: "))

valores_aleatorios = [random.randint(0, 100) for _ in range(n)]
print("Valores aleatórios gerados:", valores_aleatorios)

soma_valores = sum(valores_aleatorios)
print("Soma dos valores:", soma_valores)

raiz_quadrada = math.sqrt(soma_valores)
print("Raiz quadrada da soma dos valores:", raiz_quadrada)
