print('\33[31m{:=^30}\33[m'.format(' DESAFIO 88 '))

from random import randint
from time import sleep

print("-"*30)
print('{:^30}'.format('PALPITATOR DA MEGA SENA'))
print("-"*30)
n = int(input('Quantos jogos serão gerados? '))
lista = list()
jogos = list()
total = 0
while total < n:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 2, f' SORTEANDO {n} JOGOS ', '-=' * 2)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
print('{:=^30}'.format(' <BOA SORTE> '))