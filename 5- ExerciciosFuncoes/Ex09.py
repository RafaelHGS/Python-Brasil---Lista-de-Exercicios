"""
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
"""

#Função pronta "Preguiçosa"
def ReverteNumero(numero):
    numero = str(numero)
    
    # Verifica se o número é negativo
    if numero[0] == '-':
        return int('-' + ''.join(reversed(numero[1:])))  # Reverte sem o sinal e adiciona o '-'
    else:
        return int(''.join(reversed(numero)))  # Reverte diretamente se for positivo
    


#Função evitando "pilhas inclusas" (funções prontas)
def ReverteNumero2(numero = int):
    numero = str(numero)

    numeroRevertido = ""
    for i in range(len(numero) - 1, -1, -1):
        numeroRevertido += numero[i]
        

    if numeroRevertido[-1] == '-':  # Caso o número original seja negativo
        numeroRevertido = '-' + numeroRevertido[:-1]

    return int(numeroRevertido)


while True:
    try:
        numero = int(input("Digite um numero inteiro para reverter: "))
        print(ReverteNumero(numero))
        print(ReverteNumero2(numero))
        break
    except:
        print("Digite um valor válido!")
        continue
