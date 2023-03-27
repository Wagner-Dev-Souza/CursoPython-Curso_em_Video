print('\33[33m{:=^30}\33[m'.format(' DESAFIO 52 '))

n = int(input('Digite um número inteiro: '))
mult = 0
for count in range(1, n + 1):
    if n % count == 0:
        print('\33[33m', end='')
        mult += 1
    else:
        print('\33[31m', end='')
    print('{} '.format(count), end='')
print('\n\33[mO número {} foi divisível {} vezes'.format(n, mult))

if mult == 2:
    print("E por isso ele É PRIMO!")
else:
    print('E por isso ele NÃO É PRIMO!')
