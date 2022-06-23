# Ex06- Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a
#       média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

media = []
nota = 0
i = 0

while i < 2:

    for j in range(4):
        nota = nota + float(input(f"Digite a {j+1}ª nota do {i+1}º Aluno: "))

    media.append(nota/4)
    nota = 0
    i = i+1

print("\n\nAlunos com media >= 7 :")

for j, k in enumerate(media, 1):
    if k >= 7:
        print(f"O {j}º aluno teve média: {k}")
