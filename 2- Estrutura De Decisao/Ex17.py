"""
    17- Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este
ano é ou não bissexto.
"""

ano = int(input("Informe um número correspondente ao ano (Ex: 2021): "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} Ano Bissexto")
else:
    print(f"O ano {ano} Não é um ano Bissexto!")
