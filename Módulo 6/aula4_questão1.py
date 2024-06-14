# x definido como 0 para inciar o código, depois, o código define os números pares entre 20 e 50, os quadrados de 1 a 9, os divisíveis por 7 de 1 a 100 e paridade

x=0 

pares_20_50 = [i for i in range(20, 51) if i % 2 == 0]
print("Pares entre 20 e 50:", pares_20_50)

quadrados = [i**2 for i in range(1, 10)]
print("Quadrados de 1 a 9:", quadrados)

divisiveis_por_7 = [i for i in range(1, 101) if i % 7 == 0]
print("Divisíveis por 7 entre 1 e 100:", divisiveis_por_7)
6
paridade = ['par' if i % 2 == 0 else 'ímpar' for i in range(0, x, 3)]
