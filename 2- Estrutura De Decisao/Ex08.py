"""
    8- Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""

#Entrada
p1 = float(input("\nInforme o preço do primeiro produto: "))
p2 = float(input("Informe o preço do segundo produto: "))
p3 = float(input("Informe o preço do terceiro produto: "))

#Processamento

if p1 < p2 and p1 < p3:
    menor = p1
if p2 < p1 and p2 < p3:
    menor = p2
if p3 < p1 and p3 < p2:
    menor = p3

#Saída
print(f"\nO produto que você deve comprar é o produto de R${menor:.2f}")
