print('=' * 5, 'DESAFIO 6', '=' * 5)

n = int(input('Digite um valor: '))
n1 = n * 2
n2 = n * 3
n3 = n ** (1 / 2)
print('{}O dobro é {},{} o triplo é {}{} e a raiz quadrada é {:.2f}'. format('\33[31m', n1,'\33[32m', n2,'\33[33m', n3))