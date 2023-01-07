print('='*5, 'DESAFIO 43', '='*5)

p = float(input('Digite seu peso: '))
h = float(input('Digite sua altura: '))
imc = p / (h * h)
if imc < 18.5:
    print('\33[34mVocê está Abaixo do Peso...')
elif imc >= 18.5 and imc < 25:
    print('\33[32mVocê está no Peso Ideal...')
elif imc >=25 and imc <30:
    print('\33[33mVocê está com Sobrepeso...')
elif imc >=30 and imc < 40:
    print('\33[31mVocê está com Obesidade...')
else:
    print('\33[35mVocê está com Obesidade Mórbida...')