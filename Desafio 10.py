print('='*5, 'DESAFIO 10', '='*5)

n = float(input('Digite seu valor em reais: R$ '))
m = float(input('Insira o valor da cotação do dolar em reais: R$ '))
x = n/m
print('Você pode comprar {:.2f} dólares'.format(x))