print('='*5, 'DESAFIO 31', '='*5)

d = float(input('Digite a distância da viagem em Km: '))

if d <= 200:
    print('O valor da passagem é de R$ {:.2f}'.format(d * 0.50))
else:
    print('O valor da passagem é de R$ {:.2f}'.format(d * 0.45))
