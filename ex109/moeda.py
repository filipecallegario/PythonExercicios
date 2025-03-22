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