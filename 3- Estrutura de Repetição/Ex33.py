"""
    O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
    indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a 
    média das temperaturas.
"""

temperaturas = []

contador = 1
while True:
    temperatura = float(input(f"Digite a {contador}ª temperatura (Cº): "))
    contador = contador + 1
    temperaturas.append(temperatura)

    print()
    op = int(input("Deseja continuar ?" + "\n[1]Sim" + "\n[2]Não" + "\nR: "))

    if op == 1:
        continue
    else:
        break

temperaturas.sort()

print(f"A maior temperatura: {temperaturas[-1]}")
print(f"A menor temperatura: {temperaturas[0]}")
print(f"A média das temperaturas: {sum(temperaturas)/len(temperaturas)}")
