from math import hypot

co = float(input('Digite o cateto oposto do triangulo retangulo: '))
ca = float(input('Digite o cateto adjacente do triangulo retangulo: '))

h = hypot(co, ca)

print(f'O comprimento da hipotenusa é {h:.2f}')

""""""
