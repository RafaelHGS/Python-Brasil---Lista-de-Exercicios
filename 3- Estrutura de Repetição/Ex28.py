"""
    Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor
    médio gasto em cada um deles.
    O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""


def appendDVD(qtdDVD=int, DVD=list):
    for i in range(qtdDVD):
        valorDVDs = float(input(f"Valor do {i+1}º DVD da coleção: \n"))
        DVD.append(valorDVDs)
    return DVD


if __name__ == "__main__":
    DVDs = []
    qtdDVDs = int(input("Quantos DVD's/CD's ?\n"))

    DVDs = appendDVD(qtdDVDs, DVDs)

    media = sum(DVDs)/len(DVDs)

    print(f"Valor total gasto nos DVD's/CD's: {sum(DVDs)}")
    print(f"Média do valor gasto por DVD: {round(media, 2)}")
