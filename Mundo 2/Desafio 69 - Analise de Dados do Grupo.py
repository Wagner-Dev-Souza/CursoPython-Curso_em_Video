print('\33[33m{:=^30}\33[m'.format(' DESAFIO 69 '))

cont = homem = mulher = 0
while True:
    print('-'*30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]
    print('-' * 30)
    escolha = ' '
    while escolha not in 'sn':
        escolha = str(input('Quer continuar? [S/N]')).strip().lower()[0]
    if idade > 18:
        cont += 1
    if sexo == 'm':
        homem += 1
    if sexo == 'f' and idade < 20:
        mulher += 1
    if escolha == 'n':
        break
print('{:=^30}'.format(' FIM DO PROGRAMA '))
print(f'Total de pessoas com mais de 18 anos: {cont}\n'
      f'Ao todo temos {homem} homens cadastrados\n'
      f'E temos {mulher} mulheres com menos de 20 anos.')