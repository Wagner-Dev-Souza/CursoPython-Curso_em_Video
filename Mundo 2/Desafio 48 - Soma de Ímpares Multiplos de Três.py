print('\33[33m{:=^30}\33[m'.format(' DESAFIO 48 '))

s = 0
c = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i
        c += 1
        print(i, end=" ")

print('\nA soma  de todos os {} números ímpares\n'
'múltiplos de 3 no intervalo de 1 até 500\n'
'é igual a: {}'.format(c, s))
