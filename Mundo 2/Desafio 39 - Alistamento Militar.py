print('\33[33m='*5, 'DESAFIO 39', '='*5, '\33[m')

from datetime import date
data = int(input('Digite o ano de seu nascimento: '))
ano = date.today().year
tempo = ano - data
dif = 18 - tempo

if tempo < 18:
    print('Você \33[33mainda vai se alistar\33[m em {} anos'.format(dif))
    alist = ano + dif
    print('Seu alistamento será em {}.'.format(alist))
elif tempo == 18:
    print('\33[32mÉ hora de você se alistar\33[m')
else:
    print('Você \33[31mperdeu o prazo de se alistar\33[m passou {} anos'.format(dif*(-1)))
    alist = ano + dif
    print('Seu alistamento foi em {}.'.format(alist))