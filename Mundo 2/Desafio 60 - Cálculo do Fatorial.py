print('\33[33m{:=^30}\33[m'.format(' DESAFIO 60 '))


numero = int(input('Insira um número: '))
fatorial = 1
i = 2
while i <= numero:
    fatorial = fatorial * i
    i += 1
print(fatorial)