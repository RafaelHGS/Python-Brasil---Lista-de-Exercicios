"""
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante

Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

"""

# #Descobrindo Faixa Salario, teste de cálculo
# faixa_salario = ((valor-200)/0.09)


# Inicializa o array de contadores para cada faixa salarial
array_contador = [0, 0, 0, 0, 0, 0, 0, 0, 0]


#Exemplo de entrada de salários contadores:
salariosContadores = [200, 3900, 400, 4900, 3000, 8000, 2600, 100, 1200, 800, 6050, 4000, 12000]

for i in salariosContadores:
    salarioContador = 200 + (i * 0.09)
    indice = int((salarioContador-200)/100)

    if indice >= 8:
        array_contador[-1] += 1
    else:
        array_contador[indice] +=1


"Exibição de valores"
faixas = [
    "$200 - $299", "$300 - $399", "$400 - $499",
    "$500 - $599", "$600 - $699", "$700 - $799",
    "$800 - $899", "$900 - $999", "$1000 ou mais"
]
for i, contador in enumerate(array_contador):
    print(f"{faixas[i]}: {contador} vendedores")
