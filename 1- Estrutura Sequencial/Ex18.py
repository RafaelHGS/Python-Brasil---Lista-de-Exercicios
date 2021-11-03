"""
    18- Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um
link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este
link (em minutos).
"""

#Entrada de Dados
arquivoParaDownload = float(input("\nInforme o Tamanho do Arquivo para Download (em MB): "))
linkDeInternet = float(input("Informe Sua velocidade de Internet (link) em Mbps: "))

#Processamento
tempoDeDownload = (arquivoParaDownload/(linkDeInternet))/60

#Saída
print(f"\nO tempo aproximado para consclusão do download do arquivo é de : {tempoDeDownload:.2f} minutos")
