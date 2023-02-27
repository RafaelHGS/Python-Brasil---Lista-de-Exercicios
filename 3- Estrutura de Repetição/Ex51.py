"""
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
  
Imprima no final a soma da série.
"""

S = int(input("Digite a quantidade de termos (n): "))

n = 1
m = 1
termos = []

for i in range(S):
    aux = (n, m)
    termos.append(aux)
    n += 1
    m += 2

print(f"Série de {S}:", *termos, sep="\n")
