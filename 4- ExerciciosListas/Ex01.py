# EX01- Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor = [int(input(f"Digite o {i+1}º número inteiro: ")) for i in range(5)]

print("\nNúmeros digitados:")
for i in vetor:
    print(i)
