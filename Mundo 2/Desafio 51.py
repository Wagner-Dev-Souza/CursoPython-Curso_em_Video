print('\33[33m{:=^30}\33[m'.format(' DESAFIO 51 '))

n = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
for c in range(n, n + r * 10, r):
    print(c, end='->')