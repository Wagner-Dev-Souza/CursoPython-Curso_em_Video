print('\33[33m='*5, 'DESAFIO 41', '='*5, '\33[m')

from datetime import date

n = int(input('Digite o ano de nascimento do atleta: \33[34m'))
date = date.today().year
time = date - n
if time <= 9:
    print('MIRIM')
elif time > 9 and time <= 14:
    print('INFANTIL')
elif time > 14 and time <=19:
    print('JUNIOR')
elif time == 20:
    print('SÊNIOR')
else:
    print('MASTER')