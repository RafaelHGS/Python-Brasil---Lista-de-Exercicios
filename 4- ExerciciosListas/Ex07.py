# Ex07- Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.


vetor = [int(input(f"Digite o {i+1}º Número inteiro: ")) for i in range(5)]

multiplicacao = 1
for i in vetor:
    multiplicacao = multiplicacao*i

print("\n\nResultados:")
print(f"\nA soma dos números: {sum(vetor)}")
print(f"A multiplicação dos números: {multiplicacao}")
print(f"Todos os números: {vetor}")
