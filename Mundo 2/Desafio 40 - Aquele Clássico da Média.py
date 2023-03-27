print('\33[33m='*5, 'DESAFIO 40', '='*5, '\33[m')

m1 = float(input('Digite a primeira nota: '))
m2 = float(input('Digite a segunda nota: '))
media = (m1 + m2) / 2
if media < 5.0:
    print('\33[31mREPROVADO\33[m')
elif media > 7.0:
    print('\33[32mAPROVADO\33[m')
else:
    print('\33[33mRECUPERAÇÃO\33[m')