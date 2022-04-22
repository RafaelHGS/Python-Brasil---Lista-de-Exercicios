"""
        Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de 
    crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
        Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
    ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

        Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento
    iniciais. Valide a entrada e permita repetir a operação.

"""

while True:
    try:
        print("Informe a seguir duas populações e suas taxas de crescimento anuais")
        print(
            "OBS: A maior populaçao deve conter uma taxa de crescimento menor que a outra")

        populacao_A = int(input("Habitantes da População A: "))
        populacao_B = int(input("Habitantes da População B: "))

        if populacao_A >= populacao_B:
            print("A População A deve ser menor que a população B")
            continue
        break

    except:
        print("Numero de habitantes inválido !")
        continue

while True:
    try:
        taxa_pop_A = int(
            input("Digite o crescimento da População A (0 a 100): "))
        taxa_pop_B = int(
            input("Digite o crescimento da População B (0 a 100): "))

        if (taxa_pop_A or taxa_pop_B) < 0 or (taxa_pop_A or taxa_pop_B) > 100:
            print("Taxa inválida")
            continue

        if taxa_pop_A <= taxa_pop_B:
            print("A População A deve ter a taxa maior que a população B")
            continue
        break

    except:
        print("Taxa inválida")
        continue


contagem_de_anos = 0
while populacao_A <= populacao_B:
    populacao_A = populacao_A + (populacao_A*(taxa_pop_A/100))
    populacao_B = populacao_B + (populacao_B*(taxa_pop_B/100))
    contagem_de_anos += 1

print(f"Levarão {contagem_de_anos} anos para a População A se igualar ou ultrapassar a População B")
