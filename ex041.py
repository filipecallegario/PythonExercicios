from datetime import date

nascimento = int(input('Digite o ano de nascimento: '))

anoatual = date.today().year
idade = anoatual - nascimento

if idade <= 9:
    print(f'{idade} -> Categoria MIRIM')
elif idade <= 14:
    print(f'{idade} -> Categoria INFANTIL')
elif idade <= 19:
    print(f'{idade} -> Categoria JUNIOR')
elif idade <= 20:
    print(f'{idade} -> Categoria SENIOR')
else:
    print(f'{idade} -> Categoria MASTER')