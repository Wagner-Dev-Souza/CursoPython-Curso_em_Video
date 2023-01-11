print('\33[32m='*5, 'DESAFIO 29', '='*5,'\33[m')

Vel = float(input('Qual a velocidade do carro em Km/h: '))

multa = (Vel - 80.0) * 7.00

if Vel > 80.0:
    print('\33[33mVelocidade acima do permitido: \33[31mMulta de R$ {:.2f}'.format(multa))
else:
    print('\33[32mVelocidade permitida. Tenha um bom dia! Dirija com segurança!')