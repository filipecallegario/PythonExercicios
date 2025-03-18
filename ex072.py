
pergunta = ''
extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while pergunta != 'N':
    while True:
        try:
            n = int(input('Digite um número de 0 a 20: '))
            if 0 <= n <= 20:
                break
        except ValueError:
            print('Entrada invalida..')

    for pos, numero in enumerate(extenso):
        if n == pos:
            print(f'Você digitou o número {numero}')
    while True:
        pergunta = str(input('Deseja Continuar? [S / N]')).upper()
        if pergunta in 'SN':
            break
        else:
            print('Deseja Continuar? [S / N]')
print('Fim')





