"""
    23- Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma
função de arredondamento.
"""

num = float(input("Digite um número: "))

if num == round(num):
    print(f"O número {num:.0f} é inteiro")
else:
    print(f"O número {num} é decimal")