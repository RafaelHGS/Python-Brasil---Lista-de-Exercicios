"""
    Faça um programa que calcule o mostre a média aritmética de N notas.
"""

n_notas = int(input("Quantas notas você deseja inserir ?: "))
notas = []

for i in range(1, n_notas+1):
    while True:
        try:
            nota = float(input(f"Digite a {i}ª nota: "))

            if nota < 0 or nota > 10:
                print("Digite uma nota de 0 a 10 !")
                continue

            notas.append(nota)
            break
        except:
            print("Erro de operação")
            continue

print(f"A Média aritmética das notas é: {sum(notas)/len(notas)}")
