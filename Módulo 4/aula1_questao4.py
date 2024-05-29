
n = int(input("Digite um valor para n: "))

maior = 0

while n > 0:
  
    x = int(input("Digite um número x: "))
   
    if x > maior:
        maior = x
   
    n -= 1

print("O maior número é:", maior)
