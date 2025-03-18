galera = []
dados = {}
totidade = count = 0
mulheres = []
while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M / F]')).upper()
        if dados['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F')
    dados['idade'] = int(input('Idade: '))
    galera.append(dados.copy())
    totidade += dados['idade']
    while True:
        pergunta = str(input('Deseja continuar? [S / N]')).upper()
        count += 1
        if pergunta in 'SN':
            break
        else:
            print('Entrada Invalida..')
    if pergunta == 'N':
        break

media = totidade / len(galera)
print(f'A) Foram cadastradas {len(galera)} pessoas')
print(f'B) A média de idade do grupo é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas, foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print(f'\nD) Lista de pessoas acima da média ', end="")
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end= '')
print('\n-=-=-=ENCERRADO=-=-=-')
