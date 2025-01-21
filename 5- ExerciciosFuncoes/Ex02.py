"""
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""


def piramide(camadasPirade = int):
    for i in range(1, camadasPirade+1):
        strinPiramide = ""
        for j in range(1, i+1):
            strinPiramide += f" {str(j)}"
        print(strinPiramide)
    return

while True:
    try:
        numeroCamadas = int(input("Digite um número inteiro: "))
        piramide(numeroCamadas)
        break
    except:
        print("Digite um valor válido!")
        continue