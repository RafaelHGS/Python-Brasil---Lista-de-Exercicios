"""
    24- Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    -par ou ímpar;
    -positivo ou negativo;
    -inteiro ou decimal.

"""


def soma(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def div(n1, n2):
    try:
        r = n1/n2
        return n1/n2
    except ZeroDivisionError:
        return "Não é posivel realizar divisão por 0"
    except ValueError:
        return "Erro em definir número"


def mul(n1, n2):
    return n1 * n2


def switch_case(op):
    try:
        case = switch.get(op)
        return case, True
    except:
        print("Operação inválida!"), False


def menu(n1, n2):
    print(
        f"Qual operação Básica você deseja realizar com os números {n1} e {n2}, respectivamente:")
    print("[1]- Soma")
    print("[2]- Subtração")
    print("[3]- Divisão")
    print("[4]- Multiplicação")


while True:
    print()
    try:
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite outro número: "))
    except:
        print("Digite um número válido!")
        continue

    switch = {
        1: soma(num1, num2),
        2: sub(num1, num2),
        3: div(num1, num2),
        4: mul(num1, num2)
    }

    while True:
        try:
            print()
            menu(num1, num2)
            r = int(input())
            print()

            if r > 4 or r < 1:
                print("Escolha uma operação válida!")
                continue
            else:
                break
        except:
            print("Escolha uma operação válida!")
            continue

    calculo, calculo_valido = switch_case(r)

    if calculo_valido:
        if type(calculo) == int:
            print(int(calculo), "É inteiro")
        else:
            print(f"{calculo:.2f} É decimal")
        if calculo % 2 == 0:
            print(f"{calculo} é um número par")
        else:
            print(f"{calculo} é um número ímpar")
        if calculo > 0:
            print(f"{calculo} é positivo")
        else:
            print(f"{calculo} é negativo")
    else:
        print(calculo)
        break
    break
