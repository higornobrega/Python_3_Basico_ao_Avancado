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
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i}) - {opcao}:')
    r = input('Escreva a opção certa: ')

    if r == pergunta['Resposta']:
        print('Acertou Miserave')
    else:
        print('EEERRRRRRRROOOOOOOOOOOUUUUUUUUU')
