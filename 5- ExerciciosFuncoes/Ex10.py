"""
Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12.
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

Comentário do Programador: Me senti no meu primeiro ano de faculdade novamente, onde fiz algo parecido. Bons Tempos S2
"""
from random import randint as rd

#Implementação para adicionar diretamente o resultado da rolagem de dados, comente a função de mesmo nome e implemente essa 
# def rolaDados():
#     resultadoDados = rd(2, 12)
#     print(f"Resultado da rolagem de dados: {resultadoDados}")
#     return resultadoDados


def rolaDados():
    dado1 = input("Aperte qualquer tecla para rolar o primeiro dado: ")
    resultadoDado1 = rd(1,6)

    dado2 = input("Aperte qualquer tecla para rolar o segundo dado: ")
    resultadoDado2 = rd(1,6)

    resultadoDados = resultadoDado1 + resultadoDado2


    print(f"Resultado da rolagem do primeiro dado: {resultadoDado1}")
    print(f"Resultado da rolagem do segundo dado: {resultadoDado2}")
    print(f"Resultado da rolagem de dados: {resultadoDados}")
    return resultadoDados


def verificaResultado(resultadoDados,):
    natural = [7, 11]
    crap = [2, 3, 12]
    if resultadoDados in natural:
        print("Você Ganhou!!!")
        return True
    elif resultadoDados in crap:
        print("Você Perdeu!!!")
        return True
    return False


def main():
    print("1ª rodada")
    resultadoDados = rolaDados()
    
    if verificaResultado(resultadoDados):
        return
    

    ponto = resultadoDados
    contaRodada = 2
    while True:
        print()
        print(f"{contaRodada} Rodada: ")
        print(f"Ponto necessário: {ponto}")

        novaRolagem = rolaDados()

        if novaRolagem == ponto:
            print("Você ganhou")
            break
        elif novaRolagem == 7:
            print("Você Perdeu!")
            break
        contaRodada +=1
    

if __name__ == "__main__":
    main()