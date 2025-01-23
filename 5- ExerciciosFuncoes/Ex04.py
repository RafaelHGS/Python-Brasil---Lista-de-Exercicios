"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""


#Comentário do programador: Dado a natureza do enunciado e das questões anteriores,
#irei presumir que os "argumentos" são numero inteiro

def PositivoNegativo(numero):
    if numero >0:
        return "P"
    return "N"


while True:
    try:
        num1 = int(input("Digite um numero: "))
        print(PositivoNegativo(num1))
        break
    except:
        print("Digite um valor válido!")
        continue