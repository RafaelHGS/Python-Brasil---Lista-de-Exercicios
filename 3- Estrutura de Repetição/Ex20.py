"""

    Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
        Ex.: 5!=5.4.3.2.1=120

        Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
    limitando o fatorial a números inteiros positivos e menores que 16.

"""


def fatorial(num):  # Solução Recursiva
    if num <= 0:
        return 1
    return num*fatorial(num-1)


def fatorial_iterativa(num):  # Solução iterativa
    numero = 1
    for i in range(1, num+1):
        numero = numero*i
    return numero


while True:
    try:
        num = int(
            input("Digite um número para se calcular o fatorial [1 a 16]: "))
        if num <= 0 or num >= 17:
            print("O número deve ser de 1 a 16 !")
            continue

        print(fatorial(num))

    except:
        print("Operação Inválida")
