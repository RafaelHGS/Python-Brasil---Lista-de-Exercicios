"""
    12- Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda
, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde
a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde
ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade
de horas trabalhadas no mês.

    Desconto do IR:
    -Salário Bruto até 900 (inclusive) - isento
    -Salário Bruto até 1500 (inclusive) - desconto de 5%
    -Salário Bruto até 2500 (inclusive) - desconto de 10%
    -Salário Bruto acima de 2500 - desconto de 20%
    
    Imprima na tela as informações,dispostas conforme o exemplo abaixo.
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""
#Definição de funções
def descontoIR(salario):
    if salario <= 900:
        return 0
    elif salario > 900 and salario <= 1500:
        return 5
    elif salario > 1500 and salario <= 2500:
        return 10
    else:
        return 20

def INSSeFGTS(salario):
    INSS = salario * 0.10
    FGTS = salario * 0.11
    return INSS, FGTS

def main():
    #Entradas
    ganhoPorhora = int(input("\nInforme Quanto você ganha por hora: "))
    horasTrabalhadas = int(input("Informe o Número de horas Trabalhadas: "))
    salario = ganhoPorhora * horasTrabalhadas

    #Processamento
    IR = salario*(descontoIR(salario)/100)
    INSS, FGTS = INSSeFGTS(salario)

    #Saída
    print(f"\nSalário Bruto: ({ganhoPorhora} * {horasTrabalhadas})        : R$  {salario:.2f}")
    print(f"(-) IR (5%)                     : R$  {IR:.2f}")  
    print(f"(-) INSS ( 10%)                 : R$  {INSS:.2f}")
    print(f"FGTS (11%)                      : R$  {FGTS:.2f}")
    print(f"Total de descontos              : R$  {(IR+INSS):.2f}")
    print(f"Salário Liquido                 : R$  {salario-(IR+INSS):.2f}")

if __name__ == "__main__":
    main()
