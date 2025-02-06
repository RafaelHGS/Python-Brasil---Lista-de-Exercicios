"""
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
"""

def main():
    #Método preguiçoso com módulos prontos
    nome = input("Digite seu nome: ").upper()

    for i in range(1, len(nome)+1):
        print(nome[:i])
    return

if __name__ == "__main__":
    main()