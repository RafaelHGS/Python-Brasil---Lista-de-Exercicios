"""
    6- Faça um Programa que leia três números e mostre o maior deles.
"""

#Entrada
num1 = float(input("Informe o primeiro numero: "))
num2 = float(input("Informe o segundo numero: "))
num3 = float(input("Informe o terceiro numero: "))

#Processamento
maiorNum1Num2 = (num1 + num2 + abs(num1- num2))/2
maiorNum1Num2Num3 =(maiorNum1Num2 + num3 + abs(maiorNum1Num2 - num3))/2

#Saída
print(f"O maior numero informado é {maiorNum1Num2Num3}")