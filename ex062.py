ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0
termo = ptermo
pergunta = 1
while cont < 10:
    print(f'{termo} -> ', end='')
    cont += 1
    termo += razao
while True:
    pergunta = int(input('\nDeseja mostrar mais quantos termos? (Digite 0 para parar) '))
    if pergunta == 0:
        break
    else:
        for i in range(pergunta):
            print(f'{termo} -> ', end='')
            termo += razao
        print('FIM')
print('FIM')