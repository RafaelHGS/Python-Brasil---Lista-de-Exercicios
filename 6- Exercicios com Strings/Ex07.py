"""
Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.

"""

def main():
    frase = input("Digite sua frase: ").lower()

    vogais = ('a', 'e', 'i', 'o', 'u')
    contaVogais = 0
    espacosBrancos = 0

    for i in frase:
        if i in vogais:
            contaVogais += 1
        if i == " ":
            espacosBrancos +=1

    print(f"Na sua frase existem {contaVogais} vogais e {espacosBrancos} espaços em branco")

    return

if __name__ == "__main__":
    main()