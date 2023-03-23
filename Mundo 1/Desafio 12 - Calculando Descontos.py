print('\33[32m='*5, 'DESAFIO 12', '='*5,'\33[m')

n = float(input('Insira o preço do produto: R$ '))
p = n*0.05
print('O valor a pagar é de \33[36mR$ {:.2f}'.format(n-p))
