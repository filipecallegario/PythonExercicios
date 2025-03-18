jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    totpartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    partidas.clear()
    for c in range(0, totpartidas):
        partidas.append(int(input(f'Quantos gols na partida {c + 1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar? [S / N]')).upper()
        if resposta in "SN":
            break
        else:
            print('Entrada invalida..')
    if resposta == 'N':
        break

print('-=' * 30)
print(' cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('_' * 40)
for k, v in enumerate(time):
    print(f'{k:>3}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro, não existe jogador com cod {busca}')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'     No jogo {i + 1} fez {g} gols')
    print('-' * 40)
print('VOLTE SEMPRE')