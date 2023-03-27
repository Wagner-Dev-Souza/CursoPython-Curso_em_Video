print('\33[31m{:=^30}\33[m'.format(' DESAFIO 74 '))

from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10),
         randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {tupla}')
print(f'O maior valor sorteado foi {max(tupla)}')
print(f'o menor valor sorteado foi {min(tupla)}')