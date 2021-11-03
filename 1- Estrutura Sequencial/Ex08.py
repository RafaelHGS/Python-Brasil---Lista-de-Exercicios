"""
    8- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
 Calcule e mostre o total do seu salário no referido mês.
"""
horasTrabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))
salario = float(input("Informe quanto você ganhar por hora: "))
print(f"O seu salário mensal é de : R${salario*horasTrabalhadas}")