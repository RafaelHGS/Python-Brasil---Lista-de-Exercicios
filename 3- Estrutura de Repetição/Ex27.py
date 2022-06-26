"""
    Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de 
    turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

"""


def appendTurma(qtdTurmas=int, turma=list):
    for i in range(qtdTurmas):
        while True:
            qtdAlunos = int(input(f"Quantidade de alunos da turma {i+1}: \n"))
            if qtdAlunos <= 0 or qtdAlunos > 40:
                continue
            else:
                break
        turma.append(qtdAlunos)
    return turma


if __name__ == "__main__":
    turmas = []
    qtdTurmas = int(input("Quantas turmas ?\n"))

    turmas = appendTurma(qtdTurmas, turmas)

    media = sum(turmas)/len(turmas)
    print(f"Média de alunos por turma: {round(media)}")
