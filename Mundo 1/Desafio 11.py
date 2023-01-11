print('\33[32m='*5, 'DESAFIO 11', '='*5,'\33[m')

l = float(input('Insira a largura em metros: '))
h = float(input('Insira a altura em metros: '))
a = l*h
t = a/2
print('A área mede \33[31m{:.3f}\33[m m² e você precisará de \33[31m{:.3f}\33[m litros de tinta para pintá-la'.format(a, t))