"""
    Faça um programa que leia 5 números e informe o maior número.
"""

numeros = []

for i in range(1, 6):
    numero = int(input(f"Digite o {i}ºn inteiro: "))
    numeros.append(numero)

print(max(numeros))
