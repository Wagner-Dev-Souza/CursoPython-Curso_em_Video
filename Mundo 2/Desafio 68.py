print('\33[33m{:=^30}\33[m'.format(' DESAFIO 68 '))

from random import randint

soma = cont = 0
while True:
    PC = randint(0, 10)
    escolha = ' '
    while escolha not in 'pi':
        escolha = str(input('Escolha PAR ou ÍMPAR: [P/I] ')).lower().strip()[0]
    jogador = int(input('Digite um número: '))
    cont +=1
    soma = PC + jogador
    resultado = soma % 2
    if resultado == 0:
        resultado = 'par'
    else:
        resultado = 'impar'
    print(f'Eu escolhi {PC} e você {jogador}.\n'
          f'A soma é {soma} que é {resultado}')
    if escolha == resultado[0]:
        print('Você venceu...')
    else:
        break

print(f'VENCI você depois de {cont - 1} derrotas...')