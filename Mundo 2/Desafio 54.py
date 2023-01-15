print('\33[33m{:=^30}\33[m'.format(' DESAFIO 54 '))

M=0
m=0
from datetime import date
atual = date.today().year
for i in range(1, 8):
    n = int(input('Digite o ano de nascimento da pessoa {}: '.format(i)))
    idade = atual - n
    if idade >= 21:
        M += 1
    else:
        m += 1
print('O número de pessoas maiores de idade é {}\n'
      'e de pessoas menores de idade é {}.'.format(M, m))