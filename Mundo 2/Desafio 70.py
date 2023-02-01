print('\33[33m{:=^30}\33[m'.format(' DESAFIO 70 '))

print('-'*30)
print('{:^30}'.format(' LOJA SUPER BARATÃO '))
print('-'*30)

soma = cont = menor = 0
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    soma += preco
    if menor == 0:
        menor = preco
        mnome = nome
    else:
        if preco < menor:
            menor = preco
            mnome = nome
    if preco > 1000:
        cont += 1
    if escolha == 'N':
        break
print('{:-^30}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$ {soma:.2f}\n'
      f'Temos {cont} produtos custando mais de R$ 1000.00\n'
      f'E o produto mais barato foi {mnome} que custa {menor:.2f}')