frase = str(input('Digite a frase: ')).upper()

print(f'A letra "A" aparece {frase.count('A')} vezes')
print(f'A letra "A" aparece na posição {frase.find('A') + 1}ª pela primeira vez')
print(f'A letra "A" aparece na posição {frase.rfind('A') + 1}ª pela ultima vez')
