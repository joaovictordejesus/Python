# Define quais os alunos estão aprovados, sendo o mínimo 60 para ser aprovado.

alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

aprovados = [alunos[i] for i in range(len(notas)) if notas[i] >= 60]

print("O aluno aprovado é:",aprovados)
