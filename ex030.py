n = int(input('Digite um número: '))

if n % 2 == 0:
    print(f'{n} é \033[1:33mPAR\033[m')
else:
    print(f'{n} é \033[1:34mIMPAR\033[m')