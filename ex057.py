sexo = str(input('Informe seu sexo [F / M] ')).upper()[0]

while sexo not in 'FfMm':
    sexo = str(input('Dados inválidos... Por favor, Informe seu sexo [F / M] ')).upper().strip()[0]
print(f'SEXO {sexo} Registrado com sucesso! ')
