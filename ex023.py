numero = int(input('Digite um número de 0 a 9999: '))
n = str(numero)
print(f'Analisando o número {n}')
if numero < 0 or numero > 9999:
    numero = int(input('Digite um número de 0 a 9999: '))
if len(n) == 4:
    print(f'Unidade {n[3]}')
    print(f'Dezena {n[2]}')
    print(f'Centena {n[1]}')
    print(f'Milhar {n[0]}')
elif len(n) == 3:
    print(f'Unidade {n[2]}')
    print(f'Dezena {n[1]}')
    print(f'Centena {n[0]}')
    print(f'Milhar 0')
elif len(n) == 2:
    print(f'Unidade {n[1]}')
    print(f'Dezena {n[0]}')
    print(f'Centena 0')
    print(f'Milhar 0')
elif len(n) == 1:
    print(f'Unidade {n[0]}')
    print(f'Dezena 0')
    print(f'Centena 0')
    print(f'Milhar 0')