s = float(input('Digite o salario do funcionario R$'))

maiors = s + (s * 10 / 100)
menors = s + (s * 15 / 100)
if s > 1250:
    print(f'O novo salario do funcionário com aumento de 10% é de R${maiors:.2f}')
else:
    print(f'O novo salario do funcionário com aumento de 15% é de R${menors:.2f}')