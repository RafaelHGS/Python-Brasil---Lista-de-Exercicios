"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
"""


def conversao(hora, minuto):
    if hora >= 12:
        if hora == 12:
            hora_12 = 12
        else:
            hora_12 = hora - 12
        periodo = 'P'
    elif hora >= 0 and hora <12:
        if hora == 0:
            hora_12 = 12
        else:
            hora_12 = hora
        periodo = 'A'
    
    return hora_12, minuto, periodo


def saida(hora_12, minuto, periodo):
    periodo_ext = "A.M." if periodo == 'A' else "P.M."
    return f"{hora_12}:{minuto:02d} {periodo_ext}"

while True:
    try:
        horas, minutos = map(int, input("Digite um horario para a conversão (ex 14:25)): ").split(":"))
        if 0 <= horas < 24 and 0 <= minutos < 60:
            hora_12, minuto, periodo = conversao(horas, minutos)
            print(saida(horas, minutos, periodo))
            
            repetir = input("Deseja realizar outra conversão? (s/n): ").lower()
            if repetir != 's':
                break
        else:
            print("Valores de hora ou minuto fora do intervalo!")
            continue
    except:
        print("Digite um valor válido!")
        continue
