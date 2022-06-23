# Ex03- Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = [float(input(f"Digite a {i}ª nota: ")) for i in range(4)]
print(f"\nMédia = {sum(notas)/len(notas)}")
