"""
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 

    Imprima no final a soma da série.
"""

S = int(input("Digite a quantidade de termos (n): "))

n = 1
m = 1
total = 0

for i in range(S-1):
    n += 1
    m += 2

print(f"A soma é {n/m}")