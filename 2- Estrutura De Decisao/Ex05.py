"""
    5- Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a
média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

#Entrada de Dados
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

#Processamento
media = (nota1 + nota2)/2

if media == 10:
    aprovadoOuReprovado = "Aprovado com Distinção"
elif media >= 7 and media < 10:
    aprovadoOuReprovado = "Aprovado"
elif media < 7:
    aprovadoOuReprovado = "Reprovado"
#Saída
print(aprovadoOuReprovado)
