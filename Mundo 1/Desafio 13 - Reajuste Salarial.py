print('\33[32m='*5, 'DESAFIO 134', '='*5,'\33[m')

n = float(input('Insira seu salário atual: R$ '))
s = n*0.15
print('Seu novo salário é:\33[35m R$ {:.2f}'.format(n+s))

