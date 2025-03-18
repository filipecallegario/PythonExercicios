pergunta = ''
lista = []
count = 0
while pergunta != 'N':
    while True:
        try:
            lista.append(int(input('Digite o valor: ')))
            count += 1
            break
        except ValueError:
            print('Entrada invalida...')
    while True:
        pergunta = str(input('Deseja continuar? [S / N]')).upper()
        if pergunta in 'SN':
            break
        else:
            print('Entrada invalida....')
print(f'Foram digitados {count} números.')
lista.sort(reverse=True)
print(f'A lista de valores de forma ordenada {lista}')

if 5 in lista:
    print('O valor 5 foi digitado na lista.')
else:
    print('O valor 5 não foi digitado na lista')