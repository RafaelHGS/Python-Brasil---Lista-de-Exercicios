"""
    9- Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

#Entrada
listaOrdenada= []
for i in range(3):
    numero = int(input(f"\n\nInforme o {i+1}º Numero (inteiro): "))
    listaOrdenada.append(numero)

#Processamento
listaOrdenada.sort()

#Saída
print(f"\nOs numeros na ordem crescente são: {listaOrdenada[0]}, {listaOrdenada[1]}, {listaOrdenada[2]}")