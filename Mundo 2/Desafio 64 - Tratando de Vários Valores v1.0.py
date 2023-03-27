print('\33[33m{:=^30}\33[m'.format(' DESAFIO 64 '))

n = 0
soma = -999
cont = -1
while n != 999:
    n = int(input('Digite um número inteiro: '))
    soma += n
    cont += 1
print('\nVocê digitou um total de {} números\n'
      'que totalizam um valor de {}'.format(cont, soma))