#o random.randit gera os valores aleatórios 
import random

num_elementos = random.randint(5, 20)

elementos = [random.randint(1, 10) for _ in range(num_elementos)]

print("Lista elementos:", elementos)

soma = sum(elementos)
print("Soma dos valores:", soma)

media = soma / num_elementos
print("Média dos valores:", media)