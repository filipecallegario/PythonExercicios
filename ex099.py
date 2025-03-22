from time import sleep

def maior(* n):
    print('Analisando os valores passados...')
    for c in n:
        print(f'{c} ', end= '')
        sleep(0.5)
    print(f'foram informados {len(n)} valores. \n O maior valor informado é {max(n)}.')
    print('-=' * 20)

maior(1, 2, 3, 7)
maior(133)
maior(133, 12, 89, 2, 2, 5, 1, 76)