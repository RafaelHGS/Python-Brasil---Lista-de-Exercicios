"""
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
"""
from random import randint


def EscolhePalavra():
    with open("6- Exercicios com Strings\Ex11\\dicionario.txt", "r+") as dicionario:
        palavras = dicionario.readlines()
        palavra_aleatoria = palavras[randint(0, len(palavras) - 1)].strip().lower()
        dicionario.close()
    return palavra_aleatoria

def ConstroiPalavra(letras, palavra):
    palavraContruida = ""
    for i in palavra:
        if i in letras:
            palavraContruida += i
        else:
            palavraContruida += "_"

    return palavraContruida

def main():
    palavra = EscolhePalavra()

    tentativas = 0
    letras = set()

    print("Jogo da Forca!")


    while tentativas < 6:
        palavraAtual = ConstroiPalavra(letras, palavra)

        print(f"\nPalavra: {palavraAtual}")

        if palavraAtual == palavra:
            print("\nParabéns, você ganhou!")
            break

        letra = input("Digite uma letra: ").lower()
        
        if letra.isnumeric() or letra == "":
            print("\nDigite uma letra!!!!")
            continue
        elif letra in letras:
            print("\nLetra já digitada!!!!")
            continue

        if letra not in palavra:
            tentativas += 1
            print(f"Você errou pela {tentativas}ª vez. Tente de novo!")

        letras.add(letra)

    
    if tentativas == 6:
        print(f"Você perdeu, a palavra era: {palavra}")
        
    return

if __name__ == "__main__":
    main()