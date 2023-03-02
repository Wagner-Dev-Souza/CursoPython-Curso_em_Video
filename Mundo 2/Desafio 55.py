print('\33[33m{:=^30}\33[m'.format(' DESAFIO 55 '))

#solução com gambiarra (menor peso iniciado por 99999)
'''M = 0
m = 99999999
for i in range(0, 5):
    n = float(input('Informe seu peso: '))
    if n > M:
        M = n
    elif n < m:
        m = n
print('O mais pesado foi {}, e o mais leve {}.'.format(M, m))'''

#solução sem gambiarra

M = 0
m = 0
for i in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))
    if i == 1:
        M = peso
        m = peso
    else:
        if peso > M:
            M = peso
        if peso < m:
            m = peso
print('O maior peso lido foi de {}kg'.format(M))
print('O menor peso lido foi de {}Kg'.format(m))