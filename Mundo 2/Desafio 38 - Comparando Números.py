print('\33[33m='*5, 'DESAFIO 38', '='*5, '\33[m')

n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))

if n1 > n2:
    print('O \33[33mPRIMEIRO valor\33[m é \33[34mmaior.')
elif n2 > n1:
    print('O \33[33mSEGUNDO valor\33[m é \33[34mmaior.')
else:
    print('\33[33mNão existe\33[m valor maior, os dois são \33[34mIGUAIS.')

