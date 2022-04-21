"""
    Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
e continue pedindo até que o usuário informe um valor válido.

"""

while True:
    try:
        nota = int(input("Digite uma nota de 0 a 10: "))

        if nota > 10 or nota < 0:
            print("Nota Inválida\n")
            continue
        else:
            print(f"\n{nota} é Válida :)\n")
            break
    except:
        print("Nota Inválida\n")
        continue
