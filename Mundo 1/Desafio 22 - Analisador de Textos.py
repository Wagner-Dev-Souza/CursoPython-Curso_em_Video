print('\33[32m='*5, 'DESAFIO 22', '='*5,'\33[m')

nome = input('Digite seu nome completo: \33[34m')
print(nome.upper())
print(nome.lower())
print(len(nome.replace(" ", "")))
print(len(nome.split()[0]))