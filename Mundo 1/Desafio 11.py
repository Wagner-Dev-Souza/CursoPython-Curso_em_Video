print('='*5, 'DESAFIO 11', '='*5)

l = float(input('Insira a largura em metros: '))
h = float(input('Insira a altura em metros: '))
a = l*h
t = a/2
print('A área mede {:.3f} m² e você precisará de {:.3f} litros de tinta para pintá-la'.format(a, t))