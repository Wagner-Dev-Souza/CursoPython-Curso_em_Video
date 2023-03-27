print('\33[31m{:=^30}\33[m'.format(' DESAFIO 77 '))

palavras = ('aprender', 'programar', 'liguagem',
            'python', 'curso', 'grátis', 'estudar',
            'paticar', 'tabalhar', 'mercado', 'programador',
            'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aáeiou':
            print(letra, end=' ')