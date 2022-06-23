# Ex09- Faça um Programa que leia um vetor A com 10 números inteiros,
#       calcule e mostre a soma dos quadrados dos elementos do vetor.

vetor = [int(input(f"Digite o {i+1}º Número inteiro: ")) for i in range(10)]

somaVetores = 0

for i in vetor:
    i = i**2
    somaVetores = somaVetores + i

print(f"A soma dos quadrados dos vetores é: {somaVetores}")
