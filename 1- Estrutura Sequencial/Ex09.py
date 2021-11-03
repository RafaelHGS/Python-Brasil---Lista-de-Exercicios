"""
    9- Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em
 graus Celsius.
fórmula = C = 5 * ((F-32) / 9).
"""
temperatura = float(input("Informe a Temperatura em Fahrenheit: "))
print(f"A temperatura em Celsius é de {5 * ((temperatura-32) / 9):.2f}ºC")