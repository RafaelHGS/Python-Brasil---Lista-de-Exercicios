"""
    14-João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário
de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de
pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa
que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na 
variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João
deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""

peso = float(input("Informe quantos quilos (Kg) de peixe foram pescados: "))
if peso > 50:
    excesso = peso - 50
    multa = excesso*4.00
    print(f"Quantidade pescada em quilos: {peso}Kg")
    print(f"Excesso Pescado: {excesso}")
    print(f"Multa pelo Excesso (R$4,00/Kg de Excesso): R${multa:.2f}")
else:
    print(f"Quantidade pescada em quilos: {peso}Kg")
    print(f"Excesso Pescado: Sem Excesso")
    print(f"Multa pelo Excesso (R$4,00/Kg de Excesso): Sem Multa")
