from datetime import date

anoatual = date.today().year
totmaior = 0
totmenor = 0

for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {c}º pessoa: '))
    idade = anoatual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Existem {totmaior} pessoas Maiores de 21 anos')
print(f'Existem {totmenor} pessoas menores de 21 anos')