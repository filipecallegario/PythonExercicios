velocidade = int(input('Digite a velocidade do carro: '))

multa = (velocidade - 80) * 7
if velocidade <= 80:
    print(f'Sua velocidade de {velocidade}KM está dentro do limite da vida')
else:
    print(f'Você passou a {velocidade}KM e excedeu o limite da via, MULTA de R$ {multa:.2f}')
