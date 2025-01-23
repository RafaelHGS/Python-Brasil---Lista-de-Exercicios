"""
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

"""

def valorPagamento(valorPrestacao, diasEmAtraso):
    if diasEmAtraso > 0: 
        multa = valorPrestacao * 0.03  # 3% de multa
        juros = valorPrestacao * (0.001 * diasEmAtraso)  # 0,1% de juros por dia
        valorPrestacao += multa + juros
    return valorPrestacao


def main():
    prestacoes = []

    while True:
        try:
            prestacao = float(input("Digite o valor da prestação no formato R$00.00 ou R$00 (Digite 0 para encerrar): R$"))

            if prestacao <= 0:
                print(f"Quantidade de Prestações Pagas no dia: {len(prestacoes)}")
                print("Prestações: ", *prestacoes, sep="\nR$")
                print(f"\nValor total pago: R${sum(prestacoes):.2f}")

                break
    
            diasEmAtraso = int(input("Digite o numero de dias em atraso: "))
            prestacoes.append(valorPagamento(prestacao, diasEmAtraso))
            print()


        except:
            print("Digite um valor válido!")
            continue

if __name__ == "__main__":
    main()