"""
     Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
    mostrando uma mensagem de erro e voltando a pedir as informações.

"""

while True:
    usuario = input("Digite o seu nome de usuário: ")
    senha = input("Digite Sua senha: ")

    if usuario == senha:
        print("O usuário senha não podem ser iguais !\n")
        continue
    
    break
