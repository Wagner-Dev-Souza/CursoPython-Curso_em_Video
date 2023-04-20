print('\33[31m{:=^30}\33[m'.format(' DESAFIO 87 '))

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite um valor para [{l}, {c}]: ')))
print('-=' * 30)
somapar = maior = somacol = 0
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print('-='*30)
for l in range(0, 3):
    somacol += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    if matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'A soma dos valores pares é {somapar}.')
print(f'A soma dos valores da terceira coluna é {somacol}.')
print(f'O maior valor da segunda linha é {maior}')