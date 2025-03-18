from time import sleep
from random import sample
jogos = []

print('-' * 30)
print(f'{"JOGA DA MEGA SENA":^30}')
print('-' * 30)

valor = int(input('Quantos jogos quer que eu sorteie? '))
print(f'{f"-=-=-= SORTEANDO {valor} JOGOS =-=-=-":^30}')
for c in range(valor):
    jogos.append(sample(range(1, 61), 6))
    print(f'Jogo {c + 1}: {jogos[c]}')
    sleep(0.5)
print('-=' * 6, end='')
print(f'{" BOA SORTE":^10}', end='')
print('=-' * 6)

