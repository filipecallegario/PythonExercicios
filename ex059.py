escolha = 0

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

while escolha != 5:

    print("""ESCOLHA:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] saior do programa""")
    escolha = int(input('Escolha uma opção: '))

    if escolha == 1:
        print(f'O resultado da soma de {n1} + {n2} é {n1 + n2}')
    elif escolha == 2:
        print(f'O resultado da multiplicação de {n1} x {n2} é {n1 * n2}')
    elif escolha == 3:
        if n1 < n2:
            print(f'O maior número é {n2}')
        else:
            print(f'O maior número é {n1}')
    elif escolha == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif escolha == 5:
        print('Fim')
    else:
        print('Escolha uma opção correta')