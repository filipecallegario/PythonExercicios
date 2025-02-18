from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))

anoatual = date.today().year
idade = anoatual - ano

if idade < 18:
    print(f'Você vai se alistar daqui a {18 - idade} anos')
elif idade == 18:
    print('Você precisa se alistar esse ano!')
else:
    print(f'Já passou {idade - 18} anos do seu alistamento')

