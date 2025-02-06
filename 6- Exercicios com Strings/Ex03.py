"""
Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
F
U
L
A
N
O
"""

def main():
    #Método preguiçoso com módulos prontos
    nome = input("Digite seu nome: ").upper()

    for i in nome:
        print(i)

    return

if __name__ == "__main__":
    main()