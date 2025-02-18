r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'As retas podem formar um triangulo ', end='')
    if r1 == r2 == r3:
        print(f'EQUILÁTERO! ')
    elif r1 != r2 != r3 != r1:
        print(f'ESCALENO!')
    else:
        print('ISOSCELES!')
else:
    print('Não pode formar um triangulo')