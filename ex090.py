dados = dict()

dados['nome'] = str(input('Nome: '))
dados['media'] = float(input('Média: '))

if dados['media'] >= 7:
    dados['situação'] = "Aprovado"
elif 5 <= dados['media']:
    dados['situação'] = "Recuperação"
else:
    dados['situação'] = 'Reprovado'

for k, v in dados.items():
    print(f'{k} é igual a {v}')
