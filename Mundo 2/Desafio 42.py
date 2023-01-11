print('\33[33m='*5, 'DESAFIO 42', '='*5, '\33[m')

print('-='*20)
print('\33[31mANALISADOR DE TRIÂNGULO 2.0\33[m')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \33[32mPODEM FORMAR\33[m triângulo!')
    if r1 == r2 and r2 == r3:
        print('\33[34mTriângulo Equilátero')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('\33[34mTriângulo Escaleno')
    else:
        print('\33[34mTriângulo Isósceles')
else:
    print('Os segmentos acima \33[31mNÃO PODEM FORMAR\33[m triângulo!')
