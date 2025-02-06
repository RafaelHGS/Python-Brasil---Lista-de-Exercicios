"""
Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
"""

def main():
    #Método preguiçoso com módulos prontos
    nome = input("Digite seu nome: ").upper()
    nomeCopia = nome

    nome = ''.join(reversed(nome))
    print(nome)

    #Metodo iterativo
    nomeInvertido = ""
    for i in range(len(nomeCopia)-1, -1, -1):
        nomeInvertido += nomeCopia[i]
    print(nomeInvertido)

    return

if __name__ == "__main__":
    main()