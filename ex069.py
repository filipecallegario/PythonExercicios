maior18 = homem = mulhermenor20 = 0

while True:
    print('--' * 10)
    print('CADASTRE UMA PESSOA')
    print('--' * 10)
    while True:
        try:
            idade = int(input('Digite a idade: '))
            break
        except ValueError:
            print('Por favor, digite um número inteiro válido para a idade.')
    while True:
        sexo = str(input('Digite o sexo [F / M] ')).strip().upper()
        if sexo in 'FM':
            break
        else:
            print('Entrada invalida...')
    while True:
        pergunta = str(input('Quer continuar? S/N ')).strip().upper()
        if pergunta in 'SN':
            break
        else:
            print('Entrada invalida...')
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulhermenor20 += 1
    if pergunta == 'N':
        break

print('-' * 35)
if maior18 == 0:
    print('Não foi cadastrado nenhum maior de 18 anos.')
if maior18 == 1:
    print(f'Foi cadastrado {maior18} maior de 18 anos.')
else:
    print(f'Foram cadastrados {maior18} maiores de 18 anos.')

print('-' * 35)
if homem == 0:
    print('Não foi cadastrado nenhum homem.')
elif homem == 1:
    print(f'Foi cadastrado {homem} homem.')
else:
    print(f'Foram cadastrados {maior18} homens.')

print('-' * 35)
if mulhermenor20 == 0:
    print('Não foi cadastrada nenhuma mulher menor de 20 anos.')
elif mulhermenor20 == 1:
    print(f'Foi cadastrada {mulhermenor20} mulher menor de 20 anos.')
else:
    print(f'Foram cadastradas {mulhermenor20} mulheres menores de 20 anos.')
print('-' * 35)
print('FIM')


