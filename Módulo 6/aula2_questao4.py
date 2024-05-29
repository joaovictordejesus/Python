#Combinação de duas listas de forma intercalada
def intercalar_listas(lista1, lista2):
    intercalada = []
    for i in range(min(len(lista1), len(lista2))):
        intercalada.append(lista1[i])
        intercalada.append(lista2[i])
    intercalada.extend(lista1[i+1:])
    intercalada.extend(lista2[i+1:])
    return intercalada

n1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = [int(input(f"Digite o {i+1}º elemento da lista 1: ")) for i in range(n1)]

n2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = [int(input(f"Digite o {i+1}º elemento da lista 2: ")) for i in range(n2)]

lista_intercalada = intercalar_listas(lista1, lista2)

print("Lista intercalada:", lista_intercalada)