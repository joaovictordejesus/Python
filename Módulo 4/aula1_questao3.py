# Define se o aluno está aprovado, em recuperação ou reprovado. Maior ou igual a 60 é Aprovado, menor do que 60, mas maior que 40,é recuperação, já menor que 40 já é reprovado. 

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))


m = (n1 + n2 + n3) / 3

if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
elif m < 40:
    print("Reprovado")


print("Fim")
