def notas(*n, sit = False):
    dados = dict()
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['media'] = sum(n) / len(n)
    if sit:
        if dados['media'] >= 7:
            dados['situacao'] = 'BOA'
        elif 7 > dados['media'] >= 4:
            dados['situacao'] = 'REGULAR'
        else:
            dados['situacao'] = 'RUIM'

    return dados



resp = notas(2, 2, 5.5, sit=True )
print(resp)
