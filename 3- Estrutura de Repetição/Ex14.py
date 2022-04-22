"""
        Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e
    a quantidade de números impares.
"""

numeros = []
numeros_pares = []
numeros_impares = []

for i in range(1, 11):
    num = int(input(f"Digite o {i}º número inteiro: "))
    numeros.append(num)

for i in numeros:
    if i % 2 == 0:
        numeros_pares.append(i)
    else:
        numeros_impares.append(i)

print(f'\nNa lista "{numeros}" existem: \n{len(numeros_pares)} Números pares e {len(numeros_impares)} Números impares')
