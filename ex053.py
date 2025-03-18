"""frase = str(input('Digte uma frase para verificar se é um palindromo: '))
novafrase = frase.replace(" ", '')

invertido = novafrase[::-1]

print(invertido)"""

frase = str(input('Digte uma frase para verificar se é um palindromo: ')).upper().strip()

palavras = frase.split()
junto = ''.join(palavras)

inverso = ''

for letra in range(len(junto) -1 , -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('É um PALINDROMO')
else:
    print('Não é um PALINDROMO')
