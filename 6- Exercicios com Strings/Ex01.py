"""
Tamanho de strings.
Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
Exemplo de Saída:

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.

"""

def main():
    palavra1 = input("Insira a primeira palavra: ")
    palavra2 = input("Insira a segunda palavra palavra: ")

    tamanho1 = len(palavra1)
    tamanho2 = len(palavra2)

    print("\nCompara duas strings")
    print(f"String 1: {palavra1}")
    print(f"String 2: {palavra2}")
    print(f'Tamanho de "{palavra1}": {tamanho1} caracteres')
    print(f'Tamanho de "{palavra2}": {tamanho2} caracteres')

    if tamanho1 == tamanho2:
        print("As duas strings são de tamanhos iguais.")
    else:
        print("As duas strings são de tamanhos diferentes.")

    if palavra1 == palavra2:
        print("As duas strings possuem conteúdo idêntico.")
    else:
        print("As duas strings possuem conteúdo diferente.")


    return

if __name__ == "__main__":
    main()