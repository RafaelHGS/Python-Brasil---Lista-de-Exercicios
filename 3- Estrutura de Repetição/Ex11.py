"""
        Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
    compreendido por eles.
"""

num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))
soma = 0

if num1 > num2:
    num1, num2 = num2, num1

print(f"Os números no intervalo entre {num1} e {num2} são:")

for i in range(num1, num2+1):
    print(i)
    soma += i

print(f"\nE a Soma entre eles é {soma}")
