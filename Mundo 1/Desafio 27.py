print('='*5, 'DESAFIO 27', '='*5)

nome = input('Digite se nome completo: ')
s = nome.split()
i = s[0]
f = s[-1]
print('Seu primeiro nome é: \33[36m{}\33[m e seu último nome é: \33[36m{}\33[m'.format(i, f))