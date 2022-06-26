"""
    Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de 
    idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou 
    idosa, conforme a média calculada.

"""

n_pessoas = int(input("Quantas pessoas ?: "))
idadesPessoas = []

for i in range(n_pessoas):
    idadePessoa = int(input(f"Digite a idade da {i+1}ª Pessoa: "))
    idadesPessoas.append(idadePessoa)

media = sum(idadesPessoas)/len(idadesPessoas)

if media >= 0 and media <= 25:
    print("A turma é Jovem")

elif media >= 26 and media <= 60:
    print("A turma é Adulta")

else:
    print("A turma é Idosa")
