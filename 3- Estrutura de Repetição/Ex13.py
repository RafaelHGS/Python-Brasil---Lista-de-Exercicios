"""
        Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao
    segundo número. Não utilize a função de potência da linguagem.
"""


def potencia(base, expoente):
    if expoente == 0:
        return 1
    return base*potencia(base, expoente-1)


num1 = int(input("Digite o primeiro número (Base): "))
num2 = int(input("Digite o primeiro número (Expoente): "))

print(potencia(num1, num2))
