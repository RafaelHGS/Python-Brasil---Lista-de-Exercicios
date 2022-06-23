#   Ex05-Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#       Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.


vetor = [int(input(f"Digite o {i+1}º número inteiro: ")) for i in range(20)]

pares = []
impares = []

for i in vetor:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f"\nLista de Números: {vetor}")

print(f"\nLista de Números Ímpares: {impares}")

print(f"\nLista de Números: {pares}")
