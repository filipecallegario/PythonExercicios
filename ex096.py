def area(a, b):
    a * b
    print(f'A area de um terreno {a}x{b} é de {a * b}m².')

print('CONTROLE DE TERRENOS')
print('-' * 20)

area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))
