matriz = [[], [], []]

for l in range(3):
    for c in range(3):
        matriz[l].append(int(input(f'Valor {l + 1} {c + 1}: ')))

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

