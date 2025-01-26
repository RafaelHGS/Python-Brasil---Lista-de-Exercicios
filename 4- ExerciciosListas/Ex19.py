"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
1- Windows Server           1500   17%
2- Unix                     3500   40%
3- Linux                    3000   34%
4- Netware                   500    5%
5- Mac OS                    150    2%
6- Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""

def main():
    votacao = [0]*6
    while True:
        try:
            print("Digite o número correspondente ao Sistema Operacional (1 a 6) ou 0 para encerrar:\n")
            print("1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro\n")
            resposta = int(input("Digite sua opção: "))

            if resposta == 0:
                break
            elif 1 <= resposta <= 6:
                votacao[resposta - 1] += 1
            else:
                print("Opção inválida. Digite um número entre 1 e 6 ou 0 para encerrar.")
                continue
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            


    total = sum(votacao)
    if total == 0:
        print("\nNenhum voto foi registrado.")
        return
    porcentagemDeVotos = [(x/total)*100 for x in votacao]

    print("\nResultado:")
    print("Sistema Operacional     Votos   %")
    print("-------------------     -----   ---")
    sistemas = [
        "Windows Server",
        "Unix",
        "Linux",
        "Netware",
        "Mac OS",
        "Outro",
    ]

    for i in range(6):
        print(f"{i + 1}- {sistemas[i]:<20} {votacao[i]:<8} {porcentagemDeVotos[i]:.1f}%")

    print("-------------------     -----")
    print(f"Total                   {total}")

    vencedor = max(votacao)
    indice_vencedor = votacao.index(vencedor)
    print(
        f"\nO Sistema Operacional mais votado foi o {sistemas[indice_vencedor]}, "
        f"com {vencedor} votos, correspondendo a {porcentagemDeVotos[indice_vencedor]:.1f}% dos votos."
    )

if __name__ == "__main__":
    main()