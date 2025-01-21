"""
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""



#Comentário do programador: Dado a natureza do enunciado e das questões anteriores,
#irei presumir que os "argumentos" são numero inteiro
def somaArgumento(arg1, arg2, arg3):
    return arg1+arg2+arg3


while True:
    try:
        num1, num2, num3 = map(int, input("Digite 3 números inteiros: ").split(" "))
        print(somaArgumento(num1, num2, num3))
        break
    except:
        print("Digite um valor válido!")
        continue