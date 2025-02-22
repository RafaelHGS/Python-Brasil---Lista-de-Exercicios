"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

respostas_positivas = 0

print("responda escrevendo sim/nao")
for i in perguntas:
    resposta = input(f"\n{i}: ")
    if resposta.lower() == "sim":
        respostas_positivas +=1

if respostas_positivas <2:
    print("Classificada como: Inocente")
elif respostas_positivas == 2:
    print("Classificada como: Suspeita")
elif respostas_positivas >= 3 and respostas_positivas <=4:
    print("Classificada como: Cúmplice")
elif respostas_positivas == 5:
    print("Classificada como: Assassino")