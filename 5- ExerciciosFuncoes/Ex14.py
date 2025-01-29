"""
Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

8  3  4 
1  5  9
6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.


vetor exemplo: vetor = [8, 3, 4, 1, 5, 9, 6, 7, 2]
"""

from itertools import permutations


def eh_quadrado_magico(quadrado):
    # Índices das linhas, colunas e diagonais do quadrado mágico 3x3
    indices = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Linhas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colunas
        (0, 4, 8), (2, 4, 6)              # Diagonais
    ]

    # Verifica se todas as somas são iguais a 15
    return all(sum(quadrado[i] for i in grupo) == 15 for grupo in indices)

def encontrar_quadrados_magicos():
    numeros = range(1, 10)
    quadrados_magicos = []
    
    for perm in permutations(numeros):
        if eh_quadrado_magico(perm):
            quadrados_magicos.append(perm)
    
    return quadrados_magicos

def imprimir_quadrados(quadrados):
    for q in quadrados:
        print(f"{q[0]} {q[1]} {q[2]}\n{q[3]} {q[4]} {q[5]}\n{q[6]} {q[7]} {q[8]}\n")

quadrados_magicos = encontrar_quadrados_magicos()
imprimir_quadrados(quadrados_magicos)
