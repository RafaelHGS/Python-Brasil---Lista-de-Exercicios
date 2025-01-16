"""

Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m


"""

atletas = []

while True:
    atleta = []
    nomeAtleta = input("Digite o nome do Atleta (para encerrar, aperte enter): \n")

    if nomeAtleta == "":
        break

    atleta.append(nomeAtleta)
    for i in range(5):
        salto = float(input(f"Digite a distância do salto {i + 1} (Ex: 5.2): \n"))
        atleta.append(salto)
    
    atletas.append(atleta)

for atleta in atletas:
    nome = atleta[0]
    saltos = atleta[1:]  # Pega apenas os valores dos saltos
    media = sum(saltos) / len(saltos)
    
    print(f"Atleta: {nome}\n")
    print(f"Primeiro Salto: {saltos[0]} m")
    print(f"Segundo Salto: {saltos[1]} m")
    print(f"Terceiro Salto: {saltos[2]} m")
    print(f"Quarto Salto: {saltos[3]} m")
    print(f"Quinto Salto: {saltos[4]} m\n")
    print(f"Resultado final:")
    print(f"Atleta: {nome}")
    print(f"Saltos: {' - '.join(map(str, saltos))}")
    print(f"Média dos saltos: {media:.1f} m\n")