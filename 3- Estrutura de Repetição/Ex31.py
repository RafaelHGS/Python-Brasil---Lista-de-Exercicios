"""
    O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de
    conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá 
    receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve 
    ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da
    compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor
    do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima 
    compra. A saída deve ser conforme o exemplo abaixo:
    Lojas Tabajara 
        Produto 1: R$ 2.20
        Produto 2: R$ 5.80
        Produto 3: R$ 0
        Total: R$ 9.00
        Dinheiro: R$ 20.00
        Troco: R$ 11.00
"""


def main():
    produto = 1.0
    contador = 1

    produtos = []

    print("Lojas Tabajara")
    while produto != 0:
        produto = float(input(f"Digite o valor do {contador}º Produto: "))
        produtos.append(produto)

        contador = contador + 1

    while True:
        valorPago = float(input("Digite o valor a ser pago: "))
        if valorPago < sum(produtos):
            continue
        else:
            break

    print()
    print("Lojas Tabajara")
    for i, j in enumerate(produtos, 1):
        print(f"Produto {i}: R$ {round(j, 2)}")

    print(f"Total: R$ {sum(produtos)}")
    print(f"Dinheiro: R$ {valorPago}")
    print(f"Troco: R$ {valorPago - sum(produtos)}")


if __name__ == "__main__":
    while True:
        print()
        main()
