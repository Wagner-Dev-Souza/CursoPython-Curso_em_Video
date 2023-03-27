print('\33[33m='*5, 'DESAFIO 37', '='*5, '\33[m')

n = int(input('Digite um número inteiro: '))

print('''\33[34m[ 1 ]\33[m para \33[33mbinário
\33[34m[ 2 ]\33[m para \33[33moctal
\33[34m[ 3 ]\33[m para \33[33mhexadecimal\33[m''')
op = int(input('Escolha o número correspondente para converção: \33[36m'))
b = bin(n)[2:]
o = oct(n)[2:]
h = hex(n)[2:]
if op == 1:
    print('O número {} em binário é: {}'.format(n, b))
elif op == 2:
    print('O número {} em octal é: {}'.format(n, o))
elif op == 3:
    print('O número {} em hexadecimal é: {}'.format(n, h))
else:
    print('Opção invalida. Tente novamente.')
