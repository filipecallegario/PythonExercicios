dados = list()
galera = list()
resposta = ''
count = maior = menor  = 0

while resposta != 'N':
    dados.append(str(input('Digite o nome: ')))
    while True:
        try:
            dados.append(float(input('Digite o peso: ')))
            count += 1
            if len(galera) == 0:
                maior = menor = dados[1]
            elif dados[1] > maior:
                maior = dados[1]
            elif dados[1] < menor:
                menor = dados[1]
            galera.append(dados[:])
            dados.clear()
            break
        except ValueError:
            print('Entrada invalida..')
    while True:
        resposta = str(input('Deseja continuar? [S / N]')).upper()
        if resposta in 'SN':
            break
        else:
                print('Entrada invalida...')

print(f'Você cadastrou {count} pessoas.')
print(f'O maior peso cadastrado foi {maior}KG. ', end='')
for p in galera:
    if p[1] == maior:
        print(f'Peso de [{p[0]}]')
print(f'O menor peso cadastrado foi {menor}KG. ', end='')
for p in galera:
    if p[1] == menor:
        print(f'Peso de [{p[0]}]')
print(galera)

