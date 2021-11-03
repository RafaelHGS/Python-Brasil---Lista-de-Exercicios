"""
    2- Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

#Entradas
valor = int(input("Informe aqui o valor: "))

#Processamento
if  valor >= 0:
    positivoOuNegativo = "Positivo"
else:
    positivoOuNegativo = "Negativo"

#Saída
print(f'O valor informado "{valor}" é {positivoOuNegativo}')