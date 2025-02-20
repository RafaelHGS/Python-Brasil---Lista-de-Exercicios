"""
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""

def geraRelatorio(equipamentos, defeitos):
    totalDeEquipamentos = len(equipamentos)
    print(f"Quantidade de mouses: {totalDeEquipamentos}")
    print(f"{'Situação':<40}{'Quantidade':>14} {'Percentual':>15}")

    for i in range(1,5):
        defeito = sum(x['Defeito'] == defeitos[i] for x in equipamentos)
        print(f"{i}- {defeitos[i]:<40} {defeito:<13} {defeito/totalDeEquipamentos*100:>8.2f}%")

    return

def main():
    defeitos = {
    1: "Necessita de Esfera",
    2: "Necessita de Limpeza",
    3: "Necessita de Troca de Cabo ou Conector",
    4: "Quebrado ou Inutilizado"
    }

    equipamentos = []
    id = 0
    
    while id <200:
        try:
            print("\nInsira o defeito do mouse: ")
            print(f"[1]{defeitos[1]}")
            print(f"[2]{defeitos[2]}")
            print(f"[3]{defeitos[3]}")
            print(f"[4]{defeitos[4]}")
            print("[0]Encerrar")
            mouse = int(input("R:"))

            if mouse == 0:
                if len(equipamentos) > 0:
                    geraRelatorio(equipamentos, defeitos)
                print("Encerrando o programa...")
                break
            elif mouse in defeitos:
                equipamentos.append({"ID_Mouse": id, "Defeito": defeitos[mouse]})
            else:
                print("Escolha inválida!")
                continue
            id+=1

        except:
            print("Escolha inválidos!\n")
            continue

    return


if __name__ == "__main__":
    main()