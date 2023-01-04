print('='*5, 'DESAFIO 10', '='*5)

n = float(input('Digite seu valor em reais: R$ '))
m = float(input('Insira o valor da cotação do dolar em reais: R$ '))
x = n/m
print('\33[32mVocê pode comprar \33[31m{:.2f}\33[32m dólares'.format(x))