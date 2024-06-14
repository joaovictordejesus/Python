# Verifica se um ano é bissexto

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não Bissexto")
    
#Teste
print("Teste dos anos 1900, 2000,2016 e 2017 abaixo:")
test_anos = [1900, 2000, 2016, 2017]
for ano in test_anos:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano}: Bissexto")
    else:
        print(f"{ano}: Não Bissexto")
