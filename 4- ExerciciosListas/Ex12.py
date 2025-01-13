"""
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
"""

from random import randint as rd

#Valores de Teste para idade e altura, podem ser alterados
#Idade de alunos 10 a 18 anos:
idade = [rd(10, 18) for x in range(30)]

#altura alunos em centimetros:
altura = [rd(120, 180) for x in range(30)]


#Insira  a idade dos alunos, no nosso exemplo 13 anos
def media_altura_idade(idade_alvo):
    altura_idade_alvo = [x for x in idade if x >= idade_alvo]
    media_altura = sum(altura)/len(altura)
    alunos_inferior_media = [x for x in altura_idade_alvo if x <= media_altura]

    return alunos_inferior_media

print("o numero de alunos com altura abaixo da media escolhida é de: ", len(media_altura_idade(13)), "alunos")
print("alunos: ", media_altura_idade(13))
