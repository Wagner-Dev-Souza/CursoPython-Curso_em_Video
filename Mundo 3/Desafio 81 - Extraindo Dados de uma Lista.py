print('\33[31m{:=^30}\33[m'.format(' DESAFIO 80 '))

valores = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    cont = input('Deseja continuar S/N? ').lower()
    if cont != 's':
        break

print('=-'*30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('Sim!!! O valor 5 faz parte da lista!')
else:
    print('Não!!! O valor 5 não faz parte da lista!')