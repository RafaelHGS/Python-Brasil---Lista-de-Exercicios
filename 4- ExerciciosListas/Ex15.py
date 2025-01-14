""""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""

valores = []


print("Por favor digite as notas:")
while True:
    valor = int(input("nota: "))
    
    if valor <= -1:
        break

    valores.append(valor)

valores_invertidos = valores.copy()
valores_invertidos.reverse()

soma_valores = sum(valores)
media_valores = sum(valores)/len(valores)
acima_media = [x for x in valores if x > media_valores]
media_sete = [x for x in valores if x <7]


print("Quantidades de valores lidos: ", len(valores))
print("Valores:\n", *valores)
print("Valores Invertidos:\n", *valores_invertidos, sep="\n")
print("Soma dos valores: ", soma_valores)
print("Media Valores: ", media_valores)
print("Quantidade de valores acima da média: ", len(acima_media))
print("Quantidade de valores abaixo de 7: ", len(media_sete))

print("Mensagem Final! :D")


