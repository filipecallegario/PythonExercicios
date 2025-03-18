tupla = ('aprender', 'praticar', 'anoitecer', 'visao')

for p in tupla:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
