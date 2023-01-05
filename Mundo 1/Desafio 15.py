print('='*5, 'DESAFIO 15', '='*5)

n = int(input('Informe o número de dias em que o carro foi alugado: '))
Km = float(input('Informe a kilometragem rodada: '))
Preço = (n * 60) + (Km * 0.15)
print('\33[33mO valor total a pagar é de R${:.2f}'.format(Preço))
