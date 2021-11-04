"""
    13- Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
"""
#Definindo Dicionário
dicionario1 = {
    1 : "Domingo",
    2 : "Segunda",
    3 : "Terça",
    4 : "Quarta",
    5 : "Quinta",
    6 : "Sexta",
    7 : "Sábado",
}

#Entrada
numero = int(input("Digite um valor de 1 a 7: "))

#Procesamento e Saída
if numero < 1 or numero > 7:
    print("Valor Inválido")
else:
    print(dicionario1[numero])
