'''aula bonus de cores no terminal'''

print('\33[4;3;31mOlá, Mundo!\33[m')

a = 3
b = 5
print('Os valores são \33[32m{}\33[m e \33[31m{}\33[m!!!'.format(a, b))

nome = 'Wagner'
print('Olá, Muito prazer em te conhecer, {}{}{}!!!'.format('\33[4;34m', nome, '\33[m'))

nome = 'Grasielle'
cores = {'limpa':'\33[m',
        'azul':'\33[34m',
        'amarelo':'\33[33m',
        'pretoebranco':'\33[7m'}
print('Olá, que nome bonito você tem {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))