"""
    21- Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do 
saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de
1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se 
preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
    uma nota de 5 e uma nota de 1;

    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
    quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

listaDeCedulas = [100, 50, 10, 5, 1]

while True:
    saque = int(input("Informe um valor para sacar (min: 10 / máx: 600): "))
    if saque < 10 or saque > 600:
        continue

    print()
    for nota in listaDeCedulas:
        saque = saque/nota
        print(f"Será fornecido {int(saque)} nota(s) de R$ {nota},00")
        saque = saque * nota - (int(saque)*nota)
    
    print()
    break