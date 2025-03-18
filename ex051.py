ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
calculo = ptermo + razao * 10

for c in range(ptermo, calculo, razao):
    print(f'{c}',end='-> ')