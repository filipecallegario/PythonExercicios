nome = str(input('Digite o nome completo: '))

pnome = nome.split()
nometam = len(nome) - nome.count(" ")
print(f'O nome com todas as letras maiusculas {nome.upper()}')
print(f'O nome com todas as letras minusculas {nome.lower()}')
print(f'O primeiro nome tem {len(pnome[0])} caracteres')
print(f' O nome tem o total de {nometam} caracteres')