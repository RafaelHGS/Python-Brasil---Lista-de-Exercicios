"""
     Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a 
    soma dos valores.
"""

numeros = []

conjunto = int(input("Quantos números deseja inserir ?: "))

for i in range(1, conjunto+1):
    while True:
        try:
            num = int(input(f"Insira o {i}º número: "))
            numeros.append(num)
            break
        except:
            print("Número inválido")
            continue

print(f"O menor valor do conjunto: {min(numeros)}")
print(f"O maior valor do conjunto: {max(numeros)}")
print(f"A soma do conjunto: {sum(numeros)}")
