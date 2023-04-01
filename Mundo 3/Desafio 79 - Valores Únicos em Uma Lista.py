print('\33[31m{:=^30}\33[m'.format(" DESAFIO 79 "))

valores = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        print('Valor adicionado com sucesso...')
        valores.append(n)
    else:
        print('Valor duplicado! Não vou adicionar...')
    cond = input('Deseja continuar S/N? ').lower()
    if cond != 's':
        break

print('=-'*30)
print(f'Você digitou os valores {sorted(valores)}')