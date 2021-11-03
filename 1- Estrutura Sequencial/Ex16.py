"""
    16- Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área 
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é 
vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total.
"""
import math

#Entradas

metrosArea = float(input("\nInforme o tamanho em metros quadrados: "))

#Processamento
litrosPor3Metros = metrosArea/3

#Tratamento de Erros
if litrosPor3Metros % 18 == 0:  #Se a quantidade de Tinta for divisivel por 18, dá a quantidade exata de latas
    quantidadeDeLatas = litrosPor3Metros / 18
else:
    #Se a quantiade não for divisivel, ele usará um numero de latas acima que pode ser usada para tingir a área:
    #Ex: 54m²/3 = 18L/3m² = 1ª (uma) Lata
    #Ex2: 55/3 = 18.333 = 2ªs (duas) Latas necesárias para pintar a área total
    quantidadeDeLatas= math.ceil(litrosPor3Metros/18)

#Saída
print(f"\nA Quantidade de Latas de tinta compradas deve ser de: {quantidadeDeLatas:.0f} Lata(s)")
print(f"Preço total: R${quantidadeDeLatas*80.00:.2f}")