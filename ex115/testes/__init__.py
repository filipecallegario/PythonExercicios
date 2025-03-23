from ex115 import dados

opc = 0
while opc != 4:
    print(f'~' * 45)
    print(f'{"MENU PRINCIPAL":^45}')
    print(f'~' * 45)
    print("""\033[33m1 -\033[m \033[34mVer pessoas cadastradas\033[m
\033[33m2 -\033[m \033[34mCadastrar nova pessoa\033[m
\033[33m3 -\033[m \033[34mApagar todos os registros\033[m
\033[33m4 -\033[m \033[34mSair do programa\033[m""")
    print('~' * 30)
    try:
        opc = int(input('\033[33mEscolha uma opção: \033[m'))
    except (ValueError, TypeError):
        print('\033[31mErro.. Digite um número válido..\033[m')
        continue
    except KeyboardInterrupt:
        print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
    if opc == 1:
        dados.verpessoas()
    elif opc == 2:
        dados.cadastrar()
    elif opc == 3:
        dados.apagar()
    elif opc == 4:
        print(f'Saindo do programa...')
    else:
        print(f'\033[31mOpção invalida...\033[m')
