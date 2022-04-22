"""

    A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
    Faça um programa capaz de gerar a série até o n−ésimo termo.

"""

from re import A

numero = int(
    input("Até qual número da sequencia fibonnaci você deseja ver ?: "))

a = 0
b = 1

for i in range(0, numero+1):
    print(a)
    a = a + b
    a, b = b, a
