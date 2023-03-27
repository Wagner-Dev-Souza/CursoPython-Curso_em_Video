print('\33[33m{:=^30}\33[m'.format(' DESAFIO 62 '))

n = 0
fim = 1
pri_ter = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
while n < 10:
    print(pri_ter + (razao * n), end='->')
    n += 1
while fim != 0:
    fim = int(input('Ver mais quantos termos? '))
    m = 0
    while m < fim:
        print(pri_ter + (razao * n), end='->')
        m += 1
        n += 1
print('Voce digitou {} termos dessa PA.'.format(total))
print('\33[31mFIM')