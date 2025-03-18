lista = []

for c in range(1, 6):
    valor = int(input(f'Digite o {c} valor: '))
    if c == 1 or valor > lista[len(lista ) - 1]:
        lista.append(valor)
        print(f'Adicionado ao final da lista..')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Adicionado na posição {pos + 1}ª')
                break
            pos += 1
print(lista)