lista = [[], []]


for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(f'Números pares: {lista[0]}')
print(f'\nNúmeros impares: {lista[1]}')
