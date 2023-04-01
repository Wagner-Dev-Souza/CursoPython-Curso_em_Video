print('\33[31m{:=^30}\33[m'.format(' DESAFIO 83 '))

abrindo = []
fechando = []
expressão = (input('Digite sua expressão: '))

for parentese in expressão:
    if parentese == '(':
        abrindo.append('(')
    elif parentese == (')'):
        fechando.append(')')
if len(abrindo) == len(fechando):
    print('Sua expressão é \33[32mválida\33[m!!!')
else:
    print('Sua expressão está \33[31merrada\33[m!!!')
