"""
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F
"""

def main():
    #Método preguiçoso com módulos prontos
    nome = input("Digite seu nome: ").upper()

    for i in range(len(nome), -1, -1):
        print(nome[:i])
    return

if __name__ == "__main__":
    main()