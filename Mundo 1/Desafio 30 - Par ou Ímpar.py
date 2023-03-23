print('\33[32m='*5, 'DESAFIO 30', '='*5,'\33[m')

n = int(input('Digite um numero inteiro: '))
d = n % 2

if d == 0:
    print('O numero inserido é \33[32mpar!!!')
else:
    print('O número inserido é \33[31mímpar!!!')