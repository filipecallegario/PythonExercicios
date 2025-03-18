from time import sleep
import random

from pygame.event import clear

todos_os_jogos = []

print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
valor = int(input('Quantos jogos você quer que eu sorteie? '))

print(f'-=-=-= SORTEANDO {valor} JOGOS =-=-=-')
for c in range(valor):
    todos_os_jogos.append(random.sample(range(1, 61), 6))

for count, jogo in enumerate(todos_os_jogos, 1):
    print(f'Jogo {count}: {jogo} ')
    sleep(0.5)
print('-=-=-=-=-=-= BOA SORTE =-=-=-=-=-=-')

