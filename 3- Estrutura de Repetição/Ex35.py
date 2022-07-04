"""
    Encontrar números primos é uma tarefa difícil.
    Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro
    informado pelo usuário.
"""


def verificaPrimo(numero):
    if numero <= 2:
        return
    else:
        for i, j in enumerate(range(numero-2), 2):
            if numero % i == 0:
                return
    return numero


print("Listar números primos:")
numeroInteiro = int(
    input("Digite o número inteiro para a listagem de primos até ele: "))


numerosPrimos = [1]

for i in range(2, numeroInteiro+1):
    numeroAtual = verificaPrimo(i)

    if numeroAtual != None:
        numerosPrimos.append(numeroAtual)

print(numerosPrimos)
