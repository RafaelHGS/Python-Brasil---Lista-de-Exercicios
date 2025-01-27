"""
Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.
"""

def ConstroiRetangulo(largura = 0, altura = 0):
    proporcao = 1.78 #Valor de conversão para a proporção 16:9, comum de monitores

    proporcao = 1.78  # Proporção 16:9

    # Ajustar largura e altura com base na proporção, mantendo os limites de 1 a 20
    if (largura < 1 or largura > 20) and altura > 0:
        largura = int(altura * proporcao)
    elif (altura < 1 or altura > 20) and largura > 0:
        altura = int(largura / proporcao)

    # Garantir que largura e altura estejam dentro do intervalo permitido
    largura = max(1, min(largura, 20))
    altura = max(1, min(altura, 20))

    # Desenha a borda superior
    print("+" + "-" * (largura - 2) + "+")
    
    # Desenha as linhas intermediárias
    for _ in range(altura - 2):
        print("|" + " " * (largura - 2) + "|")
    
    # Desenha a borda inferior, se a altura for maior que 1
    if altura > 1:
        print("+" + "-" * (largura - 2) + "+")


    return

def main():
    print("Exemplo 1: Largura maior que o limite, ajustada pela altura com proporcionalidade")
    ConstroiRetangulo(25, 10)  # Largura fora do limite, ajustada pela proporção
    
    print("\nExemplo 2: Altura maior que o limite, ajustada pela largura com proporcionalidade")
    ConstroiRetangulo(10, 25)  # Altura fora do limite, ajustada pela proporção
    
    print("\nExemplo 3: Ambos os valores dentro do limite")
    ConstroiRetangulo(16, 9)  # Proporção 16:9
    
    print("\nExemplo 4: Ambos os valores ausentes")
    ConstroiRetangulo(0, 0)  # Inválido (não desenha o retângulo)
    return

if __name__ == "__main__":
    main()