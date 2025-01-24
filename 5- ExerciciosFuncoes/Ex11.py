"""
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

"""

def mesPorExtenso(data):
    # Lista de meses com 31 dias
    # Lista de meses com seus nomes e dias
    meses = [
        {"nome": "Janeiro", "dias": 31},
        {"nome": "Fevereiro", "dias": 28},  # Considerando ano não bissexto
        {"nome": "Março", "dias": 31},
        {"nome": "Abril", "dias": 30},
        {"nome": "Maio", "dias": 31},
        {"nome": "Junho", "dias": 30},
        {"nome": "Julho", "dias": 31},
        {"nome": "Agosto", "dias": 31},
        {"nome": "Setembro", "dias": 30},
        {"nome": "Outubro", "dias": 31},
        {"nome": "Novembro", "dias": 30},
        {"nome": "Dezembro", "dias": 31},
    ]

    try:
        aux =list(map(int, data.split("/")))

        #Verificações a partir do algarismo com maiores caracteres
        # Validar ano
        if aux[2] <= 0 or aux[2] > 9999:
            return None

        # Validar mês
        if aux[1] <= 0 or aux[1] > 12:
            return None


        #Dia
        mes = aux[1]-1
        dias_no_mes = meses[mes]["dias"]


        # Ajustar Fevereiro para anos bissextos
        if mes == 1 and ((aux[2] % 4 == 0 and aux[2] % 100 != 0) or (aux[2] % 400 == 0)):
            dias_no_mes = 29

        if aux[0] <= 0 or aux[0] > dias_no_mes:
            return "Dia inválido."

        return f"{aux[0]} de {meses[mes]['nome']} de {aux[2]:0>4}"
    
    except:
        return None

def main():
    while True:
        try:
            data = input("Digite uma data data no formato DD/MM/AAAA: ")
            print(mesPorExtenso(data))

            break
        except:
            print("Digite um valor válido!")
            continue


if __name__ == "__main__":
    main()