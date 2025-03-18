print('-' * 30)
print('BANCO BLT')
print('-' * 30)
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0
valor = int(input('Qual valor quer sacar? '))

while valor > 0:
    if valor >= 50:
        nota50 += 1
        valor -= 50
    elif valor >= 20:
        nota20 += 1
        valor -= 20
    elif valor >= 10:
        nota10 += 1
        valor -= 10
    elif valor >= 1:
        nota1 += 1
        valor -= 1

if nota50 == 0:
    pass
else:
    print(f'Total de {nota50} cédulas de R$ 50,00')

if nota20 == 0:
    pass
else:
    print(f'Total de {nota20} cédulas de R$ 20,00')

if nota10 == 0:
    pass
else:
    print(f'Total de {nota10} cédulas de R$ 10,00')

if nota1 == 0:
    pass
else:
    print(f'Total de {nota1} cédulas de R$ 1,00')
print('Volte Sempre!')