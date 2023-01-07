print('='*5, 'DESAFIO 37', '='*5)

n = int(input('Digite um número inteiro: '))

print('\33[34m1\33[m para \33[33mbinário\n'
      '\33[34m2\33[m para \33[33moctal\n'
      '\33[34m3\33[m para \33[33mhexadecimal\33[m')
op = int(input('Escolha o número correspondente para converção: \33[36m'))
b = 0
o = 0
h = 0
if op == 1:
    print('O número {} em binário é: {}'.format(n, b))
elif op == 2:
    print('O número {} em octal é: {}'.format(n, o))
elif op == 3:
    print('O número {} em hexadecimal é: {}'.format(n, h))
