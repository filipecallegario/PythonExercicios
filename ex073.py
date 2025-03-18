times = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'São Paulo', 'Internacional', 'Bahia', 'Cruzeiro',
         'Atlético-MG', 'Vasco da Gama', 'Fluminense', 'Criciúma', 'Grêmio', 'Red Bull Bragantino', 'Juventude',
         'Vitória', 'Corinthians', 'Athletico-PR', 'Cuiabá', 'Atlético-GO')

print(f'Os 5 primeiros colocados {times[0:5]}')
print(f'Os ultimos 4 colocados da tabela {times[-4:]}')
print(f'Os times em ordem alfabética {sorted(times)}')
print(f'O time flamengo está na posição {times.index('Flamengo') + 1}')