print('='*5, 'DESAFIO 23', '='*5)

#n = input('Digite um número inteiro de 4 digitos: ')
#print('Analizando o número {}'.format(n))
#print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(n[3], n[2], n[1], n[0]))

##num = 1984
##unidade = num // 1 % 10 # 4
##dezena = num // 10 % 10 #8
##centena = num // 100 % 10 # 9
##milhar = num // 1000 % 10 # 1

n = int(input('Insira um número de 0 a 9999: '))
uni = n // 1 % 10
dez = n // 10 % 10
cen = n // 100 % 10
mil = n // 1000 % 10
print('Analizando o número {}'.format(n))
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(uni, dez, cen, mil))
