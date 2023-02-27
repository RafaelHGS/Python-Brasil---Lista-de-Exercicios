"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, 
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""


vetor1 = input(
    'Digite o vetor 1 com 10 numeros inteiros (ex: "0 2 4 6 8 10..."): ').split(" ")
vetor2 = input(
    'Digite o vetor 2 com 10 numeros inteiros (ex: "1 3 5 7 9..."): ').split(" ")
vetor3 = input(
    'Digite o vetor 2 com 10 numeros inteiros (ex: "1 3 5 7 9..."): ').split(" ")


# # Gerar Vetores de teste
# vetor1 = [x for x in range(20) if x % 2 == 0]
# vetor2 = [x for x in range(20) if x % 2 != 0]
# vetor3 = [x for x in range(100) if x % 10 != 0]

# 0 2 4 6 8 10 12 14 16 18
# 1 3 5 7 9 11 13 15 17 19

vetor4 = []

for i in range(len(vetor1)):
    vetor4.append(int(vetor1[i]))
    vetor4.append(int(vetor2[i]))
    vetor4.append(int(vetor3[i]))


print(vetor3)
