peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)
pesoideal = 24.9 * (altura * altura)

if imc < 18.5:
    print(f'Você está abaixo do peso. seu peso ideal é  {pesoideal:.2f} KG')
    print(f'Você precisa ganhar {pesoideal - peso:.2f} KG')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print(f'Sobrepeso, seu peso ideal é  {pesoideal:.2f} KG')
    print(f'Você precisa perde {peso - pesoideal:.2f} KG')
elif imc >= 30 and imc < 40:
    print(f'Obesidade, seu peso ideal é  {pesoideal:.2f} KG')
    print(f'Você precisa perde {peso - pesoideal:.2f} KG')
else:
    print(f'Obesidade Morbida, seu peso ideal é  {pesoideal:.2f} KG')
    print(f'Você precisa perde {peso - pesoideal:.2f} KG')

