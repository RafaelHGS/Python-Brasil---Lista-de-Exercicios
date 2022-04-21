"""
    Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
        "Telefonou para a vítima?"
        "Esteve no local do crime?"
        "Mora perto da vítima?"
        "Devia para a vítima?"
        "Já trabalhou com a vítima?"
    O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

"""


Pessoa = ""

perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?",
             "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

respostas = []

for pergunta in perguntas:
    while True:
        print(pergunta)
        resposta = input("R (S/N): ").upper()

        if resposta == "S" or resposta == "N":
            respostas.append(resposta)
            print()
            break
        else:
            print("\nResposta inválida!\n")
            continue

respostas_positivas = sum(map(lambda x: 1 if "S" in x else 0, respostas))

if respostas_positivas == 2:
    print("Suspeita")
elif respostas_positivas >= 3 and respostas_positivas <= 4:
    print("Cúmplice")
elif respostas_positivas == 5:
    print("Assassino")
else:
    print("Inocente")
