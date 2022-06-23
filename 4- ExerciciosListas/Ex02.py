# Ex02- Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = [float(input(f"Digite o {i+1}º número real: ")) for i in range(10)]

print("Números digitados na ordem inversa")
for i, j in enumerate(vetor, 1):
    print(vetor[i*(-1)])
