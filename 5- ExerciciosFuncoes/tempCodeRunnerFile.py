    criaLargura = ["+", "+"]
    for i in range(1, largura-1):
        criaLargura.insert(i, "-")
    novaLargura = "".join(criaLargura)

    print(novaLargura)

    for i in range(altura-2):
        print(f"|{'':>{largura}}|")

    print(novaLargura)