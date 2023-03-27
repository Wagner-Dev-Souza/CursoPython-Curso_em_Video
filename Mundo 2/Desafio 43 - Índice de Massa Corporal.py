print('\33[33m='*5, 'DESAFIO 43', '='*5, '\33[m')

p = float(input('Digite seu peso (Kg): '))
h = float(input('Digite sua altura (m): '))
imc = p / (h * h)
print('O IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('\33[34mVocê está ABAIXO DO PESO normal...')
elif imc >= 18.5 and imc < 25:
    print('\33[32mParabéns, você está no PESO IDEAL...')
elif imc >=25 and imc <30:
    print('\33[33mVocê está com SOBREPESO...')
elif imc >=30 and imc < 40:
    print('\33[31mVocê está com OBESIDADE!!!')
else:
    print('\33[35mVocê está com OBESIDADE MÓRBIDA, CUIDADO!!!')