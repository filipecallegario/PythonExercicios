from random import randint
from time import sleep

jogadores = {
'Jogador1': randint(1,6),
'Jogador2': randint(1,6),
'Jogador3': randint(1,6),
'Jogador4': randint(1,6),
}
print(f'Valores sorteados: ')
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)
print('Ranking dos jogadores')

ranking = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))

pos = 0
for k, v in ranking.items():
    pos += 1
    print(f'{pos}º lugar: {k} com {v}')
    sleep(0.5)

