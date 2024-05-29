# Verificar se pelo menos uma é maior de 17
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

podem_entrar = idade_juliana > 17 or idade_cris > 17
print(podem_entrar)
