import  random
maior = menor = 0
tupla = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print(f'Os números sorteados são: ', end='')
for count in tupla:
    print(f'{count} ', end='')
print(f'\nO maior número é {max(tupla)}')
print(f'O menor número é {min(tupla)}')