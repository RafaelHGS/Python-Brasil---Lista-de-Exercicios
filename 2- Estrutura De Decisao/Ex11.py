"""
    11- As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para 
desenvolver o programa que calculará os reajustes.
    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no 
salário atual:

    -salários até R$ 280,00 (incluindo) : aumento de 20%
    -salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    -salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    -salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
        {
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.
        }
"""

#Entradas
salario = float(input("\nInforme Seu Salário no formato [R$ ****.**]: R$"))

#Processamento
if salario <= 280.00:
    percentual = 20
    novoSalario = salario * ((percentual/100)+1)
elif salario > 280.00 and salario < 700.00:
    percentual = 15
    novoSalario = salario * ((percentual/10)+1)
elif salario >= 700.00 and salario < 1500.00:
    percentual = 10
    novoSalario = salario * ((percentual/100)+1)
elif salario >= 1500.00:
    percentual = 5
    novoSalario = salario *((percentual/100)+1)

#Saída
print(f"\nSalário antes do reajuste: R${salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"o valor do aumento: R${novoSalario-salario:.2f}")
print(f"o novo salário, após o aumento: R${novoSalario:.2f}")
print()