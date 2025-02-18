from datetime import date
a = int(input('Digite o ano que quer analisar? Se deseja analisar o ano atual aperta 0: '))

if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 == 0 and a % 400 == 0:
    print(f'{a} é um ano BISSEXTO!')
else:
    print(f'{a} não é um ano BISSEXTO!')