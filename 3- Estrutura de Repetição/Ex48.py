"""
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
 123456789
 987654321

"""
# Como o execício pede um "número inteiro", irei trata-lo inicialmente como um valor númerico, e não como String

# Recebendo int
numeroInteiro = int(input("Digite um número inteiro e positivo: "))

# Cast para String
numToString = str(numeroInteiro)

# Tratando String
novaString = ""
for i, j in enumerate(numToString, 1):
    novaString = novaString + numToString[(i)*(-1)]

# Novo número inteiro, invertido
novoNumero = int(novaString)

print(f"\n\nNúmero original: {numeroInteiro}")
print(f"Número invertido: {novoNumero}")
print(f"Tipo de variável do número invertido: {type(novoNumero)}")
print()
