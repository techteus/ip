turma = int(input("Digite o número de alunos na turma: "))
soma = 0

for i in range(turma):
    idade = int(input(f"Digite a idade do aluno {i + 1}: "))
    soma += idade

media = soma / turma

if media <= 25:
    print("A turma é jovem.")

elif media <= 60:
    print("A turma é adulta.")

else:
    print("A turma é idosa.")
