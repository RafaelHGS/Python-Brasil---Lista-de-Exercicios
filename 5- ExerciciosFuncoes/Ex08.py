"""
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
"""

#Função pronta "Preguiçosa"
def ContaNumero(numero = int):
    return len(str(numero))

#Função evitando "pilhas inclusas" (funções prontas)
def ContaNumero2(numero = int):
    if numero < 0:  # Lida com números negativos
        numero = -numero  # Torna o número positivo

    contaNumero = 0

    while numero > 0:
        numero //= 10
        contaNumero +=1

    return contaNumero if contaNumero > 0 else 1 # Garante 1 dígito para o caso de '0'


while True:
    try:
        #conversão para int somente porque o valor dentro de um input já vem como string e o exercício pede um int
        numero = int(input("Digite um numero inteiro para contar a quantidade de digitos: "))
        print(ContaNumero(numero))
        print(ContaNumero2(numero))
        break
    except:
        print("Digite um valor válido!")
        continue
