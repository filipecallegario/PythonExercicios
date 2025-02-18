print('\033[4:34mFINANCIAMENTO CASA\033[m')

valor = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o salário do comprador: R$ '))
anos = int(input('Quantos anos deseja pagar? '))

pmensal = valor / (anos * 12)

if pmensal > salario * 30 / 100:
    print(f'\033[1:31EMPRESTIMO NEGADO!\033[m')
else:
    print(f'Parabéns, emprestimo aprovado!')
    print(f'Você pagará R$ {pmensal} por mês, em {anos} anos')