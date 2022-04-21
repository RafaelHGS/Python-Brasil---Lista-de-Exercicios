"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg


        Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
    porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
    cliente receberá ainda um desconto de 5% sobre o total da compra.
    
     Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
    contendo as informações da compra: 
        -tipo e quantidade de carne
        -preço total
        -tipo de pagamento
        -valor do desconto
        -valor a pagar.

"""


def carne(carne, quantidade):
    if quantidade > 5:
        tabela = tabela_de_precos2
    else:
        tabela = tabela_de_precos1

    if carne == "F":
        valor_carne = round(tabela[0].get(
            "Filé Duplo")*quantidade, 2)
    elif carne == "A":
        valor_carne = round(tabela[1].get(
            "Alcatra")*quantidade, 2)
    elif carne == "P":
        valor_carne = round(tabela[2].get(
            "Picanha")*quantidade, 2)
    return valor_carne


tabela_de_precos1 = [{"Filé Duplo": 4.90}, {"Alcatra": 5.90},
                     {"Picanha": 6.90}, ]

tabela_de_precos2 = [{"Filé Duplo": 5.80}, {"Alcatra": 6.80},
                     {"Picanha": 7.80}, ]

resposta = ["F", "A", "P"]


while True:
    try:
        print("Aproveite a nossa imperdível promoção de carnes, porém você pode levar apenas uma!")
        print("Qual você deseja levar ?\n", "[F]Filé Duplo",
              "[A]Alcatra",
              "[P]Picanha",)

        tipo_de_carne = input("R: ").upper()
        qtd_carne = int(input("Quantos Kg de carne você deseja ?: "))

        if (tipo_de_carne not in resposta) or qtd_carne <= 0:
            print("Opção inválida!\n")
            continue
    except:
        print("Opção inválida!\n")
        continue

    total = carne(tipo_de_carne, qtd_carne)

    while True:
        tipo_de_pagamento = input(
            "O pagamento será com cartão Tabajara ? [S/N]: ").upper()

        if tipo_de_pagamento == "S":
            total = round(total*0.9, 2)
            print(f"O total de sua compra foi de: R${total}")
            break
        elif tipo_de_pagamento == "N":
            print(f"O total de sua compra foi de: R${total}")
            break
        else:
            print("Tipo de pagamento inválido!")
            continue
    break
