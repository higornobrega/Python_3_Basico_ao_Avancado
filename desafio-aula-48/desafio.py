# '''Minha solução'''
# cpf = input('Digite seu cpf ')
# # cpf = '10879179481'
# cont = 0
# mult = 10
# soma = 0
# while mult > 1:
#     print
#     if(cpf[cont]).isdigit():
#         soma = soma + (int(cpf[cont])*mult)
#         mult -= 1
#     cont += 1


# digito1 = 11 - (soma % 11)

# if digito1 > 9:
#     digito1 = 0

# cont = 0
# mult = 11
# soma = 0

# while mult >2:
#     if(cpf[cont]).isdigit():
#         soma = soma + (int(cpf[cont])*mult)
#         mult -= 1
#     cont += 1
    


# soma = soma + (digito1 * 2)
# digito2 = 11 - (soma % 11)
# if digito2 > 9:
#     digito2 = 0


# if digito1 == int(cpf[-2]) and digito2 == int(cpf[-1]):
#     print("CPF VÁLIDOOOO!!!")
# else:
#     print("CPF NÃÃÃOOOO VÁLIDOOOO!!!")


'''Solução do Professor'''
cpf = input('Digite seu cpf: ')
novo_cpf = cpf[:-2] #[:9]
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)
        if d> 9:
            d=0
        total = 0
        novo_cpf += str(d)

if cpf == novo_cpf:
    print('valido')
else:
    print('Inválido')