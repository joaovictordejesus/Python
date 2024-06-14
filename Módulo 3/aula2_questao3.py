#  Verificar se o usuário pode ingressar no clube juvenil de jogos de tabuleiro

idade = int(input("Digite sua idade: "))
jogou_3_ou_mais = input("Já jogou pelo menos 3 jogos de tabuleiro? ").strip().lower() == "true"
vitorias = int(input("Quantos jogos já venceu? "))

pode_ingressar = 16 <= idade <= 18 and jogou_3_ou_mais and vitorias >= 1
print("Apto para ingressar no clube de jogos de tabuleiro:", pode_ingressar)
