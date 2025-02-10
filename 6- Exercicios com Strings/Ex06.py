"""
Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
"""

def main():
    meses = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho',
    7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
    }
    data_nascimento = input("Digite a sua data de nascimento (dd/mm/aaaa): ")

    dia, mes, ano = map(int, data_nascimento.split('/'))

    print(f"Você nasceu em {dia} de {meses[mes]} de {ano}.")

if __name__ == "__main__":
    main()