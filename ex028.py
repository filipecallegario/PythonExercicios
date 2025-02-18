import random
import time

computador = [1, 2, 3, 4, 5]
escolhido = random.choice(computador)


print('-' * 10)
print('Vou pensar em um número de 1 a 5')
print('-' * 10)

n = int(input('Digite um número: '))

print('PROCESSANDO...')
time.sleep(1.5)

if n == escolhido:
    print(f'PARABÉNS!! Você escolheu {n} e o computador {escolhido}.')
else:
    print(f'VOCÊ ERROU! você escolheu {n} e o computador {escolhido}')
