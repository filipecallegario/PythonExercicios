ficha = []

while True:
    nome = str(input('Nome: '))
    while True:
        try:
            nota1 = float(input('Nota 1: '))
            break
        except ValueError:
            print('Entrada invalida...')
    while True:
        try:
            nota2 = float(input('Nota 2: '))
            break
        except ValueError:
            print('Entrada invalida...')
    while True:
        pergunta = str(input('Deseja continuar? [S / N]')).upper()
        if pergunta in 'SN':
            media = (nota1 + nota2) / 2
            ficha.append([nome, [nota1, nota2], media])
            break
    if pergunta == 'N':
        break

print('-=' * 15)
print(f'{"Nº":<4} {"NOME":<10} {"Média":>9}')
print('-'* 30)
for pos, dados in enumerate(ficha):
    print(f'{pos:<4}{dados[0]:<10}{dados[2]:>9}')


while True:
    pergunta = int(input(('Mostrar nota de qual aluno? (999 interrompe): ')))
    if pergunta == 999 :
        print('FIM')
        break
    if pergunta <= len(ficha) - 1:
        print(f'As notas de {ficha[pergunta][0]} são {ficha[pergunta][1]}')




