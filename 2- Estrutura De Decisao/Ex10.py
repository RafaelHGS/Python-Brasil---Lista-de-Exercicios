"""
    10- Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino 
ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

#Entrada
print("Qual Turno você estuda ?\n")
print("[M]- Matutino")
print("[V]- Vespertino")
print("[N]- Noturno")
turno = input("[M/V/N]:").upper()
print()

#Processamento e Saída
if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
