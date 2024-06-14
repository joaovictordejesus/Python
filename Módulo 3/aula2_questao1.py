# Verificar ambas são maiores de 17

idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

podem_entrar = idade_juliana > 17 and idade_cris > 17
print(podem_entrar)
