print('='*5, 'DESAFIO 17', '='*5)

from math import sqrt
co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
h2 = co**2 + ca**2
h = sqrt(h2)
print('Para os catetos \33[32m{}\33[m e \33[32m{}\33[m a hipotenusa é igual a \33[31m{:.2f}\33[m'.format(co, ca, h))
