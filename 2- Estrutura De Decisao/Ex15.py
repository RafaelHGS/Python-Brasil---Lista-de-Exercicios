"""
    15- Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser 
um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""
#   Entrada de dados: 
ladoA = int(input("Digite o tamanho da primeira aresta: "))
ladoB = int(input("Digite o tamanho da segunda aresta: "))
ladoC = int(input("Digite o tamanho da terceira aresta: "))

#Processamento e Saída
if (ladoA + ladoB) > ladoC or (ladoA + ladoC) > ladoB or (ladoB + ladoC) > ladoA:
    print("É um triângulo")

    if ladoA == ladoB == ladoC:
        print("É um triângulo Equilátero")
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print("É um triângulo Isósceles")
    elif ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
        print("É um triângulo Escaleno")  

else:
    print("Não é um triângulo")