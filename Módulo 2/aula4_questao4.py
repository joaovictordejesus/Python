print("Cálculo da menor quantidade possível de notas necessárias para pagar determinado valor.")
quantia = int(input("Digite a quantia em reais: "))

notas = [100, 50, 20, 10, 5, 2, 1]
quantidades = []
for nota in notas:
    quantidade_nota = quantia // nota
    quantidades.append(quantidade_nota)
    quantia %= nota

for i in range(len(notas)):
    print(f'{quantidades[i]} nota(s) de R${notas[i]:,.2f}')
