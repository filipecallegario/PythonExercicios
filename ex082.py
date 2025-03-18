lista = []
pergunta = ''
pares = []
impares = []

while pergunta != 'N':
    while True:
        try:
            valor = int(input('Digite o valor: '))
            break
        except ValueError:
            print('Entrada invalida...')
    while True:
        pergunta = str(input('Deseja continuar? [S / N] ')).upper()
        if pergunta in 'SN':
            break
        else:
            print('Entrada invalida...')
    if valor % 2 == 0:
        lista.append(valor)
        pares.append(valor)
    else:
        lista.append(valor)
        impares.append(valor)
print('-' * 20)
print(f'Lista cheia -> {lista}')
print(f'Lista pares -> {pares}')
print(f'Lista impares -> {impares}')