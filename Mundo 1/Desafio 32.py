print('='*5, 'DESAFIO 32', '='*5)

import calendar
from datetime import date
ano = int(input('Digite o ano com 4 digitos: '))
if ano == 0:
    ano = date.today().year
b = calendar.isleap(ano)
# ano bissexto é =  ano % 4 == 0 and (ano % 100 != 0 and % 400 == 0)
if b == True:
    print('Sim, o ano de {} é bissexto.'.format(ano))
else:
    print('Não, o ano de {} não é bissexto.'.format(ano))

