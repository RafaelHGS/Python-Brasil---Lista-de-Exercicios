"""
    7- Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

#Entrada
num1 = float(input("\nInforme o primeiro numero: "))
num2 = float(input("Informe o segundo numero: "))
num3 = float(input("Informe o terceiro numero: "))

#Processamento
maiorNum1Num2 = (num1 + num2 + abs(num1- num2))/2
maiorNum1Num2Num3 =(maiorNum1Num2 + num3 + abs(maiorNum1Num2 - num3))/2

if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

#Saída
print(f"\nO maior numero informado é {maiorNum1Num2Num3}")
print(f"O menor numero informado é {menor}\n")