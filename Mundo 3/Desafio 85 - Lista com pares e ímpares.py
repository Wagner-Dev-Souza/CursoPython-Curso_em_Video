print('\33[31m{:=^30}\33[m'.format(' DESAFIO 85 '))

lista = [[], []]
for i in range(1, 8):
    num = int(input(f'Digite o {i}° valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')
