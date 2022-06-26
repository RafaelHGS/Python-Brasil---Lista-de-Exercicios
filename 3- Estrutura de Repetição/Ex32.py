"""
    Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
     Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

"""

# Solução recursiva


def fatorial(numero):
    if numero <= 0:
        return 1
    return numero * fatorial(numero-1)


# Solução iterativa
def fatorialIterativa(numero):
    resultado = 1
    for i, j in enumerate(range(numero), 1):
        resultado = resultado * i
    return resultado


numFatorial = int(input("Digite o número para se calcular o fatorial: "))
print(fatorial(numFatorial))
print(fatorialIterativa(numFatorial))
