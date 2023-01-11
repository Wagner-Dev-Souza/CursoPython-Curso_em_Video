print('\33[32m='*5, 'DESAFIO 25', '='*5,'\33[m')

nome = str(input('Insira seu nome completo: ').strip())
f = ('silva' in nome.lower())

if f != False:
    print('Seu nome possui \33[32m"Silva"\33[m')
else:
    print('Seu nome \33[35mNÃO\33[m possui \33[36m"Silva"\33[m')
