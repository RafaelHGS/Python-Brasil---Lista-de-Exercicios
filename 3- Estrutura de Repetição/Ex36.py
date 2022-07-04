"""
        Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
    mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser 
    informados também pelo usuário, conforme exemplo abaixo:
    
    Montar a tabuada de: 5
    Começar por: 4
    Terminar em: 7

        Vou montar a tabuada de 5 começando em 4 e terminando em 7:
        5 X 4 = 20
        5 X 5 = 25
        5 X 6 = 30
        5 X 7 = 35

    Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
"""


def geraTabuada(num, nInicial, nFinal):
    print(
        f"\n Tabuada do {num} começando por {nInicial} e terminando em {nFinal}")
    for i in range(nInicial, nFinal+1):
        print(f"{num} X {i} = {num*i}")
    return


print("Gera tabuada:")
tabuada = int(input("Qual tabuada você deseja fazer ?: "))

while True:
    num1 = int(input("Começar por: "))
    num2 = int(input("Terminar por: "))

    if num1 > num2:
        print('\n\n"Começar" deve ser um número menor que "Terminar" !!!\n\n')
        continue
    else:
        geraTabuada(tabuada, num1, num2)
        break
