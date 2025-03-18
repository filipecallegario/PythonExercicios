
"""fatorial = int(input('Digite o valor para descobrir o factorial: '))
resultado = fatorial
nova = fatorial
while  nova > 1:
    nova -= 1
    resultado *= nova

print(f'FATORIAL DE {fatorial}! é {resultado}')"""
fatorial = int(input('Digite o valor para descobrir o factorial: '))
c = fatorial
resultado = 1
print(f'Calculando fatorial {fatorial}! ', end='')
while c > 0:
    print(f'{c} ', end='')
    print(f'x ' if c > 1 else '= ', end='')
    resultado *= c
    c -= 1

print(resultado)



