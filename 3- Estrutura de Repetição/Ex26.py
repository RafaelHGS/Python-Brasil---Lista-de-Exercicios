"""
    Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
    Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato
"""

numEleitores = int(input("Numeros de eleitores: "))

numVotos = []

for i in range(numEleitores):
    voto = int(input("Digite seu voto:" +
               "\n[1]Candidato 1"+"\n[2]Candidato 2"+"\n[3]Candidato 3\n"))
    numVotos.append(voto)

print("\\\\\\\\\\\\\\\\\\\n\n\nTotal de votos:")
for i in range(3):
    votos = 0
    for j in numVotos:
        if j == (i+1):
            votos = votos + 1
    print(f"\nVotos no Canditato {i+1}: {votos}")
