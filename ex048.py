soma = 0
cont = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 == 1:
        soma += c
        cont += 1
print(f'A soma dos números impares que são multiplos de 3 é {soma}')
print(f'existem {cont} números')