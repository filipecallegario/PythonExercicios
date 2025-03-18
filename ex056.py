totidade = 0
totmulhermenor20 = 0
idademaisvelho = 0
nomemaisvelho = ''


for c in range(1, 5):
    print(f'{c}ª PESSOA')
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade:'))
    sexo = str(input('Digite o sexo: F / M ')).upper()

    totidade += idade
    if c == 1 and sexo == 'M':
        idademaisvelho = idade
        nomemaisvelho = nome
    if sexo == 'M' and idade >= idademaisvelho:
        idademaisvelho = idade
        nomemaisvelho = nome
    if idade > 20 and sexo == 'F':
        totmulhermenor20 += 1
print(f'A média das idades é {totidade / 4}')
if totmulhermenor20 == 0:
    print(f'Não há mulheres menores que 20 anos.')
else:
    print(f'O total de mulheres menores que 20 é {totmulhermenor20}')
print(f'O nome do homem mais velho é {nomemaisvelho} com {idademaisvelho} anos')
