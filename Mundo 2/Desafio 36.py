print('='*5, 'Desafio 36', '='*5)

casa = float(input('Informe o valor do imóvel: '))
salario = float(input('Informe o salário do comprador: R$ '))
anos = float(input('Informe em quantos anos pretende pagar: '))

parcelas = anos * 12
pm = casa / parcelas
pmax = salario * 30 / 100


if pm > pmax:
    print('Emprestimo \33[31mNEGADO...')
else:
    print('Empréstimo \33[32mConcedido\33[m!\n'
          '\33[33mParcelas de R$ {:.2f} divididas em {} meses.'.format(pm, parcelas))