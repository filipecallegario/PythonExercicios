from sphinx.addnodes import index

tupla = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')),
             int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))

print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3, 0) + 1}ª posição')
else:
    print('Não foi digitado o valor 3.')


pares = [i for i in tupla if i % 2 == 0]
if pares:
    print(f'Os números pares são: {", ".join(map(str, pares))}')
else:
    print('Não há números pares')
