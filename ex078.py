valores = []
maior = menor = posmenor = posmaior = 0

for c in range(1, 6):
    valores.append(int(input(f'Digite o valor para posição {c}: ')))

    for pos, valor in enumerate(valores):
        if pos == 0:
            maior = valor
            menor = valor
        elif valor > maior:
            maior = valor
            posmaior = pos
        elif valor < menor:
            menor = valor
            posmenor = pos

print(valores)
print(f'O maior valor é {maior} na posição {posmaior + 1}ª')
print(f'O menor valor é {menor} na posição {posmenor + 1}ª')