print('='*5, 'DESAFIO 44', '='*5)

n = float(input('Informe o valor do produto: R$ '))
p = str(input('Informe a condição de pagamento: '))
if p == 'dinheiro' or p == 'cheque':
    print('Valor a pagar: R$ {:.2f}'.format(n - n * 10 / 100))
elif p == 'cartão':
    x = int(input('Quantas parcelas? '))
    if x == 1:
        print('Valor a pagar: R$ {:.2f}'.format(n - n * 5 / 100))
    elif x == 2:
        print('Valor a pagar: R$ {:.2f}, em duas vezes de R$ {:.2f}'.format(n, n / 2))
    else:
        print('Valor a pagar: R$ {:.2f}, em {}x de R$ {:.2f}'.format(n + n * 20 / 100, x, (n + n * 20 / 100) / x))