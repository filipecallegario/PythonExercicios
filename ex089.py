ficha = list()
pergunta =  ''
count = 0

while pergunta != 'N':
    nome = str(input('Nome: '))
    while True:
        try:
            nota1 = float(input('Nota 1: '))
            break
        except ValueError:
            print("Por favor, insira um número válido para a Nota 1.")
    while True:
        try:
            nota2 = float(input('Nota 2: '))
            break
        except ValueError:
            print("Por favor, insira um número válido para a Nota 2.")
    while True:
        pergunta = str(input('Deseja continuar? [S / N]')).upper()
        if pergunta in 'SN':
            count += 1
            break
        else:
            print('Entrada invalida...')

    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

print('-=' * 15)
print(f'{"Nº":<4} {"NOME":<10} {"Média":>9}')
print('-'* 30)
for pos, dados in enumerate(ficha):
    print(f'{pos:<4} {dados[0]:<10} {dados[2]:>8.1f}')
while True:
    resposta = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if resposta == 999:
        print('Fim')
        break
    if resposta <= len(ficha) - 1:
        print(f'As notas de {ficha[resposta][0]} são {ficha[resposta][1]}')







