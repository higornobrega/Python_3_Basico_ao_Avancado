inteiro = input("Digite um número: ")


try:
    intFormat = int(inteiro)
    if intFormat % 2 == 0:
        print("Número Par")
    else:
        print("Número Inpar")
except ValueError:
    print("Não é um número inteiro")
