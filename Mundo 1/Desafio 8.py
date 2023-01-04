print('=' * 5, 'DESAFIO 8', '=' * 5)

n = float(input('Digite o valor em metros: '))
c = n * 100
m = n * 1000
print('O valor possui \33[33m{:.0f}\33[m centímetros e \33[33m{:.0f}\33[m milímetros'.format(c, m))
