print('\33[33m{:=^30}\33[m'.format(' DESAFIO 61 '))

n = 0
pri_ter = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
while n < 10:
    print(pri_ter + (razao * n), end='->')
    n += 1
