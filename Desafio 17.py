print('='*5, 'DESAFIO 17', '='*5)

from math import sqrt
co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
h2 = co**2 + ca**2
h = sqrt(h2)
print('Para os catetos {} e {} a hipotenusa é igual a {:.2f}'.format(co, ca, h))
