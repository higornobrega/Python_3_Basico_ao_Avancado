'''
Formatando valores com modificador

:s - Text (string): Informa que é uma string
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float) :.2f
:(CARACTERE)(> OU < OU ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
'''

#EX
num_1 = 1
print(f'{num_1:0>10}') #Coloca a quantidades de 0, a esquerda, que faça com que o número tenha 10 dígitos

num_2 = 1150
print(f'{num_2:0^10}') #Coloca o número no centro
print(f'{num_2:.2f}') #Coloca 2 0 após o número
print(f'{num_2:0>10.2f}') #Coloca 2 0 após o número e completa o que falta para completar o 10 dígitos com 0 

nome = "Higor Stefany"

print(f'{nome:#^50}') #Coloca 'nome' no centro e completa o resto, para a esquerda e direita, com '#'

nome_formatado = '{}'.format(nome) #Mostra 'nome'
nome_formatado = '{:@>50}'.format(nome) #Coloca 'nome' na direita e completa o resto, para completar os 50 caracteres, com '@'

print(nome.lower()) #Tudo minusculo
print(nome.upper()) #Tudo maiusculo
print(nome.title()) #Primeiras letras maiusculas
