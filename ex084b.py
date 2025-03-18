

dados = list()
galera = list()
maior = menor = 0


while True:
    dados.append(str(input('Digite o nome: ')))
    while True:
        try:
            dados.append(float(input('Digite o peso: ')))
            break
        except ValueError:
            print('Entrada invalida..')
    if len(galera) == 0:
        maior = menor = dados[1]
    elif dados[1] > maior:
        maior = dados[1]
    elif dados[1] < menor:
        menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    while True:
        resposta = str(input('Deseja continuar? [S / N]')).upper()
        if resposta in 'SN':
            break
        else:
            print('Entrada invalida...')
    if resposta == 'N':
        break
print(f'Ao todo, foram cadastrados {len(galera)}')
print(f'O maior peso foi de {maior}. Peso de ', end='')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')

print(f'\nO menor peso foi de {menor}. Peso de ', end='')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')






