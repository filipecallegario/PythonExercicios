def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else formatacao(res)

def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else formatacao(res)

def aumentar(preco=0, por=0, formato=False):
    res = preco + (preco * por / 100)
    return res if formato is False else formatacao(res)

def diminuir(preco=0, por=0, formato=False):
    res = preco - (preco * por / 100)
    return res if formato is False else formatacao(res)

def formatacao(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco=0, por1=0, por2=0):
    print('~' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('~' * 40)
    print(f'{"Preço analisado:":<30} {formatacao(preco)}')
    print(f'{"Dobro do preço:":<30} {dobro(preco, True)}')
    print(f'{"Metade do preço:":<30} {metade(preco, True)}')
    print(f'{por1}{"% de aumento:":<28} {aumentar(preco, por1, True):}')
    print(f'{por2}{"% de redução:":<28} {diminuir(preco, por2, True):}')
    print('~' * 40)