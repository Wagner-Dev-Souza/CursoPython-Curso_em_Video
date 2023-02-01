print('\33[33m{:=^30}\33[m'.format(' DESAFIO 71 '))

print('='*30)
print('{:^30}'.format(' BANCO CEV '))
print('='*30)

valor = int(input('Que valor você quer sacar? R$ '))
cinq = valor // 50
valor = valor - (50 * cinq)
vint = valor // 20
valor = valor - (20 * vint)
dez = valor // 10
valor = valor - (10 * dez)
um = valor // 1

if cinq > 0:
    print(f'Total de {cinq} cédulas de R$ 50')
if vint > 0:
    print(f'Total de {vint} cédulas de R$ 20')
if dez > 0:
    print(f'Total de {dez} cédulas de R$ 10')
if um > 0:
    print(f'Total de {um} cédulas de R$ 1')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')