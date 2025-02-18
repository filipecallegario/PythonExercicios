import math
a = float(input('Digite um angulo: '))

seno = math.sin(math.radians(a))
print(f'O seno do angulo {a} é {seno:.2f}')

cosseno  = math.cos(math.radians(a))
print(f'O cosseno do angulo {a} é {cosseno:.2f}')

tangente  = math.tan(math.radians(a))
print(f'A tangente do angulo {a} é {tangente:.2f}')
