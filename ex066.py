n = soma = 0
count = 0
countn = 0

while True:
    countn += 1
    n = int(input(f'Digite o {countn} número: '))
    if n == 999:
        break
    soma += n
    count += 1
if count == 0:
    print('Não foi digitado nenhum número')
elif count == 1:
    print(f'Foi digitado {count} número')
else:
    print(f'Foram digitados {count} números')
    print(f'A soma dos números é {soma}')

