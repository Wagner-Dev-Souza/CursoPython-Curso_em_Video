print('='*5, 'DESAFIO 28', '='*5)

from random import randint
from time import sleep
n = randint(0, 5)
print('-=-' * 20)
print('\33[33mLeia minha mente e descubra o número que eu estou pensando!!!\33[m')
print('-=-' * 20)
x = int(input('Digite um número inteiro entre \33[31m0 e 5\33[m: '))
print('\33[35mPROCESSANDO...\33[m')
sleep(2)
if n != x:
    print('\33[31mERROU!!! Eu pensei no número \33[35m{}\33[m'.format(n))
else:
    print('\33[32mPARABÉNS!!! Acertou exatamento o número que eu estava pensando: \33[36m"{}"\33[m'.format(n))

