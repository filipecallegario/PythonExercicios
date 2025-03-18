from datetime import date

dados = {}

dados['nome'] = str(input('Nome: '))
anonascimento = int(input('Ano de Nascimento: '))
dados['ctps'] = int(input('CTPS: (0 não tem): '))
anoatual = date.today().year
idade = anoatual - anonascimento
dados['idade'] = idade

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = idade + (35 - (anoatual - dados['contratação']))
print(dados)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
