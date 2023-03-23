print('\33[32m='*5, 'DESAFIO 35', '='*5,'\33[m')

print('-='*20)
print('ANALISADOR DE TRIÂNGULO')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \33[32mPODEM FORMAR\33[m triângulo!')
else:
    print('Os segmentos acima \33[31mNÃO PODEM FORMAR\33[m triângulo!')
