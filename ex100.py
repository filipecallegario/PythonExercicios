from random import randint
from time import sleep

numeros = []

def sorteio():
    print(f'Sortendo 5 valores da lista.', end='')
    for c in range(5):
        numeros.append(randint(1, 10))
    for c in numeros:
        print(f' {c} ', end='')
        sleep(0.5)
    print()

def somapar():
    pares = []
    print(f'A soma dos números ', end='')
    for c in numeros:
        if c % 2 == 0:
            print(f'[{c}]', end='')
            pares.append(c)
    print(f' é {sum(pares)}')

sorteio()
somapar()