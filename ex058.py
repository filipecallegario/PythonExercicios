import random
import time

computador = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolhido = random.choice(computador)
palpites = 0


print('-' * 10)
print('Vou pensar em um número de 1 a 10')
print('-' * 10)
n = 0
while n != escolhido:
    n = int(input('Digite um número: '))
    palpites += 1

    print('PROCESSANDO...')
    time.sleep(0.5)

    if n > escolhido:
        print(f'Tente um número menor!')
    elif n < escolhido:
        print(f'Tente um número maior!')
    else:
        print(f'Parabéns, você acertou em {palpites} palpites!!')