"""
    11- Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
A) o produto do dobro do primeiro com metade do segundo .
B) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.
"""
#Entradas
numInteiro = int(input("Informe um número inteiro: "))
numReal = float(input("Informe um número Real: "))

#Processamento
resultado1 = (numInteiro*2)*(numReal/2)
resultado2 = (numInteiro*3)+resultado1

#Saída
print(f"O produto do dobro de {numInteiro} com metade de {numReal}: {resultado1}")
print(f"A soma do triplo de {numInteiro} com o {resultado1}: {resultado2}")
print(f"{resultado2} elevado ao cubo: {resultado2**3}")