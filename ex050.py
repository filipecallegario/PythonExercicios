soma = 0

for c in range(1, 7):
    n = int(input(f'Digite um o {c}º número: '))
    if n % 2 == 0:
        soma += n

if n % 2 == 0:
    print(f'A soma dos números pares é {soma}')
else:
    print('Não teve número par')