"""
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n


para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
"""

def piramide(camadasPirade = int):
    for i in range(1, camadasPirade+1):
        print(f"{i} "*i)
    return

while True:
    try:
        numeroCamadas = int(input("Digite um número inteiro: "))
        piramide(numeroCamadas)
        break
    except:
        print("Digite um valor válido!")
        continue