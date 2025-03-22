def fatorial(n=1, show=False):
    """
    -> Calcula a fatorial de um número.
    :param n: O número a ser calculado.
    :param show: opcional, mostrar ou não a Conta.
    :return: o valor fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, - 1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


n = int(input('Digite o número para descobrir a fatorial: '))
show = str(input('Deseja mostrar o calculo? [S / N] ')).upper()
if show == 'S':
    show = True
elif show == 'N':
    show = False
print(fatorial(n, show))
