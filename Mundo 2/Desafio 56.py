print('\33[33m{:=^30}\33[m'.format(' DESAFIO 56 '))

media = 0
velho = 0
nome = 'Nenhum'
menor = 0
for p in range(1, 5):
    print('{:-^30}'.format(' {}ª PESSOA ').format(p))
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo (M/F): '))
    media += i / 4
    if i > velho and s in 'Mm':
        velho = i
        nome = n
    elif s in 'Ff' and i < 20:
        menor += 1

print('\nA média da idade desse grupo é {}\n'
      'O nome do homem mais velho é {} ele tem {} anos\n'
      'e existem {} mulheres com menos de 20 anos no grupo.'.format(media, nome, velho, menor))