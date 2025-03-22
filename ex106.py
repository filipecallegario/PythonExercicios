from time import sleep

c = ('\033[m', '\033[0;30;41m', '\033[0;30;42m', '\033[0;30;43m', '\033[0;30;44m', '\033[0;30;45m', '\033[0;30;46m', '\033[0;30;47m' , '\033[7;40m')
def msg(msg1, cor=0):
    print(c[cor], end='')
    print('~' * (len(msg1) + 4))
    print(f'  {msg1}')
    print('~' * (len(msg1) + 4))
    print(c[0], end='')

def ajuda(msg):
    print(c[8], end='')
    help(msg)
    print(c[0], end='')


comando = ''
while True:
    msg('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou Biblioteca >')).lower()
    if comando == 'fim':
        break
    else:
        msg(f"Acessando o manual do comando '{comando}'", 4)
        sleep(1)
        ajuda(comando)
        print('\033[m')
        sleep(1)
msg('ATÉ LOGO!', 1)


