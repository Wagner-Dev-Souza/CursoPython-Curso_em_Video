print('='*5, 'DESAFIO 34', '='*5)

n = float(input('Digite seu salário atual: R$ '))

if n > 1250.00:
    a = (n * 10) / 100
    t = n + a
    print('Você receberá um aumento de 10% no seu salário.')
    print('Seu aumento é de R${}, e seu novo salário atual totalizará R${}'.format(a, t))
else:
    a = (n * 15) / 100
    t = n + a
    print('Voce receberá um aumento de 15% no seu salário.')
    print('Seu aumento é de R$ {}, e seu novo salário atual totalizará R${}'.format(a, t))
