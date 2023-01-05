print('='*5, 'DESAFIO 24', '='*5)

n = input('Digite o nome da sua cidade: ')
s = n.split()
f = (s[0].lower().find('santo'))

if f != 0:
    print('O nome da sua cidade \33[31mNÃO\33[m começa com \33[33m"Santo"\33[m.')
else:
    print('O nome da sua cidade começa com \33[33m"Santo"\33[m.')
