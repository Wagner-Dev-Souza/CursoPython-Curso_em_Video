print('\33[33m{:=^30}\33[m'.format(' DESAFIO 58 '))

from random import randint
from time import sleep

print('-=-' * 20)
print('\33[33mLeia minha mente e descubra o número que eu estou pensando!!!\33[m')
print('-=-' * 20)
jogador = ''
pc = randint(0, 10)
cont = 1
while pc != jogador:
    jogador = int(input('Digite um número inteiro entre \33[31m0 e 10\33[m: '))
    print('\33[35mPROCESSANDO...\33[m')
    sleep(2)
    if pc != jogador:
        cont += 1
        print('\33[31mERROU!!! Tente outra vez...\33[m')

    else:
        print('\33[32mPARABÉNS!!! Acertou exatamento o número que eu estava pensando: \33[36m"{}"\33[m'.format(pc))
print('Você precisou de {} tentativas para acertar dessa vez'.format(cont))