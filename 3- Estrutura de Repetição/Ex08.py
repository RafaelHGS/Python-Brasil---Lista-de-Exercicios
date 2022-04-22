"""
    Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

numeros = []

for i in range(1, 6):
    numero = int(input(f"Digite o {i}ºn inteiro: "))
    numeros.append(numero)

print(f"A soma de todos os números é: {sum(numeros)}")
print(f"A média de todos os números é: {sum(numeros)/len(numeros)}")
