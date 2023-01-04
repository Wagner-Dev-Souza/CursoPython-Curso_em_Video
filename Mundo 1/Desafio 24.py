print('='*5, 'DESAFIO 24', '='*5)

n = input('Digite o nome da sua cidade: ')
s = n.split()
f = (s[0].lower().find('santo'))

if f != 0:
    print('O nome da sua cidade NÃO começa com "Santo".')
else:
    print('O nome da sua cidade começa com "Santo".')
