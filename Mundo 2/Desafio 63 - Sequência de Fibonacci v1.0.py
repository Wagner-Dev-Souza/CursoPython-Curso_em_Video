print('\33[33m{:=^30}\33[m'.format(' DESAFIO 63 '))

n = int(input('Digite um número inteiro: '))
i = 1
anterior = 0
proximo = 0
while i <= n:
    print(proximo,'->', end=' ')
    i += 1
    proximo = proximo + anterior
    anterior = proximo - anterior
    if proximo == 0:
        proximo = proximo + 1