nome = str(input('Digite o nome completo da pessoa: '))

splitnome = nome.split()
ultimonome = splitnome[len(splitnome) - 1]

print(f'O primeiro nome da pessoa é {splitnome[0]} e o ultimo nome da pessoa é {ultimonome}')