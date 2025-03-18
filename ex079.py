valores = []
pergunta = ''
count = 1

while pergunta != 'N':
    while True:
        try:
            valor = int(input(f'Digite o {count}ª valor:  '))
            break
        except ValueError:
            print('Por favor, insira um número inteiro')
    if valor in valores:
        print('Valor duplicado, não vou adicionar...')
    else:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
        count += 1
    while True:
        pergunta = str(input('Deseja continuar? [S / N]')).upper()
        if pergunta in 'SN':
            break
        else:
            print(f'Entrada invalida...')
print(valores)

