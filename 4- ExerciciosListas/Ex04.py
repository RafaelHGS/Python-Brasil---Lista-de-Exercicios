# Ex04- Faça um Programa que leia um vetor de 10 caracteres, e diga
#       quantas consoantes foram lidas. Imprima as consoantes.

VOGAIS = ["a", "e", "é", "i", "o", "ó", "ô", "u", "ú"]

caracteres = [input(f"Digite o {i+1}º caractere: ") for i in range(10)]

consoantes = [x for x in caracteres if x.lower() in VOGAIS]

print(f"\nExistem {len(consoantes)} consoantes")
print(f"\nAs consoantes são {consoantes}")
