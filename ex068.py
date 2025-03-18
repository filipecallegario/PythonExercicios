from random import choice
count = 0

computador = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('-=-' * 8)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=-' * 8)
while True:
    sorteio = choice(computador)
    n = int(input('Digite um valor: '))
    escolha = str(input('Digite PAR OU IMPAR ')).strip().upper()
    print('---' * 10)
    if (n + sorteio) % 2 == 0 and escolha == 'PAR' :
        print(f'Você jogou {n} e o computador {sorteio}. Total de {n + sorteio} DEU PAR')
        print('---' * 10)
        print('Você venceu!!')
        print('Vamos jogar novamente!')
        print('---' * 10)
        count += 1
    else:
        print(f'Você jogou {n} e o computador {sorteio}. Total de {n + sorteio} DEU IMPAR')
        print('Você perdeu! ')
        print('---' * 10)
        break
if count == 1:
    print(f'Você ganhou {count} vitória...')
elif count > 1:
    print(f'Você ganhou {count} vitórias consecutivas...')

