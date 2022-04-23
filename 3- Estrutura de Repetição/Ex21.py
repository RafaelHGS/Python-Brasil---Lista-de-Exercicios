"""
        Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
    Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""

numero = int(input("Digite um número inteiro para verificar se é primo: "))
verificador = 0

for i in range(2, numero):
    if numero % i == 0:
        print("Não é número primo")
        verificador += 1
        break

if verificador == 0:
    print("É primo")
