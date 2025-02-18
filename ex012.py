p = float(input('Qual é o preço do produto? R$'))

print(f'O produto que custava R${p:.2f}, com desconto de 5%, passou a custar R${p - (p * 5 / 100):.2f}')