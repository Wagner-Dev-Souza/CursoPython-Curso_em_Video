print('\33[33m{:=^30}\33[m'.format(' DESAFIO 57 '))

confirma = ''
while confirma != 'S':
    sexo = ''
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Informe seu sexo (M/F): ').upper())
        if sexo == 'M':
            confirma = str(input('Você digitou masculino, confirma (S/N)? ')).upper()
        elif sexo == 'F':
            confirma = str(input('Você digitou feminino, confirma (S/N)? ')).upper()
        else:
            print('Informação incorreta...')
print('Obrigado!!!')