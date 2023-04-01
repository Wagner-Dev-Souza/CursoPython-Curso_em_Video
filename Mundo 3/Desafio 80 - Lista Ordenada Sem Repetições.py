print('\33[31m{:=^30}\33[m'.format(' DESAFIO 80 '))

valores = list()

for cont in range(0, 5):
    n = int(input('Digite um valor: '))
    if valores == []:
        valores.append(n)
        print('Adicionado ao final da lista...')
    elif n > max(valores):
        valores.append(n)
        print('Adicionado ao final da lista...')
    elif n <= valores[0]:
        valores.insert(0, n)
        print('Adicionado na posição 0 da lista...')
    elif n > valores[0] and n <= valores[1]:
        valores.insert(1, n)
        print('Adicionado na posição 1 da lista...')
    elif n > valores[1] and n <= valores[2]:
        valores.insert(2, n)
        print('Adicionado na posição 2 da lista...')
    elif n > valores[2] and n <= valores[3]:
        valores.insert(3, n)
        print('Adicionado na posição 3 da lista...')

print('=-'*30)
print(f'Os valores digitados em ordem foram {valores}')