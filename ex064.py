n = 0
soma = 0
count = 0
while True:
    n = int(input('Digite o número: '))
    if n == 999:
        break
    count += 1
    soma += n
print(f'Foram digitados {count} números: ')
print(f'A soma entre eles é {soma}')