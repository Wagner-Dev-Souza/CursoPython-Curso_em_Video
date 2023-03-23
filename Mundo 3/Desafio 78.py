print('\33[31m{:=^30}\33[m'.format(' DESAFIO 78 '))

valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print(f'Você digitou os valores {valores}')
max = (max(valores))
print(max.index())
print(f'O maior valor sorteado foi {max(valores)} nas posições {max(cont)}...', end=' ')
print(f'\nO menor valor sorteado foi {min(valores)} nas posições {min(cont)}...', end=' ')
