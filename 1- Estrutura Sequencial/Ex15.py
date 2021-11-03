"""
    15- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

A) salário bruto.
B) quanto pagou ao INSS.
C) quanto pagou ao sindicato.
D) o salário líquido.
E) calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
"""
#Entradas:
ganhoPorhora = float(input("Informe o quanto você ganha por hora: "))
horasTrabalhadas = float(input("Informe o número de horas trabalhadas ao mês: "))

#Processamento
salarioMensal = ganhoPorhora * horasTrabalhadas 

descontoIR = salarioMensal*0.11
descontoINSS = salarioMensal*0.08
descontoSindicato = salarioMensal*0.05

salarioLiquido = salarioMensal - (descontoIR + descontoINSS + descontoSindicato)

#Saída
print(f"\n\n//{'//Cálculo Salário Liquido//':-^40}//\n")
print(f"+ Salário Bruto : R${salarioMensal:.2f}")
print(f"- IR (11%) : R${descontoIR:.2f}")
print(f"- INSS (11%) : R${descontoINSS:.2f}")
print(f"- Sindicato ( 5%) : R${descontoSindicato:.2f}")
print(f"= Salário Liquido : R${salarioLiquido:.2f}")
