"""
    Faça um programa que leia e valide as seguintes informações:
        Nome: maior que 3 caracteres;
        Idade: entre 0 e 150;
        Salário: maior que zero;
        Sexo: 'f' ou 'm';
        Estado Civil: 's', 'c', 'v', 'd';
"""


informacoes = ["Nome", "Idade", "Salário", "Sexo", "Estado Civil"]

print("Digite suas informações:")
for i in informacoes:
    while True:
        if i == "Nome":
            nome = input("Digite seu nome: ")
            if len(nome) <= 3:
                print("O nome deve conter ao menos 3 caracteres\n")
                continue

        elif i == "Idade":
            try:
                idade = int(input("Digite sua idade: "))
                if idade < 0 or idade > 150:
                    print("A idade deve ser entre 0 e 150 !\n")
                    continue
            except:
                continue

        elif i == "Salário":
            try:
                salario = float(input("Digite seu Salário: "))
                if salario <= 0:
                    print("O salário deve ser maior que 0 (zero) !\n")
                    continue
            except:
                continue

        elif i == "Sexo":
            sexo = input("Digite seu sexo [F/M]: ").upper()
            if not (sexo == "F" or sexo == "M"):
                print("Opção inválida !\n")
                continue

        elif i == "Estado Civil":
            estado_c = input(
                "Digite seu estado civil: \n[S]Solteiro\n[C]Casado\n[V]Viúv@\n[D]Divorciado\n").upper()
            if not (estado_c == "S" or estado_c == "C" or estado_c == "V" or estado_c == "D"):
                print("A idade deve ser entre 0 e 150 !\n")
                continue

        break

print("Suas informações:")
print(f"Nome : {nome}\nIdade : {idade}\nSalário : {salario}\nSexo : {sexo}\nEstado Civel : {estado_c}")
