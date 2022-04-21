"""
    Um posto está vendendo combustíveis com a seguinte tabela de descontos:
        - Álcool:
        - até 20 litros, desconto de 3% por litro
        - acima de 20 litros, desconto de 5% por litro

        - Gasolina:
        - até 20 litros, desconto de 4% por litro
        - acima de 20 litros, desconto de 6% por litro
    
    Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""


def calcula_Litros(tipo_de_combustivel, litros):
    if tipo_de_combustivel == "G":
        if litros <= 20:
            return litros*0.96
        else:
            return litros * 0.94
    elif tipo_de_combustivel == "A":
        if litros <= 20:
            return litros*0.97
        else:
            return litros * 0.95


ALCOOL = 1.90
GASOLINA = 2.50

while True:
    try:
        combustivel_escolhido = input("Gasolina ou alcool [G/A]?: ").upper()
        litros = int(input("Quantos litros deseja abastecer ?: "))

        if (combustivel_escolhido == "G" or combustivel_escolhido == "A") and litros >= 0:
            a_pagar = round(calcula_Litros(combustivel_escolhido, litros), 2)
        else:
            print("Escolha o tipo de combustível e a quantidade de litros !!!\n")
            continue
    except:
        print("Alguma Opção inválida tente novamente")
        continue

    print(f"Recibo = R${a_pagar}")
    break
