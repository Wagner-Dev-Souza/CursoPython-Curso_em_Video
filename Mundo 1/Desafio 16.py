print('\33[32m='*5, 'DESAFIO 16', '='*5,'\33[m')

from math import trunc
n=float(input('Digite um número: '))
print('\33[35mO número {} tem a parte inteira {}'.format(n, trunc(n)))
