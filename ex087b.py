matriz = [[], [], []]
somapares = somacoluna3 = 0
for l in range(3):
    for c in range(3):
        matriz[l].append(int(input(f'Valor [{l + 1}, {c + 1}]: ')))
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
        if c == 2:
            somacoluna3 += matriz[l][c]

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos pares é {somapares}')
print(f'A soma dos valores da 3º coluna é {somacoluna3}')
print(f'O maior número da segunda linha é {max(matriz[1])}')