listagem = ('Pão', 1, 'Leite', 4.99, 'Arroz', 5.50, 'Coca Coca', 9.90, 'Bombom Garoto', 212.39)

print('_' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('_' * 40)
for pos, item in enumerate(listagem):
    if pos % 2 == 0:
        print(f'{item:.<30}', end='')
    else:
        print(f'R${item:>6.2f}')
print('_' * 40)