def notas(*notas, sit=False):
    dados = dict()
    dados['total'] = len(notas)
    dados['maior'] = max(notas)
    dados['menor'] = min(notas)
    dados['media'] = sum(notas) / len(notas)
    if sit:
        if 4 > dados['media']:
            dados['situação'] = 'RUIM'
        elif 4 <= dados['media'] < 7:
            dados['situação'] = 'REGULAR'
        else:
            dados['situação'] = 'BOA'
    return dados


print(notas(1, 6.9, 10, 9.8, 7.5, sit=True))
