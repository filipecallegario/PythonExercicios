d = float(input('Digite a distancia da viagem: '))

menos200 = d * 0.5
mais200 = d * 0.45

if d <= 200:
    print(f'O preço da passagem é de R$ {menos200}')
else:
    print(f'O preço da passagem é de R$ {mais200}')