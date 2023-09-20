# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
cont = 0
respostas = []
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print(pergunta['Opções'])
    r = input('Escreva a opção certa: ')
    respostas.append(r)

if respostas[0] == '4':
    cont = cont + 1

if respostas[1] == '25':
    cont = cont + 1

if respostas[2] == '5':
    cont = cont + 1

print(f'Sua pontuação é {cont}')
