"""
    Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) 
de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

"""

tabela_de_precos = [{"Morango": 2.50}, {"Morango": 2.20},
                    {"Maçã": 1.80}, {"Maçã": 1.50}]

while True:
    try:
        print("Bem vindo à minha fruteira, hoje temos morangos e maçãs disponíveis para venda.")
        morangos = int(input("Quantos KG de morangos você deseja comprar ?: "))
        macas = int(input("Quantas KG de maçãs você deseja comprar ?: "))

        if morangos <= 0 and macas <= 0:
            print("Sinto muito se nada te agrada, volte sempre.")
            break
    except:
        print("Número de frutas inválido! Tente novamente\n")
        continue

    if morangos > 5:
        total_morangos = round(
            tabela_de_precos[1].get("Morango") * morangos, 2)
    else:
        total_morangos = round(
            tabela_de_precos[0].get("Morango") * morangos, 2)

    if macas > 5:
        total_macas = round(tabela_de_precos[3].get("Maçã")*macas, 2)
    else:
        total_macas = round(tabela_de_precos[2].get("Maçã")*macas, 2)

    total = round(total_morangos + total_macas, 2)

    if (morangos + macas > 8) or total > 25:
        total = total*0.90

    print()
    print(f" Maçãs = R${total_macas}\n",
          f"Morangos = R${total_morangos}\n",
          f"Total à pagar = R${total}")

    break
