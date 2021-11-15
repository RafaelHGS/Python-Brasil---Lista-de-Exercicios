"""
    18- Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida
"""


while True:
    data = "".join(input("Informe uma data no formato (dd/mm/aaaa): ").split("/"))
    if data.isnumeric() == False or len(data) != 8:
        print("Digite uma data válida: \n")
        continue
    try:
        dia = int(data[0:2])
        mes = int(data[2:4])
        ano = int(data[4:])
    except:
        print("\nData inválida!")
        break
    
    if dia > 31 or dia <= 0:
        invalido = "\nDia Invalido"
        print(f"Data inválida! {invalido}")
        break

    elif mes > 12 or mes <= 0:
        invalido = "\nMês Invalido"
        print(f"Data inválida! {invalido}")
        break

    elif ano > 9999 or ano <= 0:
        invalido = "\nAno Invalido"
        print(f"Data inválida! {invalido}")
        break

    else:
        print(f"Data válida: {dia}/{mes}/{ano}")
    print()
    break