def leiaint(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            break
        else:
            print('\033[31mErro.. Digite um número inteiro válido..\033[m')
    return valor
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')