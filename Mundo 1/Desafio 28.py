print('='*5, 'DESAFIO 28', '='*5)

from random import randint
from time import sleep
n = randint(0, 5)
print('-=-' * 20)
print('Leia minha mente e descubra o número que eu estou pensando!!!')
print('-=-' * 20)
x = int(input('Digite um número inteiro entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)
if n != x:
    print('ERROU!!! Eu pensei no número {}'.format(n))
else:
    print('PARABÉNS!!! Acertou exatamento o número que eu estava pensando: "{}"'.format(n))

