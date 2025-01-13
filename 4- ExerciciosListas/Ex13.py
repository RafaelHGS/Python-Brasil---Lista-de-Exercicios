"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
from random import randint as rd

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

#temperaturas, em nosso exemplo de 18 a 38º:
temperaturas = [rd(18, 38) for x in range(12)]


def mediaTemperaturas():
    media_anual = sum(temperaturas)/len(temperaturas)
    print(f"media anual {media_anual:.2f}")
    temperaturas_acima_media = {}

    for i, j in enumerate(temperaturas, 1):
        if j >= media_anual:
            temperaturas_acima_media[i] = j

    print("Os meses que ultrapássaram a média anual foram:\n")
    for i in temperaturas_acima_media:
        print(meses[i-1], temperaturas_acima_media[i])

    return

mediaTemperaturas()

