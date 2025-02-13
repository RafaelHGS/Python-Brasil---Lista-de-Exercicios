"""
Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

"""

def numeroPorExtenso(numero):
    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

    if numero < 20:
        return unidades[numero]
    else:
        dezena = numero // 10
        unidade = numero % 10
        return f"{dezenas[dezena]} e {unidades[unidade]}"

    return

def main():
    while True:
        numero = int(input("\nDigite um número entre 1 e 99 para a conversão: "))
        if 0 <= numero >= 100:
            print("Número inválido!")
            continue

        print("Seu número é: ", numeroPorExtenso(numero))
        break
    return

if __name__ == "__main__":
    main()