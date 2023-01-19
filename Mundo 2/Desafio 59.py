print('\33[33m{:=^30}\33[m'.format(' DESAFIO 59 '))

escolha = 4
while escolha != 5:
    valor1 = float(input('Digite um valor: '))
    valor2 = float(input('Digite outro valor: '))
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair''')
    escolha = int(input('Escolha a operação: '))
    if escolha == 1:
        print(valor1 + valor2)
    elif escolha == 2:
        print(valor1 * valor2)
    elif escolha == 3:
        if valor1 > valor2:
            maior = valor1
            print('O maior número é {}'.format(maior))
        elif valor2 > valor1:
            maior = valor2
            print('O maior número é {}'.format(maior))
        else:
            print('Ambos os valores são iguais')

