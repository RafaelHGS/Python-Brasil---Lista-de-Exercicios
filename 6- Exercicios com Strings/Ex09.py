"""
Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.
"""

def verificaCPF(cpf = list):

    novoCPF = cpf[:-2]

    for i in novoCPF:
        if len(set(novoCPF)) == 1:
            return "Cpf Inválido"

    for k in range(2):
        digitoVerificador = 10
        if len(novoCPF) > 9:
            digitoVerificador +=1

        somaDigitos = 0
        for i in range(digitoVerificador-1):
            somaDigitos += novoCPF[i] * (digitoVerificador - i)

        digito = somaDigitos % 11
        
        if digito < 2:
            digito = 0
        else:
            digito = 11 - digito

        novoCPF.append(digito)

    return novoCPF


def main():
    while True:
        cpf = input("\nDigite o cpf no formato: xxx.xxx.xxx-xx: ").replace(".", "")

        if not cpf.isnumeric() or len(cpf) != 11:
            print("Cpf Inválidooooo!")
            continue

        novoCPF = list(map(int, cpf))
        novoCPF = "".join(map(str,verificaCPF(novoCPF)))
        
        if cpf == novoCPF:
            print("Cpf válido")
        else:
            print("Cpf inválido")
        
        break
        


if __name__ == "__main__":
    main()