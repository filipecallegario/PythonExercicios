preco = float(input('Digite o valor do produto: R$'))
print("""FORMAS DE PAGAMENTO: 
         [ 1 ] A VISTA DINHEIRO / CHEQUE
         [ 2 ] A VITA CARTÃO
         [ 3 ] CARTÃO ATÉ 2X
         [ 4 ] CARTÃO 3X OU +""")
escolha = int(input('Escolha a condição de pagamento: '))


if escolha == 1:
    print(f'O valor do produto R$ {preco:.2f} com desconto de 10% R$ {preco - preco * 10 / 100:.2f}')
elif escolha == 2:
    print(f'O valor do produto R$ {preco:.2f} com desconto de 5% R$ {preco - preco * 5 / 100:.2f}')
elif escolha == 3:
    print(f'Nessa condição de pagamento não tem desconto, o valor do produto permance R$ {preco:.2f}')
elif escolha == 4:
    parcela = int(input('Digite em quantas vezes deseja dividir? '))
    print(f'Sua compra parcelada em {parcela}x de R${(preco + preco * 20 / 100) / parcela:.2f}')
    print(f'Sua compra de R${preco}, vai custar {preco + preco * 20 / 100:.2f}')
else:
    print('Por favor escolha uma opção correta')
    print("""Digite: 
             [ 1 ] A VISTA DINHEIRO / CHEQUE
             [ 2 ] A VITA CARTÃO
             [ 3 ] CARTÃO ATÉ 2X
             [ 4 ] CARTÃO 3X OU +""")
    escolha = int(input('Escolha a condição de pagamento: '))


