print('\33[32m='*5, 'DESAFIO 14', '='*5,'\33[m')

C = float(input('Informe a temperatura em ºC: '))
F = C * 1.8 + 32
print('A temperatura de \33[36m{}ºC\33[m corresponde a \33[35m{}ºF\33[m!'.format(C, F))
