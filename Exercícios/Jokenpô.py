from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''\33[33mSuas opções:\33[34m
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\33[m''')
jogador = int(input('Qual é a sua jogada? '))
print('\33[33mJO')
sleep(1)
print('\33[32mKEN')
sleep(1)
print('\33[31mPO!!!\33[m')
print('\33[33m-=' * 12)
print('\33[mComputador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('\33[33m-=' * 12)
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print('[33[33mEMPATE')
    elif jogador == 1:
        print('\33[34mJOGADOR VENCE')
    elif jogador == 2:
        print('\33[31mCOMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1: # computador jogo papel
    if jogador == 0:
        print('\33[31mCOMPUTADOR VENCE')
    elif jogador == 1:
        print('\33[33mEMPATE')
    elif jogador == 2:
        print('\33[34mJOGADOR VENCE')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print('\33[34mJOGADOR VENCE')
    elif jogador == 1:
        print('\33[31mCOMPUTADOR VENCE')
    elif jogador == 2:
        print('\33[33mEMPATE')
    else:
        print('JOGADA INVALIDA!')
else:
    print('JOGADA INVALIDA!')