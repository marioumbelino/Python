from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
jogadores['Jogador1'] = randint(1, 6)
jogadores['Jogador2'] = randint(1, 6)
jogadores['Jogador3'] = randint(1, 6)
jogadores['Jogador4'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = {}
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-' * 10, 'Ranking', '-' * 10)
for k, v in enumerate(ranking):
    print(f'{k + 1}º - {v[0]} com {v[1]}')