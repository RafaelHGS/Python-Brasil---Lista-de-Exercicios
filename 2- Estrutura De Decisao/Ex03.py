"""
    3- Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

#Entradas
sexo = input("Informe seu sexo [F/M]= ").upper()

#Processamento
if sexo == "F":
    sexo = "F- Feminino"
elif sexo == "M":
    sexo = "M- Masculino"
else: 
    sexo = "Sexo Inválido"

#Saída
print(sexo)