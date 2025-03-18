n = int(input('Digite a quantidade que de números que deseja mostrar da quantidade de fibonacci:  '))

a = 0
b = 1
count = 2

print(f'{a} -> {b}', end='')
while count < n:
    c = a + b
    print(f' -> {c}', end='')
    a = b
    b = c
    count += 1
print('FIM')





