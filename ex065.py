

pergunta = ''
maior = menor = soma  = n = 0
count = 0


while pergunta in 'sS':
    n = int(input(f'Digite o {count} número:'))
    count += 1
    soma += n
    pergunta = str(input('Deseja continuar? [ S / N ]')).upper()
    if count == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
print(f'A media dos valores digitados é {soma / count}')
print(f'O maior valor digitado for {maior}')
print(f'O menor valor digitado for {menor}')

