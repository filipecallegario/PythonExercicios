lanche = ('Hamburguer', 'Pizza', 'Sorvete', 'Batata Frita', 'Coca Cola')

for comida in lanche:
    print(f'Eu vou comer {comida} ')

print('-' * 30)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('-' * 30)

for count in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[count]} na posição {count}')