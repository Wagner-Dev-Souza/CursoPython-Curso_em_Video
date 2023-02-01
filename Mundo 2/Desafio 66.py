print('\33[33m{:=^30}\33[m'.format(' DESAFIO 66 '))

soma = cont = 0
while True:
    num = int(input('Digite um número inteiro (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')