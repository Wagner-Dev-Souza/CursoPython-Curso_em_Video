print('\33[31m{:=^30}\33[m'.format(' Desafio 82 '))

valores = list()

while True:
    valores.append(int(input('Digite um número: ')))
    cont = (input('Deseja continuar S/N? ')).lower()
    if cont != 's':
        break

print('=-'*30)
print(f'A lista completa é {valores}')
pares = list()
ímpares = list()
for i in valores:
    if i % 2 == 0:
        pares.append(i)
    else:
        ímpares.append(i)
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')