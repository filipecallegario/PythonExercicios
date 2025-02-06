d = float(input('Digite uma distancia em metros: '))

print('A medida de {}m corresponde a:'.format(d))
print('{}km'.format(d / 1000))
print('{}hm'.format(d / 100))
print('{}am'.format(d / 10))
print('{:.0f}dm'.format(d * 10))
print('{:.0f}cm'.format(d * 100))
print('{:.0f}mm'.format(d * 1000))
