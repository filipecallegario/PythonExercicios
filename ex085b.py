lista = [[], []]

for i in range(1, 8):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

print(f'Pares -> {sorted(lista[0])}')
print(f'Impares -> {sorted(lista[1])}')