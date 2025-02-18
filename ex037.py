n = int(input('Digite um número inteiro: '))
print('''Escolha a base de conversão:
                    [ 1 ] - binário
                    [ 2 ] - octal
                    [ 3 ] - hexadecimal''')
escolha = int(input('Sua opção: '))

if escolha == 1:
    print(f'{n} convertido para binário é {bin(n)}')
elif escolha == 2:
    print(f'{n} convertido para octal é {oct(n)}')
elif escolha == 3:
    print(f'{n} convertido para hexadecimal é {hex(n)}')