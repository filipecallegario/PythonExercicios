cidade = str(input('Digite o nome de uma cidade: ')).upper()
splitcidade = cidade.split()
if 'SANTO' in splitcidade[0]:
    print(f'A cidade começa com Santo')
else:
    print(f'A cidade não começa com Santo')