nome = 'Luiz Otávio'
idade = 32
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso / (altura**2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
# 
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')

print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
# No exemplo abaixo nome pode ser representado por 0, idade 1 e imc 2
print('{0} tem {1} anos de idade {1} e {0}seu imc é {2:.2f}'.format(nome, idade, imc)) 
# Também é possível declarar as representações
print('{n} tem {im} anos de idade {n} e {i}seu imc é {i:.2f}'.format(n=nome, i=idade, im=imc)) 