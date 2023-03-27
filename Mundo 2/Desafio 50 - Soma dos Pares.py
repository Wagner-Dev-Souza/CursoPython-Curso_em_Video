print('\33[33m{:=^30}\33[m'.format(' DESAFIO 50 '))

s = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor inteiro: '.format(c)))
    x = n % 2
    if x == 0:
        s = s + n
print('A soma dos números pares é igual a {}'.format(s))