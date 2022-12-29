print('='*5, 'DESAFIO 25', '='*5)

nome = input('Insira seu nome completo: ')
f = nome.upper().find('SILVA')

if f != False:
    print('Seu nome possui "Silva"')
else:
    print('Seu nome NÃO possui "Silva"')