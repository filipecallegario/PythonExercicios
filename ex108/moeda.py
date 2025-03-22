def metade(preco=0):
    res = preco / 2
    return res

def dobro(preco=0):
    res = preco * 2
    return res

def aumentar(preco=0, por = 0):
    res = preco + (preco * por / 100)
    return res

def diminuir(preco=0, por = 0):
    res = preco - (preco * por / 100)
    return res

def formatacao(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')