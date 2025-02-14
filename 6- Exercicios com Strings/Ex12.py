"""
Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133

"""

def main():
    print("Valida e corrige número de telefone")
    while True:
        telefone = input("Telefone: ").replace("-","")

        if telefone.isnumeric() and (len(telefone) == 7 or len(telefone) == 8):
            if len(telefone) == 8:
                print("Telefone já possui 8 dígitos.")
                print(f"Telefone sem formatação: {telefone}")
                print(f"Telefone com formatação: {telefone[:4]}-{telefone[4:]}")
            if len(telefone) == 7:
                print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")
                novoNumero = "3"+telefone
                print(f"Telefone corrigido sem formatação: {novoNumero}")
                print(f"Telefone corrigido com formatação: {novoNumero[:4]}-{novoNumero[4:]}")
        else:
            print("Número de telefone inválido")
            continue
        break

    return

if __name__ == "__main__":
    main()