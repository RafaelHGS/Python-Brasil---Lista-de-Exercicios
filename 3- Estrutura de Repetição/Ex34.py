"""
    Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
    Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um
    número inteiro e determine se ele é ou não um número primo.
"""

print("Verificação de números primos:")
numeroInteiro = int(input("Digite o número inteiro para a verificação: "))

verifica = 0
for i, j in enumerate(range(numeroInteiro-2), 2):
    if numeroInteiro % i == 0:
        verifica = 1
        break

if verifica == 1:
    print(f"O número {numeroInteiro} não é Primo")
else:
    print(f"O número {numeroInteiro} é Primo")
