"""
    19- Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
dezenas e unidades do mesmo.

    Observando os termos no plural a colocação do "e", da vírgula entre outros. 
    Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 
        326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

listaDeTeste = [326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]

print()
for numTeste in listaDeTeste:
    numero = int(numTeste/100)

    if numero == 1:
        centena = f"{numero} centena"
    else:
        centena = f"{numero} centenas"

    numero2 = int((numTeste - int(numero*100))/10)
    if numero2 == 1:
        dezenas = f"{numero2} dezena"
    else:
        dezenas = f"{numero2} dezenas"
    

    numero3 = int(numTeste - (int(numero*100) + int(numero2*10)))
    if numero3 == 1:
        unidade = f"{numero3} unidade"
    else:
        unidade = f"{numero3} unidades"
    

    if len(str(numTeste)) == 3:
        print(f"{centena}, {dezenas} e {unidade}")

    elif len(str(numTeste)) == 2:
        print(f"{dezenas} e {unidade}")

    elif len(str(numTeste)) == 1:
        print(f"{unidade}")

    print()
        
        