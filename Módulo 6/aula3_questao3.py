import random

lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

max_negativos = 0
inicio_intervalo = 0
for i in range(len(lista) - 4 + 1):  
    sub_lista = lista[i:i+4]
    negativos = sum(1 for x in sub_lista if x < 0)
    if negativos > max_negativos:
        max_negativos = negativos
        inicio_intervalo = i

del lista[inicio_intervalo:inicio_intervalo+4]
print("Editada:", lista)