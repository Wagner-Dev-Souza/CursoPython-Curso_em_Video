print('\33[33m{:=^30}\33[m'.format(' DESAFIO 67 '))

num = 0
while True:
    print('-' * 30)
    num = int(input('Quer ver a tabuada de que valor? '))
    print('-' * 30)
    if num < 0:
        break
    for c in range(0, 11):
        print(f'{num} x {c} = {num*c}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!!!')