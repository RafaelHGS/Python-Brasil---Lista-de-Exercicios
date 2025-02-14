"""
Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
"""
from random import randint


def EscolhePalavra():
    with open("6- Exercicios com Strings\Ex12\\dicionario.txt", "r+") as dicionario:
        palavras = dicionario.readlines()
        palavra_aleatoria = palavras[randint(0, len(palavras) - 1)].strip().lower()

        dicionario.close()

    palavra_embaralhada = EmbaralhaPalavra(palavra_aleatoria)
    
    return palavra_aleatoria, palavra_embaralhada

def EmbaralhaPalavra(palavra):
    palavraContruida = ""
    indexPalavra = []

    while len(indexPalavra) < len(palavra):
        escolheIndex = randint(0, len(palavra)-1)
        if escolheIndex not in indexPalavra:
            palavraContruida += palavra[escolheIndex]
            indexPalavra.append(escolheIndex)

    return palavraContruida

def main():
    palavraAleatoria, palavraEmbaralhada = EscolhePalavra()

    tentativas = 0
    palavras = set()

    print("Jogo da Forca!")


    while tentativas < 6:
        print(f"\nPalavra: {palavraEmbaralhada}")
        
        palavraTentativa = input("Digite uma palavra/tentativa para adivinhar: ").lower()
        
        if palavraTentativa.isnumeric() or palavraTentativa == "":
            print("\nDigite uma palavra!!!!")
            continue
        elif palavraTentativa in palavras:
            print("\nPalavra já digitada!!!!")
            continue

        if palavraTentativa.lower() == palavraAleatoria:
            print("\nParabéns, você ganhou!")
            break
        else:
            tentativas += 1
            print(f"Você errou pela {tentativas}ª vez. Tente de novo!")

        palavras.add(palavraTentativa)

    
    if tentativas == 6:
        print(f"Você perdeu, a palavra era: {palavraAleatoria}")
        
    return

if __name__ == "__main__":
    main()