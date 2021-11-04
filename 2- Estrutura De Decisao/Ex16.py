"""
    16- Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas 
seguintes situações:

    -Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
     pedir os demais valores, sendo encerrado;
    -Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    -Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    -Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
#Definindo Funções
def equacaoDelta(A,B,C):
    delta = (B**2) -4*A*C
    return delta

def raizes(A,B,delta):
    raiz1 =  ((-B) + (delta**0.5))/(2*A)
    raiz2 = ((-B) - (delta**0.5))/(2*A)
    return raiz1,raiz2

def main():
    while True:
        try:
            A = int(input("Informe o Número de A: "))
            if A == 0:
                return
            B = int(input("Informe o Número de B: "))
            C = int(input("Informe o Número de C: "))
        except:
            print("Digite apenas números")
        
        Delta = equacaoDelta(A,B,C)
        if Delta <0:
            print("Não há raízes reais")
            break
        elif Delta == 0:
            raiz1, raiz2 = raizes(A,B,C,Delta)
            print(f"Possue apenas uma raíz real = {raiz1}")
        elif Delta > 0:
            raiz1, raiz2 = raizes(A,B,Delta)
            print(f"Possue duas uma raízes reais: \nRaíz 1: {raiz1:.2f}\nRaíz 2: {raiz2:.2f}")

if __name__=="__main__":
    main()