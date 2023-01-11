print('\33[33m{:=^30}\33[m'.format(' DESAFIO 45 '))

from random import choice

print('-=-' * 10)
print('\33[31m          JOKENPÔ\33[m')
print('-=-' * 10)
lista = ['papel', 'pedra', 'tesoura']
x = choice(lista)
n = str(input('Faça sua escolha: '))
print('\33[36mEu escolhi',x)
if n == 'papel' and x == 'pedra':
    print('\33[32mVocê me venceu: papel embrulha pedra!!!')
elif n == 'papel' and x == 'tesoura':
    print('\33[31mVocê perdeu: tesoura corta papel!!!')
elif n == 'tesoura' and x == 'pedra':
    print('\33[31mVocê perdeu: pedra quebra tesoura!!!')
elif n == 'tesoura' and x == 'papel':
    print('\33[32mVocê me venceu: tesoura corta papel!!!')
elif n == 'pedra' and x == 'papel':
    print('\33[31mVocê perdeu: papel embrulha pedra!!!')
elif n == 'pedra' and x == 'tesoura':
    print('\33[32mVocê me venceu: pedra quebra tesoura!!!')
else:
    print('\33[33mEmpatou... Tente outra vez!!!')


