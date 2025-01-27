"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
"""


#Para usar a função pronta, descomentar esse bloco
from random import randint as rd

"""
def lancarDados2():
    return rd(1,6)
"""

#Função que garante número aleatório, sem uso da biblioteca random.
#O uso da semente anterior é para se ter uma variabilidade maior no resultado
#Garantindo a aleatoriedade sob o tempo de execução
def lancarDados(semente_anterior=0):
    from time import time_ns
    semente = time_ns() + semente_anterior  
    return semente % 6 + 1  

def main():
    print("Gerando números aleatórios:\n")

    vetorContador = [0] * 6
    semente_anterior = 0

    for _ in range(100):
        resultado = lancarDados(semente_anterior)
        vetorContador[resultado - 1] += 1
        semente_anterior += 1  # Incrementa para variar a semente
    
    print("Resultados\n")
    print("Numero // Quantidade")
    for i in range(6):
        print(f"{i+1} {vetorContador[i]:>10}")


"""
    #Para uso de randint, descomentar esse bloco de código
    vetorContador = [0] * 6
    semente_anterior = 0

    for _ in range(100):
        resultado = lancarDados2()
        vetorContador[resultado - 1] += 1

    
    print("\nResultados 2\n")
    print("Numero // Quantidade")
    for i in range(6):
        print(f"{i+1} {vetorContador[i]:>10}")
"""

if __name__ == "__main__":
    main()