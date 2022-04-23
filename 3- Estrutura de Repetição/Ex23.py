"""
    Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
    O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
    Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""


def valida_primo(num, div):
    n_primo = 0
    for i in range(2, num):
        if i <= (num**0.5):
            if num % i == 0:
                n_primo += 1
                break
        else:
            div += 1
            break
        div += 1

    if n_primo != 0:
        return div, num, False
    else:
        return div, num, True


numero = int(
    input("Digite um número inteiro para ver todos os números primos até ele: "))

numero_de_divisões = 0
numeros_primos = []

for i in range(1, numero+1):
    numero_de_divisões, n_primo, valida = valida_primo(i, numero_de_divisões)

    if valida == True:
        numeros_primos.append(n_primo)


print("\nLista de números primos:")
print(numeros_primos)
print(f"\nQuantiade de números primos: {len(numeros_primos)}")
print(f"Número de Divisões feitas: {numero_de_divisões}")
