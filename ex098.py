from time import sleep
def contagem(inicio, fim, passo):
    lista = []
    if passo == 0:
        passo = 1
    if inicio < fim:
        espaco = ''
        count = 0
        for c in range(inicio, fim, passo):
            print(f'{c} ', end='')
            sleep(0.3)
            lista.append(c)
            count += 1
        print()
        total_caracteres = sum(len(str(item)) for item in lista)
        print(f'~' * (total_caracteres + count), end='')  # Linha de tildes baseada no total de caracteres
        print('FIM!')
    else:
        count = 0
        c = inicio
        while c >= fim:
            print(f'{c} ', end='')
            sleep(0.3)
            lista.append(c)
            c -= passo
            count += 1
        print()
        total_caracteres = sum(len(str(item)) for item in lista)
        print(f'~' * (total_caracteres + count), end='')  # Linha de tildes baseada no total de caracteres
        print('FIM!')



contagem(1, 200, 10)
contagem(10, 0, 2)

print('Agora é sua vez de personalizar a contagem: ')
inicio = int(input('Inicio:'))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if inicio > fim:
    passo = -1
print(f'Contagem de {inicio} até {fim} de 1 em 1.')
contagem(inicio, fim, passo)

