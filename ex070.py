from docutils.parsers.rst.directives import value_or

nomeprodutomaisbarato = ''
maisde1000 = totalgasto = count = maisbarato = 0

print('-' * 30)
print('LOJA SUPER BARATÃO')
print('-' * 30)

while True:
    nome = str(input('Nome do produto: ')).strip()
    while True:
        try:
            preco = float(input('Preço: R$ '))
            break
        except ValueError:
            print('Digite um valor correto: R$')
    while True:
        pergunta = str(input('Deseja continuar? [S / N]')).strip().upper()
        if pergunta in 'SN':
            break
        else:
            print('Entrada invalida...')
    count += 1
    totalgasto += preco
    if preco > 1000:
        maisde1000 += 1
    if count == 1:
        maisbarato = preco
        nomeprodutomaisbarato = nome
    if preco < maisbarato:
        maisbarato = preco
        nomeprodutomaisbarato = nome
    if pergunta == 'N':
        break

print(f'O total gasto na compra é R$ {totalgasto:.2f}')
if maisde1000 == 0:
    print('Não existe nenhum produto com valor acima de R$ 1000,00')
else:
    print(f'{maisde1000} produtos custam mais de R$ 1000,00')
print(f'O nome do produto mais barato é {nomeprodutomaisbarato}')

