print('\33[33m{:=^30}\33[m'.format(' DESAFIO 44 '))

preco = float(input('Informe o valor do produto: R$ '))
print('''CONDIÇÕES DE PAGAMENTO:
 [ 1 ] à vista no dinheiro / cheque
 [ 2 ] à vista no cartão
 [ 3 ] 2x no cartão
 [ 4 ] 3x ou mais no cartão''')
p = int(input('Escolha a opção desejada: '))
if p == 1:
    total = preco - (preco * 10 / 100)
elif p == 2:
    total = preco - (preco * 5 / 100)
elif p == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))
elif p == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = preco
    print('Opção invalida. Tente novamente!!!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total))