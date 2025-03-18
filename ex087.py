matriz = [[], [], []]
pares = 0
soma3 = 0
maior2 = 0

for l in range(3):
    for c in range(3):
        valor = int(input(f'Digite o valor [{l + 1}, {c + 1}] '))
        matriz[l].append(valor)
        if valor % 2 == 0:
            pares += valor
        if l == 0 and c == 2:
            soma3 += valor
        if l == 1 and c == 2:
            soma3 += valor
        if l == 2 and c == 2:
            soma3 += valor

for linha in matriz:
    print(f'[  {linha[0]}  ] [  {linha[1]}  ] [  {linha[2]}  ]')

print(f'A soma dos valores pares é {pares}')
print(f'A soma da terceira coluna é {soma3}')

if matriz[1][0] > matriz[1][1]:
    maior2 = matriz[1][0]
elif matriz[1][1] > matriz[1][2]:
    maior2 = matriz[1][1]
else:
    maior2 = matriz[1][2]

print(f'O maior número da segunda linha é {maior2}')
