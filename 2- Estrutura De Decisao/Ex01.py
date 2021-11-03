"""
    1- Faça um Programa que peça dois números e imprima o maior deles.
"""
#Entrada
num1 = float(input("Informe o primeiro numero: "))
num2 = float(input("Informe o segundo numero: "))

#Processamento
maiorNum = (num1 + num2 + abs(num1- num2))/2

#Saída
print(f"O maior numero informado é {maiorNum}")