print('\33[33m{:=^30}\33[m'.format(' DESAFIO 48 '))

n = int(input('Insira um número: '))
for c in range(0, 11):
    print('{} * {} = {}'.format(n, c, n*c))