n = 0

while True:
    n = int(input('Digite o número para ver a taboada (Digite um número negativo para ser interrompido): '))
    print('-' * 40)
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {i * n}')
    print('-' * 40)
print('FIM')