'''while not apple:
    passo
pega'''

'''while not apple:
    if chão:
        passo
    if buraco:
        pula
    if moeda:
        pega
pega'''

for c in range (1, 10):
    print(c)
print('Fim')
#com while fica
'''c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')'''
#######
'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')'''
######
r = 'S'
'''while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''
#######
j = 1
par = impar = 0
while j != 0:
    j = int(input('Digite um valor: '))
    if j != 0:
        if j %2 == 0:
            par += 1
        else:
            impar +=1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))

