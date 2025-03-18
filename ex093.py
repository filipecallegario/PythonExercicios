dados = dict()
gols = []

dados['nome'] = str(input('Nome do jogador: '))
totpartidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(totpartidas):
    gol = int(input(f'Quantos gols na partida {c + 1}?'))
    gols.append(gol)

dados['gols'] = gols[:]
dados['total'] = sum((gols))
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for pos, g in enumerate(gols):
    print(f'=> Na partida {pos + 1}, fez {g} gols.')
print(f'Foi um total de {dados["total"]}')