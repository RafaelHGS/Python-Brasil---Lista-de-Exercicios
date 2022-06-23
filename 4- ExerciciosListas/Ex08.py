# Ex08- Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

def IdadeAltura(Pessoa):
    novaLista = []
    print()
    idade = int(input(f"Digite a idade da {Pessoa}ª Pessoa: "))
    altura = float(input(f"Digite a altura da {Pessoa}ª Pessoa: "))
    novaLista.append(idade), novaLista.append(altura)
    return novaLista


vetor = []

for i in range(5):
    vetor.append(IdadeAltura(i+1))

print("\n\n////////Informações na ordem inversa: ")

contador = len(vetor)
vetor.reverse()
for i in vetor:
    i.reverse()

    print()
    print(f"A altura da {contador}ª Pessoa: {i[0]}")
    print(f"A idade da {contador}ª Pessoa: {i[1]}")

    contador = contador-1
