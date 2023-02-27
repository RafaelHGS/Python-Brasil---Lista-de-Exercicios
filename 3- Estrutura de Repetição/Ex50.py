"""
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N,

Faça um programa que calcule o valor de H com N termos.
"""

H = int(input("Digite a quantidade de termos (n): "))

n = 1
m = 1

somaH = 1

for i in range(2, H+1):
    somaH += n/i

print(f"Soma de: {somaH}")


# OU

somaH_2 = [1/x for x in range(2, H+1)]

print(1 + sum(somaH_2))
