s = float(input('Qual o salário do funcionário? R$'))

print(f'Um funcionário que ganhava R${s:.2f}, com 15% de aumento, passa a receber R${s + (s * 15 / 100):.2f}')