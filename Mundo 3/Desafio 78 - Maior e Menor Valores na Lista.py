print('\33[31m{:=^30}\33[m'.format(' DESAFIO 78 '))

valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
maior = (max(valores))
menor = (min(valores))

print('=-' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor sorteado foi {maior} nas posições ', end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}...', end='')
print()
print(f'O menor valor sorteado foi {menor} nas posições ', end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}...', end='')
print()