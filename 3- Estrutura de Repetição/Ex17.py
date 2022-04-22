"""

    Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
        Ex.: 5!=5.4.3.2.1=120

"""

num = int(input("Digite um número para se calcular o fatorial: "))


def fatorial(num):  # Solução Recursiva
    if num <= 0:
        return 1
    return num*fatorial(num-1)


def fatorial_iterativa(num):  # Solução iterativa
    numero = 1
    for i in range(1, num+1):
        numero = numero*i
    return numero


print(fatorial(num))
print(fatorial_iterativa(num))
