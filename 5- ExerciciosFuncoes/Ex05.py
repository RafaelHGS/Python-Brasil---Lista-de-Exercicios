"""
Faça um programa com uma função chamada somaImposto.
A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""

#Comentário do programador: Dado a natureza do enunciado e das questões anteriores,
#irei presumir que o "taxaImposto" é um numero inteiro
def somaImposto(taxaImposto, custo):
    return custo*(1+(taxaImposto/100))

while True:
    try:
        custo = float(input("Digite um valor de custo (no formato R$00.00 ou R$00): R$"))
        imposto = int(input("Digite um valor de taxa (ex: 3 para 3%): "))
        print(f"Custo + Taxa = R${somaImposto(imposto, custo):.2f}")
        break
    except:
        print("Digite um valor válido!")
        continue
