ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0
termo = ptermo

while cont < 10:
    print(f'{termo} -> ', end='')
    cont += 1
    termo += razao
print('FIM')