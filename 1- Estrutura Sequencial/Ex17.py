# """
#     17- Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a 
# ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida
# em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

# -comprar apenas latas de 18 litros;
# -comprar apenas galões de 3,6 litros;
# -misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre 
# arredonde os valores para cima, isto é, considere latas cheias.
# """

#Definindo funções
def lata18Litros(litros):
    latas = litros/18
    if latas % 18 != 0:
        latas += 1
    return int(latas)

def galao(litros):
    galoes = litros / 3.6
    if galoes % 3.6 != 0:
        galoes += 1
    return int(galoes)

def latagalao(litros):
    litros = litros*1.1
    gastoComLata = int(litros/18)
    gastoComGalao = int((litros - (gastoComLata*18))/3.6)
    if litros - (gastoComLata * 18) % 3.6 != 0:
        gastoComGalao += 1
    return gastoComLata, gastoComGalao


def main():
    #Entradas
    metrosArea = float(input("\nInforme o tamanho em metros quadrados: "))

    #Processamento
    litrosPor3Metros = metrosArea/6
    somenteLata = lata18Litros(litrosPor3Metros)
    somenteGalao = galao(litrosPor3Metros)
    lata_E_Galao, lata_E_Galao2 = latagalao(litrosPor3Metros)

    #Saída
    print("\\nnOrçamentos para fabricação da tinta:\n\n")
    print(f"-Orçamento Apenas com Latas-")
    print(f"Quantidade de Latas: {somenteLata}")
    print(f"Preço Final = {somenteLata*80.00:.2f}")

    print(f"\n-Orçamento Apenas com Galões-")
    print(f"Quantidade de Latas: {somenteGalao}")
    print(f"Preço Final = {somenteGalao*25.00:.2f}")

    print(f'\n-Orçamento "misto"-')
    print(f"Quantidade de Latas e de galoes: {lata_E_Galao}-Latas & {lata_E_Galao2}-Galões")
    print(f"Preço Final = {(lata_E_Galao*80.0)+(lata_E_Galao2*25.00):.2f}")

if __name__ == "__main__":
    main()