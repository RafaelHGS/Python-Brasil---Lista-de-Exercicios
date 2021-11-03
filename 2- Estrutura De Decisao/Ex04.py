"""
    4- Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

#Entradas
letra= input("Informe uma Letra: ").lower()

#Processametno
listaDeVogais = ["a","e","i","o","u"]

if letra in listaDeVogais:
    vogalOuConsoante = "Vogal"
elif letra not in listaDeVogais:
    vogalOuConsoante = "Consoante"

#Saída
print(f'A letra digitada é uma {vogalOuConsoante}')