'''
# Criar variável para nome (str), idade (int),
# altura (float) e peso (float) de uma pessoa
# Criar variavel com ano atual (int)
# Obter o ano de nascimento da pessoa (baseada na idade e no ano atual)
# Obter o imc da pessoa com 2 casas decimais (peso e na altura da pesso)
# Exibir um texto com todos os valores na tela usando F-String (com as chaves)

'''

nome = 'Higor'
idade = 26
altura = 1.79
peso = 68.4
ano_atual = 2021

ano_nascimento = ano_atual - idade
imc = peso / (altura**2)


print(f'{nome} tem {idade} anos, {altura} de altura e peso {peso}Kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}.')
