nome = input("Digite seu nome: ")

tamanho = len(nome)


if tamanho < 5:
    print("Seu nome é Curto")
elif tamanho > 4 and tamanho < 7:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")